import os.path
import unittest

import pycodestyle
from testsuite.support import init_tests
from testsuite.support import ROOT_DIR


class PycodestyleTestCase(unittest.TestCase):
    """Test the standard errors and warnings (E and W)."""

    def setUp(self):
        self._style = pycodestyle.StyleGuide(
            paths=[os.path.join(ROOT_DIR, 'testsuite')],
            select='E,W', quiet=True)

    def test_checkers_testsuite(self):
        init_tests(self._style)
        report = self._style.check_files()
        self.assertFalse(report.total_errors,
                         msg='%s failure(s)' % report.total_errors)

    def test_own_dog_food(self):
        files = [pycodestyle.__file__.rstrip('oc'), __file__.rstrip('oc'),
                 os.path.join(ROOT_DIR, 'setup.py')]
        report = self._style.init_report(pycodestyle.StandardReport)
        report = self._style.check_files(files)
        self.assertEqual(list(report.messages.keys()), ['W504'],
                         msg='Failures: %s' % report.messages)
