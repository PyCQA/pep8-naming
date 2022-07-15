"""Checker of PEP-8 Naming Conventions."""
import sys
from collections import deque
from fnmatch import fnmatch
from functools import partial
from itertools import chain

from flake8 import style_guide

try:
    import ast
    from ast import iter_child_nodes
except ImportError:
    from flake8.util import ast, iter_child_nodes

__version__ = '0.13.1'

PYTHON_VERSION = sys.version_info[:3]

CLASS_METHODS = frozenset((
    '__new__',
    '__init_subclass__',
    '__class_getitem__',
))
METACLASS_BASES = frozenset(('type', 'ABCMeta'))

# Node types which may contain class methods
METHOD_CONTAINER_NODES = {
    ast.If,
    ast.While,
    ast.For,
    ast.With,
    ast.Try,
    ast.AsyncWith,
    ast.AsyncFor,
}
FUNC_NODES = (ast.FunctionDef, ast.AsyncFunctionDef)

if PYTHON_VERSION < (3, 8):
    def get_arg_name_tuples(node):
        groups = (node.args.args, node.args.kwonlyargs)
        return [(arg, arg.arg) for args in groups for arg in args]
else:
    def get_arg_name_tuples(node):
        groups = (node.args.posonlyargs, node.args.args, node.args.kwonlyargs)
        return [(arg, arg.arg) for args in groups for arg in args]


class _ASTCheckMeta(type):
    def __init__(cls, class_name, bases, namespace):
        cls.codes = tuple(code for code in namespace if code.startswith('N'))
        try:
            cls.all.append(cls())
        except AttributeError:
            cls.all = []


def _err(self, node, code, **kwargs):
    lineno, col_offset = node.lineno, node.col_offset
    if isinstance(node, ast.ClassDef):
        if PYTHON_VERSION < (3, 8):
            lineno += len(node.decorator_list)
        col_offset += 6
    elif isinstance(node, FUNC_NODES):
        if PYTHON_VERSION < (3, 8):
            lineno += len(node.decorator_list)
        col_offset += 4
    code_str = getattr(self, code)
    if kwargs:
        code_str = code_str.format(**kwargs)
    return lineno, col_offset + 1, f'{code} {code_str}', self


def _ignored(name, ignore):
    return any(fnmatch(name, i) for i in ignore)


BaseASTCheck = _ASTCheckMeta('BaseASTCheck', (object,),
                             {'__doc__': "Base for AST Checks.", 'err': _err})


class _FunctionType:
    CLASSMETHOD = 'classmethod'
    STATICMETHOD = 'staticmethod'
    FUNCTION = 'function'
    METHOD = 'method'


_default_ignore_names = [
        'setUp',
        'tearDown',
        'setUpClass',
        'tearDownClass',
        'setUpModule',
        'tearDownModule',
        'asyncSetUp',
        'asyncTearDown',
        'setUpTestData',
        'failureException',
        'longMessage',
        'maxDiff']
_default_classmethod_decorators = ['classmethod']
_default_staticmethod_decorators = ['staticmethod']


def _build_decorator_to_type(classmethod_decorators, staticmethod_decorators):
    decorator_to_type = {}
    for decorator in classmethod_decorators:
        decorator_to_type[decorator] = _FunctionType.CLASSMETHOD
    for decorator in staticmethod_decorators:
        decorator_to_type[decorator] = _FunctionType.STATICMETHOD
    return decorator_to_type


class NamingChecker:
    """Checker of PEP-8 Naming Conventions."""
    name = 'naming'
    version = __version__
    visitors = BaseASTCheck.all
    decorator_to_type = _build_decorator_to_type(
        _default_classmethod_decorators, _default_staticmethod_decorators)
    ignore_names = frozenset(_default_ignore_names)

    def __init__(self, tree, filename):
        self.parents = deque()
        self._node = tree

    @classmethod
    def add_options(cls, parser):
        parser.add_option(
            '--ignore-names',
            default=_default_ignore_names,
            parse_from_config=True,
            comma_separated_list=True,
            help='List of names or glob patterns the pep8-naming '
            'plugin should ignore. (Defaults to %(default)s)',
        )
        parser.add_option(
            '--classmethod-decorators',
            default=_default_classmethod_decorators,
            parse_from_config=True,
            comma_separated_list=True,
            help='List of method decorators pep8-naming plugin '
            'should consider classmethods (Defaults to '
            '%(default)s)',
        )
        parser.add_option(
            '--staticmethod-decorators',
            default=_default_staticmethod_decorators,
            parse_from_config=True,
            comma_separated_list=True,
            help='List of method decorators pep8-naming plugin '
            'should consider staticmethods (Defaults to '
            '%(default)s)',
        )
        parser.extend_default_ignore(['N818'])

    @classmethod
    def parse_options(cls, options):
        cls.ignore_names = frozenset(options.ignore_names)
        cls.decorator_to_type = _build_decorator_to_type(
            options.classmethod_decorators,
            options.staticmethod_decorators)

        # Build a list of node visitors based the error codes that have been
        # selected in the style guide. Only the checks that have been selected
        # will be evaluated as a performance optimization.
        engine = style_guide.DecisionEngine(options)
        cls.visitors = frozenset(
            visitor for visitor in BaseASTCheck.all for code in visitor.codes
            if engine.decision_for(code) is style_guide.Decision.Selected
        )

    def run(self):
        return self.visit_tree(self._node) if self._node else ()

    def visit_tree(self, node):
        yield from self.visit_node(node)
        self.parents.append(node)
        for child in iter_child_nodes(node):
            yield from self.visit_tree(child)
        self.parents.pop()

    def visit_node(self, node):
        if isinstance(node, ast.ClassDef):
            self.tag_class_functions(node)
        elif isinstance(node, FUNC_NODES):
            self.find_global_defs(node)

        method = 'visit_' + node.__class__.__name__.lower()
        parents = self.parents
        ignore_names = self.ignore_names
        for visitor in self.visitors:
            visitor_method = getattr(visitor, method, None)
            if visitor_method is None:
                continue
            yield from visitor_method(node, parents, ignore_names)

    def tag_class_functions(self, cls_node):
        """Tag functions if they are methods, classmethods, staticmethods"""
        # tries to find all 'old style decorators' like
        # m = staticmethod(m)
        late_decoration = {}
        for node in iter_child_nodes(cls_node):
            if not (isinstance(node, ast.Assign) and
                    isinstance(node.value, ast.Call) and
                    isinstance(node.value.func, ast.Name)):
                continue
            func_name = node.value.func.id
            if func_name not in self.decorator_to_type:
                continue
            meth = (len(node.value.args) == 1 and node.value.args[0])
            if isinstance(meth, ast.Name):
                late_decoration[meth.id] = self.decorator_to_type[func_name]

        # If this class inherits from a known metaclass base class, it is
        # itself a metaclass, and we'll consider all of its methods to be
        # classmethods.
        bases = chain(
            (b.id for b in cls_node.bases if isinstance(b, ast.Name)),
            (b.attr for b in cls_node.bases if isinstance(b, ast.Attribute)),
        )
        ismetaclass = any(name for name in bases if name in METACLASS_BASES)

        self.set_function_nodes_types(
            iter_child_nodes(cls_node), ismetaclass, late_decoration)

    def set_function_nodes_types(self, nodes, ismetaclass, late_decoration):
        # iterate over all functions and tag them
        for node in nodes:
            if type(node) in METHOD_CONTAINER_NODES:
                self.set_function_nodes_types(
                    iter_child_nodes(node), ismetaclass, late_decoration)
            if not isinstance(node, FUNC_NODES):
                continue
            node.function_type = _FunctionType.METHOD
            if node.name in CLASS_METHODS or ismetaclass:
                node.function_type = _FunctionType.CLASSMETHOD
            if node.name in late_decoration:
                node.function_type = late_decoration[node.name]
            elif node.decorator_list:
                for d in node.decorator_list:
                    name = self.find_decorator_name(d)
                    if name in self.decorator_to_type:
                        node.function_type = self.decorator_to_type[name]
                        break

    @classmethod
    def find_decorator_name(cls, d):
        if isinstance(d, ast.Name):
            return d.id
        elif isinstance(d, ast.Attribute):
            return d.attr
        elif isinstance(d, ast.Call):
            return cls.find_decorator_name(d.func)

    @staticmethod
    def find_global_defs(func_def_node):
        global_names = set()
        nodes_to_check = deque(iter_child_nodes(func_def_node))
        while nodes_to_check:
            node = nodes_to_check.pop()
            if isinstance(node, ast.Global):
                global_names.update(node.names)

            if not isinstance(node, (ast.ClassDef,) + FUNC_NODES):
                nodes_to_check.extend(iter_child_nodes(node))
        func_def_node.global_names = global_names


class ClassNameCheck(BaseASTCheck):
    """
    Almost without exception, class names use the CapWords convention.

    Classes for internal use have a leading underscore in addition.
    """
    N801 = "class name '{name}' should use CapWords convention"
    N818 = "exception name '{name}' should be named with an Error suffix"

    @classmethod
    def get_classdef(cls, name, parents):
        for parent in parents:
            for node in parent.body:
                if isinstance(node, ast.ClassDef) and node.name == name:
                    return node

    @classmethod
    def superclass_names(cls, name, parents, _names=None):
        names = _names or set()
        classdef = cls.get_classdef(name, parents)
        if not classdef:
            return names
        for base in classdef.bases:
            if isinstance(base, ast.Name) and base.id not in names:
                names.add(base.id)
                names.update(cls.superclass_names(base.id, parents, names))
        return names

    def visit_classdef(self, node, parents, ignore=None):
        name = node.name
        if _ignored(name, ignore):
            return
        name = name.strip('_')
        if not name[:1].isupper() or '_' in name:
            yield self.err(node, 'N801', name=name)
        superclasses = self.superclass_names(name, parents)
        if "Exception" in superclasses and not name.endswith("Error"):
            yield self.err(node, 'N818', name=name)


class FunctionNameCheck(BaseASTCheck):
    """
    Function names should be lowercase, with words separated by underscores
    as necessary to improve readability.

    Functions *not* being methods '__' in front and back are not allowed.

    mixedCase is allowed only in contexts where that's already the
    prevailing style (e.g. threading.py), to retain backwards compatibility.
    """
    N802 = "function name '{name}' should be lowercase"
    N807 = "function name '{name}' should not start and end with '__'"

    def visit_functiondef(self, node, parents, ignore=None):
        function_type = getattr(node, 'function_type', _FunctionType.FUNCTION)
        name = node.name
        if _ignored(name, ignore):
            return
        if name in ('__dir__', '__getattr__'):
            return
        if name.lower() != name:
            yield self.err(node, 'N802', name=name)
        if (function_type == _FunctionType.FUNCTION
                and name[:2] == '__' and name[-2:] == '__'):
            yield self.err(node, 'N807', name=name)

    visit_asyncfunctiondef = visit_functiondef


class FunctionArgNamesCheck(BaseASTCheck):
    """
    The argument names of a function should be lowercase, with words separated
    by underscores.

    A classmethod should have 'cls' as first argument.
    A method should have 'self' as first argument.
    """
    N803 = "argument name '{name}' should be lowercase"
    N804 = "first argument of a classmethod should be named 'cls'"
    N805 = "first argument of a method should be named 'self'"

    def visit_functiondef(self, node, parents, ignore=None):

        def arg_name(arg):
            return (arg, arg.arg) if arg else (node, arg)

        for arg, name in arg_name(node.args.vararg), arg_name(node.args.kwarg):
            if name is None or _ignored(name, ignore):
                continue
            if name.lower() != name:
                yield self.err(arg, 'N803', name=name)
                return

        arg_name_tuples = get_arg_name_tuples(node)
        if not arg_name_tuples:
            return
        arg0, name0 = arg_name_tuples[0]
        function_type = getattr(node, 'function_type', _FunctionType.FUNCTION)

        if function_type == _FunctionType.METHOD:
            if name0 != 'self' and not _ignored(name0, ignore):
                yield self.err(arg0, 'N805')
        elif function_type == _FunctionType.CLASSMETHOD:
            if name0 != 'cls' and not _ignored(name0, ignore):
                yield self.err(arg0, 'N804')
        for arg, name in arg_name_tuples:
            if name.lower() != name and not _ignored(name, ignore):
                yield self.err(arg, 'N803', name=name)
                return

    visit_asyncfunctiondef = visit_functiondef


class ImportAsCheck(BaseASTCheck):
    """
    Don't change the naming convention via an import
    """
    N811 = "constant '{name}' imported as non constant '{asname}'"
    N812 = "lowercase '{name}' imported as non lowercase '{asname}'"
    N813 = "camelcase '{name}' imported as lowercase '{asname}'"
    N814 = "camelcase '{name}' imported as constant '{asname}'"
    N817 = "camelcase '{name}' imported as acronym '{asname}'"

    def visit_importfrom(self, node, parents, ignore=None):
        for name in node.names:
            asname = name.asname
            if not asname:
                continue
            original_name = name.name
            err_kwargs = {'name': original_name, 'asname': asname}
            if original_name.isupper():
                if not asname.isupper():
                    yield self.err(node, 'N811', **err_kwargs)
            elif original_name.islower():
                if asname.lower() != asname:
                    yield self.err(node, 'N812', **err_kwargs)
            elif asname.islower():
                yield self.err(node, 'N813', **err_kwargs)
            elif asname.isupper():
                if ''.join(filter(str.isupper, original_name)) == asname:
                    yield self.err(node, 'N817', **err_kwargs)
                else:
                    yield self.err(node, 'N814', **err_kwargs)

    visit_import = visit_importfrom


class VariablesCheck(BaseASTCheck):
    """
    Class attributes and local variables in functions should be lowercase
    """
    N806 = "variable '{name}' in function should be lowercase"
    N815 = "variable '{name}' in class scope should not be mixedCase"
    N816 = "variable '{name}' in global scope should not be mixedCase"

    def _find_errors(self, assignment_target, parents, ignore):
        for parent_func in reversed(parents):
            if isinstance(parent_func, ast.ClassDef):
                checker = self.class_variable_check
                break
            if isinstance(parent_func, FUNC_NODES):
                checker = partial(self.function_variable_check, parent_func)
                break
        else:
            checker = self.global_variable_check
        for name in _extract_names(assignment_target):
            if _ignored(name, ignore):
                continue
            error_code = checker(name)
            if error_code:
                yield self.err(assignment_target, error_code, name=name)

    @staticmethod
    def is_namedtupe(node_value):
        if isinstance(node_value, ast.Call):
            if isinstance(node_value.func, ast.Attribute):
                if node_value.func.attr == 'namedtuple':
                    return True
            elif isinstance(node_value.func, ast.Name):
                if node_value.func.id == 'namedtuple':
                    return True
        return False

    def visit_assign(self, node, parents, ignore=None):
        if self.is_namedtupe(node.value):
            return
        for target in node.targets:
            yield from self._find_errors(target, parents, ignore)

    def visit_namedexpr(self, node, parents, ignore):
        if self.is_namedtupe(node.value):
            return
        yield from self._find_errors(node.target, parents, ignore)

    visit_annassign = visit_namedexpr

    def visit_with(self, node, parents, ignore):
        for item in node.items:
            yield from self._find_errors(
                    item.optional_vars, parents, ignore)

    visit_asyncwith = visit_with

    def visit_for(self, node, parents, ignore):
        yield from self._find_errors(node.target, parents, ignore)

    visit_asyncfor = visit_for

    def visit_excepthandler(self, node, parents, ignore):
        if node.name:
            yield from self._find_errors(node, parents, ignore)

    def visit_generatorexp(self, node, parents, ignore):
        for gen in node.generators:
            yield from self._find_errors(gen.target, parents, ignore)

    visit_listcomp = visit_dictcomp = visit_setcomp = visit_generatorexp

    @staticmethod
    def global_variable_check(name):
        if is_mixed_case(name):
            return 'N816'

    @staticmethod
    def class_variable_check(name):
        if is_mixed_case(name):
            return 'N815'

    @staticmethod
    def function_variable_check(func, var_name):
        if var_name in func.global_names:
            return None
        if var_name.lower() == var_name:
            return None
        return 'N806'


def _extract_names(assignment_target):
    """Yield assignment_target ids."""
    target_type = type(assignment_target)
    if target_type is ast.Name:
        yield assignment_target.id
    elif target_type in (ast.Tuple, ast.List):
        for element in assignment_target.elts:
            element_type = type(element)
            if element_type is ast.Name:
                yield element.id
            elif element_type in (ast.Tuple, ast.List):
                yield from _extract_names(element)
            elif element_type is ast.Starred:  # PEP 3132
                yield from _extract_names(element.value)
    elif target_type is ast.ExceptHandler:
        yield assignment_target.name


def is_mixed_case(name):
    return name.lower() != name and name.lstrip('_')[:1].islower()
