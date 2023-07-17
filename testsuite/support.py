from __future__ import annotations

import os.path
import re
import sys

from pycodestyle import readlines
from pycodestyle import StandardReport

SELFTEST_REGEX = re.compile(r'\b(Okay|[EW]\d{3}):\s(.*)')
ROOT_DIR = os.path.dirname(os.path.dirname(__file__))


class PseudoFile(list):
    """Simplified file interface."""
    write = list.append

    def getvalue(self):
        return ''.join(self)

    def flush(self):
        pass


class TestReport(StandardReport):
    """Collect the results for the tests."""

    def __init__(self, options):
        options.benchmark_keys += ['test cases', 'failed tests']
        super().__init__(options)
        self._verbose = options.verbose

    def error(self, line_number, offset, text, check):
        """Report an error, according to options."""
        code = text[:4]
        if code in self.counters:
            self.counters[code] += 1
        else:
            self.counters[code] = 1
        detailed_code = f'{code}:{line_number}:{offset + 1}'
        # Don't care about expected errors or warnings
        if code not in self.expected and detailed_code not in self.expected:  # pragma: no cover  # noqa: E501
            err = (line_number, offset, detailed_code, text[5:], check.__doc__)
            self._deferred_print.append(err)
            self.file_errors += 1
            self.total_errors += 1
            return code

    def get_file_results(self):
        # Check if the expected errors were found
        label = f'{self.filename}:{self.line_offset}:1'
        for extended_code in self.expected:
            code = extended_code.split(':')[0]
            if not self.counters.get(code):  # pragma: no cover
                self.file_errors += 1
                self.total_errors += 1
                print(f'{label}: error {extended_code} not found')
            else:
                self.counters[code] -= 1
        for code, extra in sorted(self.counters.items()):
            if code not in self._benchmark_keys:
                if extra and code in self.expected:  # pragma: no cover
                    self.file_errors += 1
                    self.total_errors += 1
                    print('%s: error %s found too many times (+%d)' %
                          (label, code, extra))
                # Reset counters
                del self.counters[code]
        if self._verbose and not self.file_errors:  # pragma: no cover
            print('%s: passed (%s)' %
                  (label, ' '.join(self.expected) or 'Okay'))
        self.counters['test cases'] += 1
        if self.file_errors:  # pragma: no cover
            self.counters['failed tests'] += 1
        return super().get_file_results()

    def print_results(self):
        results = ("%(physical lines)d lines tested: %(files)d files, "
                   "%(test cases)d test cases%%s." % self.counters)
        if self.total_errors:  # pragma: no cover
            print(results % ", %s failures" % self.total_errors)
        else:
            print(results % "")
        print("Test failed." if self.total_errors else "Test passed.")


def init_tests(pep8style):
    """
    Initialize testing framework.

    A test file can provide many tests.  Each test starts with a
    declaration.  This declaration is a single line starting with '#:'.
    It declares codes of expected failures, separated by spaces or
    'Okay' if no failure is expected.
    If the file does not contain such declaration, it should pass all
    tests.  If the declaration is empty, following lines are not
    checked, until next declaration.

    Examples:

     * Only E224 and W701 are expected:         #: E224 W701
     * Following example is conform:            #: Okay
     * Don't check these lines:                 #:
    """
    report = pep8style.init_report(TestReport)
    runner = pep8style.input_file

    def run_tests(filename):
        """Run all the tests from a file."""
        # Skip tests meant for higher versions of python
        ver_match = re.search(r'python(\d)(\d+)?\.py$', filename)
        if ver_match:
            test_against_version = tuple(int(val or 0)
                                         for val in ver_match.groups())
            if sys.version_info < test_against_version:  # pragma: no cover
                return
        lines = readlines(filename) + ['#:\n']
        line_offset = 0
        codes = ['Okay']
        testcase = []
        count_files = report.counters['files']
        for index, line in enumerate(lines):
            if not line.startswith('#:'):
                if codes:
                    # Collect the lines of the test case
                    testcase.append(line)
                continue
            if codes and index:
                if 'noeol' in codes:
                    testcase[-1] = testcase[-1].rstrip('\n')
                codes = [c for c in codes
                         if c not in ('Okay', 'noeol')]
                # Run the checker
                runner(filename, testcase, expected=codes,
                       line_offset=line_offset)
            # output the real line numbers
            line_offset = index + 1
            # configure the expected errors
            codes = line.split()[1:]
            # empty the test case buffer
            del testcase[:]
        report.counters['files'] = count_files + 1
        return report.counters['failed tests']

    pep8style.runner = run_tests


def run_tests(style):
    if style.options.testsuite:
        init_tests(style)
    return style.check_files()
