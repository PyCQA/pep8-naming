# -*- coding: utf-8 -*-
"""Checker of PEP-8 Naming Conventions."""
import sys
from collections import deque
from functools import partial

from flake8_polyfill import options

try:
    import ast
    from ast import iter_child_nodes
except ImportError:
    from flake8.util import ast, iter_child_nodes

__version__ = '0.8.2'

PYTHON_VERSION = sys.version_info[:3]
PY2 = PYTHON_VERSION[0] == 2

# Node types which may contain class methods
METHOD_CONTAINER_NODES = {ast.If, ast.While, ast.For, ast.With}
FUNC_NODES = (ast.FunctionDef,)

if PY2:
    METHOD_CONTAINER_NODES |= {ast.TryExcept, ast.TryFinally}
else:
    METHOD_CONTAINER_NODES |= {ast.Try}

if PYTHON_VERSION > (3, 5):
    FUNC_NODES += (ast.AsyncFunctionDef,)
    METHOD_CONTAINER_NODES |= {ast.AsyncWith, ast.AsyncFor}

if PY2:
    def _unpack_args(args):
        ret = []
        for arg in args:
            if isinstance(arg, ast.Tuple):
                ret.extend(_unpack_args(arg.elts))
            else:
                ret.append((arg, arg.id))
        return ret

    def get_arg_name_tuples(node):
        return _unpack_args(node.args.args)
else:
    def get_arg_name_tuples(node):
        args = node.args
        pos_args = [(arg, arg.arg) for arg in args.args]
        kw_only = [(arg, arg.arg) for arg in args.kwonlyargs]
        return pos_args + kw_only


class _ASTCheckMeta(type):
    def __init__(cls, class_name, bases, namespace):
        try:
            cls._checks.append(cls())
        except AttributeError:
            cls._checks = []


def _err(self, node, code, **kwargs):
    lineno, col_offset = node.lineno, node.col_offset
    if isinstance(node, ast.ClassDef):
        lineno += len(node.decorator_list)
        col_offset += 6
    elif isinstance(node, FUNC_NODES):
        lineno += len(node.decorator_list)
        col_offset += 4
    code_str = getattr(self, code)
    if kwargs:
        code_str = code_str.format(**kwargs)
    return lineno, col_offset + 1, '%s %s' % (code, code_str), self


BaseASTCheck = _ASTCheckMeta('BaseASTCheck', (object,),
                             {'__doc__': "Base for AST Checks.", 'err': _err})


class _FunctionType(object):
    CLASSMETHOD = 'classmethod'
    STATICMETHOD = 'staticmethod'
    FUNCTION = 'function'
    METHOD = 'method'


_default_ignore_names = [
        'setUp',
        'tearDown',
        'setUpClass',
        'tearDownClass',
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


class NamingChecker(object):
    """Checker of PEP-8 Naming Conventions."""
    name = 'naming'
    version = __version__
    decorator_to_type = _build_decorator_to_type(
        _default_classmethod_decorators, _default_staticmethod_decorators)
    ignore_names = frozenset(_default_ignore_names)

    def __init__(self, tree, filename):
        self.visitors = BaseASTCheck._checks
        self.parents = deque()
        self._node = tree

    @classmethod
    def add_options(cls, parser):
        options.register(parser, '--ignore-names',
                         default=_default_ignore_names,
                         action='store',
                         type='string',
                         parse_from_config=True,
                         comma_separated_list=True,
                         help='List of names the pep8-naming plugin should '
                              'ignore. (Defaults to %default)')

        options.register(parser, '--classmethod-decorators',
                         default=_default_classmethod_decorators,
                         action='store',
                         type='string',
                         parse_from_config=True,
                         comma_separated_list=True,
                         help='List of method decorators pep8-naming plugin '
                              'should consider classmethods (Defaults to '
                              '%default)')

        options.register(parser, '--staticmethod-decorators',
                         default=_default_staticmethod_decorators,
                         action='store',
                         type='string',
                         parse_from_config=True,
                         comma_separated_list=True,
                         help='List of method decorators pep8-naming plugin '
                              'should consider staticmethods (Defaults to '
                              '%default)')

    @classmethod
    def parse_options(cls, options):
        cls.ignore_names = frozenset(options.ignore_names)
        cls.decorator_to_type = _build_decorator_to_type(
            options.classmethod_decorators,
            options.staticmethod_decorators)

    def run(self):
        return self.visit_tree(self._node) if self._node else ()

    def visit_tree(self, node):
        for error in self.visit_node(node):
            yield error
        self.parents.append(node)
        for child in iter_child_nodes(node):
            for error in self.visit_tree(child):
                yield error
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
            for error in visitor_method(node, parents, ignore_names):
                yield error

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

        cls_bases = [b for b in cls_node.bases if isinstance(b, ast.Name)]
        # If this class inherits from `type`, it's a metaclass, and we'll
        # consider all of it's methods to be classmethods.
        ismetaclass = any(name for name in cls_bases if name.id == 'type')
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
            if node.name in ('__new__', '__init_subclass__') or ismetaclass:
                node.function_type = _FunctionType.CLASSMETHOD
            if node.name in late_decoration:
                node.function_type = late_decoration[node.name]
            elif node.decorator_list:
                names = [self.decorator_to_type[d.id]
                         for d in node.decorator_list
                         if isinstance(d, ast.Name) and
                         d.id in self.decorator_to_type]
                if names:
                    node.function_type = names[0]

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

    def visit_classdef(self, node, parents, ignore=None):
        name = node.name
        if ignore and name in ignore:
            return
        name = name.strip('_')
        if not name[:1].isupper() or '_' in name:
            yield self.err(node, 'N801', name=name)


class FunctionNameCheck(BaseASTCheck):
    """
    Function names should be lowercase, with words separated by underscores
    as necessary to improve readability.

    Functions *not* being methods '__' in front and back are not allowed.

    mixedCase is allowed only in contexts where that's already the
    prevailing style (e.g. threading.py), to retain backwards compatibility.
    """
    N802 = "function name '{name}' should be lowercase"
    N807 = "function name '{name}' should not start or end with '__'"

    def visit_functiondef(self, node, parents, ignore=None):
        function_type = getattr(node, 'function_type', _FunctionType.FUNCTION)
        name = node.name
        if ignore and name in ignore:
            return
        if name in ('__dir__', '__getattr__'):
            return
        if name.lower() != name:
            yield self.err(node, 'N802', name=name)
        if (function_type == _FunctionType.FUNCTION
                and '__' in (name[:2], name[-2:])):
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
            try:
                return arg, arg.arg
            except AttributeError:  # PY2
                return node, arg

        for arg, name in arg_name(node.args.vararg), arg_name(node.args.kwarg):
            if name is not None and name.lower() != name:
                yield self.err(arg, 'N803', name=name)
                return

        arg_name_tuples = get_arg_name_tuples(node)
        if not arg_name_tuples:
            return
        arg0, name0 = arg_name_tuples[0]
        function_type = getattr(node, 'function_type', _FunctionType.FUNCTION)

        if function_type == _FunctionType.METHOD:
            if name0 != 'self':
                yield self.err(arg0, 'N805')
        elif function_type == _FunctionType.CLASSMETHOD:
            if name0 != 'cls':
                yield self.err(arg0, 'N804')
        for arg, name in arg_name_tuples:
            if name.lower() != name:
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
            if name in ignore:
                continue
            error_code = checker(name)
            if error_code:
                yield self.err(assignment_target, error_code, name=name)

    def visit_assign(self, node, parents, ignore=None):
        if isinstance(node.value, ast.Call):
            if isinstance(node.value.func, ast.Attribute):
                if node.value.func.attr == 'namedtuple':
                    return
            elif isinstance(node.value.func, ast.Name):
                if node.value.func.id == 'namedtuple':
                    return
        for target in node.targets:
            for error in self._find_errors(target, parents, ignore):
                yield error

    def visit_with(self, node, parents, ignore):
        if PY2:
            for error in self._find_errors(
                    node.optional_vars, parents, ignore):
                yield error
            return
        for item in node.items:
            for error in self._find_errors(
                    item.optional_vars, parents, ignore):
                yield error

    visit_asyncwith = visit_with

    def visit_for(self, node, parents, ignore):
        for error in self._find_errors(node.target, parents, ignore):
            yield error

    visit_asyncfor = visit_for

    def visit_excepthandler(self, node, parents, ignore):
        if node.name:
            for error in self._find_errors(node, parents, ignore):
                yield error

    def visit_generatorexp(self, node, parents, ignore):
        for gen in node.generators:
            for error in self._find_errors(gen.target, parents, ignore):
                yield error

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
                for n in _extract_names(element):
                    yield n
            elif not PY2 and element_type is ast.Starred:  # PEP 3132
                for n in _extract_names(element.value):
                    yield n
    elif target_type is ast.ExceptHandler:
        if PY2:
            # Python 2 supports unpacking tuple exception values.
            if isinstance(assignment_target.name, ast.Tuple):
                for name in assignment_target.name.elts:
                    yield name.id
            else:
                yield assignment_target.name.id
        else:
            yield assignment_target.name


def is_mixed_case(name):
    return name.lower() != name and name.lstrip('_')[:1].islower()
