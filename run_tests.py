import io
import optparse
import os
import re
import sys

import pep8ext_naming


PyCF_ONLY_AST = 1024

IS_PY3 = sys.version_info[0] == 3
IS_PY3_TEST = re.compile(r"^#\s*python3\s*only")
IS_PY2_TEST = re.compile(r"^#\s*python2\s*only")

TESTCASE_RE = re.compile("^#: (?P<code>\w+)(\((?P<options>.+)\))?$")


def main():
    print('Running pep8-naming tests')
    test_count = 0
    errors = 0
    for filename in os.listdir('testsuite'):
        filepath = os.path.join('testsuite', filename)
        with io.open(filepath, encoding='utf8') as fd:
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
    if IS_PY3 and any(IS_PY2_TEST.search(line) for line in lines[:3]):
        return False

    if not IS_PY3 and any(IS_PY3_TEST.search(line) for line in lines[:3]):
        return False

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


class OptionsManager(optparse.OptionParser):
    """A Flake8-2.x-compatible OptionsManager."""
    def __init__(self, *args, **kwargs):
        optparse.OptionParser.__init__(self, *args, **kwargs)
        self.config_options = []


def parse_options(checker, options):
    """Parse the CLI-style flags from `options` and expose to `checker`"""
    options_manager = OptionsManager('flake8')
    checker.add_options(options_manager)
    processed_options, _ = options_manager.parse_args(options)
    checker.parse_options(processed_options)


def test_file(filename, lines, code, options):
    tree = compile(''.join(lines), '', 'exec', PyCF_ONLY_AST)
    checker = pep8ext_naming.NamingChecker(tree, filename)
    parse_options(checker, options)

    found_errors = []
    for lineno, col_offset, msg, instance in checker.run():
        found_errors.append(msg.split()[0])

    if code is None:  # Invalid test case
        return 0
    if not found_errors and code == 'Okay':  # Expected PASS
        return 0
    if code in found_errors:  # Expected FAIL
        return 0
    print("ERROR: %s not in %s" % (code, filename))
    return 1


if __name__ == '__main__':
    main()
