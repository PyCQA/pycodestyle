#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os.path
import sys
import unittest

import pep8
from testsuite.support import init_tests, selftest

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))


class Pep8TestCase(unittest.TestCase):

    def setUp(self):
        self._style = pep8.StyleGuide(
            paths=[os.path.dirname(__file__)],
            ignore=None, quiet=True)

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


class APITestCase(unittest.TestCase):

    def setUp(self):
        self._saved_checks = pep8._checks
        pep8._checks = dict((k, dict((f, (vals[0][:], vals[1]))
                                     for (f, vals) in v.items()))
                            for (k, v) in self._saved_checks.items())

    def tearDown(self):
        pep8._checks = self._saved_checks

    def test_register_physical_check(self):
        def check_dummy(physical_line, line_number):
            if False:
                yield
        pep8.register_check(check_dummy, ['Z001'])

        self.assertTrue(check_dummy in pep8._checks['physical_line'])
        codes, args = pep8._checks['physical_line'][check_dummy]
        self.assertTrue('Z001' in codes)
        self.assertEqual(args, ['physical_line', 'line_number'])

    def test_register_logical_check(self):
        def check_dummy(logical_line, tokens):
            if False:
                yield
        pep8.register_check(check_dummy, ['Z401'])

        self.assertTrue(check_dummy in pep8._checks['logical_line'])
        codes, args = pep8._checks['logical_line'][check_dummy]
        self.assertTrue('Z401' in codes)
        self.assertEqual(args, ['logical_line', 'tokens'])

    def test_register_ast_check(self):
        class DummyChecker(object):
            def __init__(self, tree, filename):
                pass

            def run(self):
                if False:
                    yield
        pep8.register_check(DummyChecker, ['Z701'])

        self.assertTrue(DummyChecker in pep8._checks['tree'])
        codes, args = pep8._checks['tree'][DummyChecker]
        self.assertTrue('Z701' in codes)
        self.assertTrue(args is None)

    def test_register_invalid_check(self):
        class DummyChecker(object):
            def __init__(self, filename):
                pass

            def run(self):
                if False:
                    yield
        pep8.register_check(DummyChecker, ['Z741'])

        def check_dummy(logical, tokens):
            if False:
                yield
        pep8.register_check(check_dummy, ['Z441'])

        for checkers in pep8._checks.values():
            self.assertTrue(DummyChecker not in checkers)
            self.assertTrue(check_dummy not in checkers)

        self.assertRaises(TypeError, pep8.register_check)


def _main():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(Pep8TestCase))
    suite.addTest(unittest.makeSuite(APITestCase))
    runner = unittest.TextTestRunner(verbosity=2)
    return runner.run(suite)

if __name__ == '__main__':
    sys.exit(not _main())
