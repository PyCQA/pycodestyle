#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os.path
import sys
import unittest

import pep8
from testsuite.support import init_tests, selftest, ROOT_DIR

# Note: please only use a subset of unittest methods which were present
# in Python 2.5: assert(True|False|Equal|NotEqual|Raises)


class Pep8TestCase(unittest.TestCase):
    """Test the standard errors and warnings (E and W)."""

    def setUp(self):
        self._style = pep8.StyleGuide(
            paths=[os.path.join(ROOT_DIR, 'testsuite')],
            select='E,W', quiet=True)

    def test_doctest(self):
        import doctest
        fail_d, done_d = doctest.testmod(pep8, verbose=False, report=False)
        self.assertTrue(done_d, msg='tests not found')
        self.assertFalse(fail_d, msg='%s failure(s)' % fail_d)

    def test_selftest(self):
        fail_s, done_s = selftest(self._style.options)
        self.assertTrue(done_s, msg='tests not found')
        self.assertFalse(fail_s, msg='%s failure(s)' % fail_s)

    def test_checkers_testsuite(self):
        init_tests(self._style)
        report = self._style.check_files()
        self.assertFalse(report.total_errors,
                         msg='%s failure(s)' % report.total_errors)

    def test_own_dog_food(self):
        files = [pep8.__file__.rstrip('oc'), __file__.rstrip('oc'),
                 os.path.join(ROOT_DIR, 'setup.py')]
        report = self._style.init_report(pep8.StandardReport)
        report = self._style.check_files(files)
        self.assertFalse(report.total_errors,
                         msg='Failures: %s' % report.messages)


def suite():
    from testsuite import test_api, test_shell, test_util

    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(Pep8TestCase))
    suite.addTest(unittest.makeSuite(test_api.APITestCase))
    suite.addTest(unittest.makeSuite(test_shell.ShellTestCase))
    suite.addTest(unittest.makeSuite(test_util.UtilTestCase))
    return suite


def _main():
    return unittest.TextTestRunner(verbosity=2).run(suite())

if __name__ == '__main__':
    sys.exit(not _main())
