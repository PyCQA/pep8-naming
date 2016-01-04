import sys
import os
import pep8ext_naming
import re
import unittest

PyCF_ONLY_AST = 1024

IS_PY3 = sys.version_info[0] == 3
IS_PY3_TEST = re.compile("^#\s*python3\s*only")
IS_PY2_TEST = re.compile("^#\s*python2\s*only")


class TestHelperFunctions(unittest.TestCase):
    """
    Our basic test class
    """

    def test_parse_ignore_conventions(self):
        """

        """
        line1 = "test/foo:N802, test/bar: N801 N802"
        line2 = "test/foo:N802,test/bar:N801 N802"  # equal
        line3 = "test 802, test/bar: N801 - N802"  # not equal
        solution = {"test/foo": ["N802"], "test/bar": ["N801", "N802"]}

        out1 = pep8ext_naming._parse_ignore_conventions(line1)
        out2 = pep8ext_naming._parse_ignore_conventions(line2)
        out3 = pep8ext_naming._parse_ignore_conventions(line3)

        self.assertEqual(out1, solution)
        self.assertEqual(out2, solution)
        self.assertNotEqual(out3, solution)


def main():
    print('Running pep8-naming tests')
    test_count = 0
    errors = 0
    for filename in os.listdir('testsuite'):
        with open(os.path.join('testsuite', filename)) as fd:
            lines = list(fd)
            if not is_test_allowed(lines):
                continue

            for testcase, codes in load_test_files(lines):
                test_count += 1
                errors += test_file(filename, testcase, codes)

    if errors == 0:
        print("%s tests run successful" % test_count)
        # sys.exit(0)
    else:
        print("%i of %i tests failed" % (errors, test_count))
        # sys.exit(1)


def is_test_allowed(lines):
    if IS_PY3 and any(IS_PY2_TEST.search(line) for line in lines[:3]):
        return False

    if not IS_PY3 and any(IS_PY3_TEST.search(line) for line in lines[:3]):
        return False

    return True


def load_test_files(lines):
    testcase = []
    codes = []
    for line in lines:
        if line.startswith("#:"):
            if testcase:
                yield testcase, codes
                del testcase[:]
            codes = line.split()[1:]
        else:
            testcase.append(line)

    if testcase and codes:
        yield testcase, codes


def test_file(filename, lines, codes):
    tree = compile(''.join(lines), '', 'exec', PyCF_ONLY_AST)
    checker = pep8ext_naming.NamingChecker(tree, filename)
    found_errors = []
    for lineno, col_offset, msg, instance in checker.run():
        found_errors.append(msg.split()[0])

    if not found_errors and codes == ['Okay']:
        return 0

    errors = 0
    for code in codes:
        if code not in found_errors:
            errors += 1
            print("ERROR: %s not in %s" % (code, filename))

    return errors


if __name__ == '__main__':
    main()
    unittest.main()
