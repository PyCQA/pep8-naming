import os
import platform
import re
import sys

import flake8
from flake8.options.manager import OptionManager
import pep8ext_naming


PyCF_ONLY_AST = 1024

TESTCASE_RE = re.compile(
    r'#: '
    r'(?P<code>\w+:?\d*:?\d*)'
    r'(\((?P<options>.+)\))?'
    r'$'
)
EVAL_LOCALS = {'python_version': platform.python_version()[:3]}


def main():
    print('Running pep8-naming tests')
    test_count = 0
    errors = 0
    for filename in os.listdir('testsuite'):
        filepath = os.path.join('testsuite', filename)
        with open(filepath, encoding='utf8') as fd:
            lines = list(fd)
            if not is_test_allowed(lines):
                continue
            for testcase, code, options in load_tests(lines):
                test_count += 1
                errors += test_file(filename, testcase, code, options)

    if errors == 0:
        print("%s tests run successful" % test_count)
        sys.exit(0)
    else:
        print("%i of %i tests failed" % (errors, test_count))
        sys.exit(1)


def is_test_allowed(lines):
    for line in lines[:3]:
        if 'python_version' in line:
            return eval(line[1:], {}, EVAL_LOCALS)
    return True


def load_tests(lines):
    options = None
    testcase = []
    code = None
    for line in lines:
        line_match = TESTCASE_RE.match(line)
        if line_match:
            if testcase:
                yield testcase, code, options
                del testcase[:]
            code = line_match.group('code')
            if line_match.group('options'):
                options = [line_match.group('options')]
            else:
                options = None
        else:
            testcase.append(line)

    if testcase and code:
        yield testcase, code, options


def parse_options(checker, options):
    """Parse the CLI-style flags from `options` and expose to `checker`"""
    extra_kwargs = {}
    if flake8.__version_info__[0] >= 6:
        extra_kwargs = {
            "formatter_names": []
        }

    options_manager = OptionManager(
        version=flake8.__version__,
        plugin_versions=f"naming: {pep8ext_naming.__version__}",
        parents=[],
        **extra_kwargs,
    )
    options_manager.add_option('--select', default=[])
    options_manager.add_option('--extended-default-select', default=['N'])
    options_manager.add_option('--extend-select', default=['N'])
    options_manager.add_option('--ignore', default=[])
    options_manager.add_option('--extend-ignore', default=[])
    options_manager.add_option('--enable-extensions', default=[])
    options_manager.add_option('--extended-default-ignore', default=[])
    checker.add_options(options_manager)
    processed_options = options_manager.parse_args(options)
    checker.parse_options(processed_options)


def test_file(filename, lines, code, options):
    if code is None:  # Invalid test case
        return 0
    source = ''.join(lines)
    tree = compile(source, '', 'exec', PyCF_ONLY_AST)
    checker = pep8ext_naming.NamingChecker(tree, filename)
    parse_options(checker, options)
    error_format = (
        '{0}:{lineno}:{col_offset}' if ':' in code else '{0}').format

    found_errors = set()
    for lineno, col_offset, msg, instance in checker.run():
        found_errors.add(error_format(msg.split()[0], **locals()))

    if not found_errors and code == 'Okay':  # Expected PASS
        return 0
    if code in found_errors:  # Expected FAIL
        return 0
    print("ERROR: %s not in %s. found_errors: %s. Source:\n%s"
          % (code, filename, ','.join(sorted(found_errors)), source))
    return 1


if __name__ == '__main__':
    main()
