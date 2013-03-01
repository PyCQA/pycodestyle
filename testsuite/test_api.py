# -*- coding: utf-8 -*-
import unittest

import pep8


class APITestCase(unittest.TestCase):
    """Test the public methods."""

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

        pep8.register_check(check_dummy, [])
        pep8.register_check(check_dummy, ['Z402', 'Z403'])
        codes, args = pep8._checks['logical_line'][check_dummy]
        self.assertEqual(codes, ['Z401', 'Z402', 'Z403'])
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
