# -*- coding: utf-8 -*-
import os.path
import shlex
import sys
import unittest

import pep8
from testsuite.support import ROOT_DIR, PseudoFile

E11 = os.path.join(ROOT_DIR, 'testsuite', 'E11.py')


class DummyChecker(object):
    def __init__(self, tree, filename):
        pass

    def run(self):
        if False:
            yield


class APITestCase(unittest.TestCase):
    """Test the public methods."""

    def setUp(self):
        self._saved_stdout = sys.stdout
        self._saved_stderr = sys.stderr
        self._saved_checks = pep8._checks
        sys.stdout = PseudoFile()
        sys.stderr = PseudoFile()
        pep8._checks = dict((k, dict((f, (vals[0][:], vals[1]))
                                     for (f, vals) in v.items()))
                            for (k, v) in self._saved_checks.items())

    def tearDown(self):
        sys.stdout = self._saved_stdout
        sys.stderr = self._saved_stderr
        pep8._checks = self._saved_checks

    def reset(self):
        del sys.stdout[:], sys.stderr[:]

    def test_register_physical_check(self):
        def check_dummy(physical_line, line_number):
            if False:
                yield
        pep8.register_check(check_dummy, ['Z001'])

        self.assertTrue(check_dummy in pep8._checks['physical_line'])
        codes, args = pep8._checks['physical_line'][check_dummy]
        self.assertTrue('Z001' in codes)
        self.assertEqual(args, ['physical_line', 'line_number'])

        options = pep8.StyleGuide().options
        self.assertTrue(any(func == check_dummy
                            for name, func, args in options.physical_checks))

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

        options = pep8.StyleGuide().options
        self.assertTrue(any(func == check_dummy
                            for name, func, args in options.logical_checks))

    def test_register_ast_check(self):
        pep8.register_check(DummyChecker, ['Z701'])

        self.assertTrue(DummyChecker in pep8._checks['tree'])
        codes, args = pep8._checks['tree'][DummyChecker]
        self.assertTrue('Z701' in codes)
        self.assertTrue(args is None)

        options = pep8.StyleGuide().options
        self.assertTrue(any(cls == DummyChecker
                            for name, cls, args in options.ast_checks))

    def test_register_invalid_check(self):
        class InvalidChecker(DummyChecker):
            def __init__(self, filename):
                pass

        def check_dummy(logical, tokens):
            if False:
                yield
        pep8.register_check(InvalidChecker, ['Z741'])
        pep8.register_check(check_dummy, ['Z441'])

        for checkers in pep8._checks.values():
            self.assertTrue(DummyChecker not in checkers)
            self.assertTrue(check_dummy not in checkers)

        self.assertRaises(TypeError, pep8.register_check)

    def test_styleguide(self):
        report = pep8.StyleGuide().check_files()
        self.assertEqual(report.total_errors, 0)
        self.assertFalse(sys.stdout)
        self.assertFalse(sys.stderr)
        self.reset()

        report = pep8.StyleGuide().check_files(['missing-file'])
        stdout = sys.stdout.getvalue().splitlines()
        self.assertEqual(len(stdout), report.total_errors)
        self.assertEqual(report.total_errors, 1)
        # < 3.3 returns IOError; >= 3.3 returns FileNotFoundError
        self.assertTrue(stdout[0].startswith("missing-file:1:1: E902 "))
        self.assertFalse(sys.stderr)
        self.reset()

        report = pep8.StyleGuide().check_files([E11])
        stdout = sys.stdout.getvalue().splitlines()
        self.assertEqual(len(stdout), report.total_errors)
        self.assertEqual(report.total_errors, 6)
        self.assertFalse(sys.stderr)
        self.reset()

        # Passing the paths in the constructor gives same result
        report = pep8.StyleGuide(paths=[E11]).check_files()
        stdout = sys.stdout.getvalue().splitlines()
        self.assertEqual(len(stdout), report.total_errors)
        self.assertEqual(report.total_errors, 6)
        self.assertFalse(sys.stderr)
        self.reset()

    def test_styleguide_options(self):
        # Instanciate a simple checker
        pep8style = pep8.StyleGuide(paths=[E11])

        # Check style's attributes
        self.assertEqual(pep8style.checker_class, pep8.Checker)
        self.assertEqual(pep8style.paths, [E11])
        self.assertEqual(pep8style.runner, pep8style.input_file)
        self.assertEqual(pep8style.options.ignore_code, pep8style.ignore_code)
        self.assertEqual(pep8style.options.paths, pep8style.paths)

        # Check unset options
        for o in ('benchmark', 'config', 'count', 'diff',
                  'doctest', 'quiet', 'show_pep8', 'show_source',
                  'statistics', 'testsuite', 'verbose'):
            oval = getattr(pep8style.options, o)
            self.assertTrue(oval in (None, False), msg='%s = %r' % (o, oval))

        # Check default options
        self.assertTrue(pep8style.options.repeat)
        self.assertEqual(pep8style.options.benchmark_keys,
                         ['directories', 'files',
                          'logical lines', 'physical lines'])
        self.assertEqual(pep8style.options.exclude,
                         ['.svn', 'CVS', '.bzr', '.hg', '.git', '__pycache__'])
        self.assertEqual(pep8style.options.filename, ['*.py'])
        self.assertEqual(pep8style.options.format, 'default')
        self.assertEqual(pep8style.options.select, ())
        self.assertEqual(pep8style.options.ignore, ('E226', 'E24'))
        self.assertEqual(pep8style.options.max_line_length, 79)

    def test_styleguide_ignore_code(self):
        def parse_argv(argstring):
            _saved_argv = sys.argv
            sys.argv = shlex.split('pep8 %s /dev/null' % argstring)
            try:
                return pep8.StyleGuide(parse_argv=True)
            finally:
                sys.argv = _saved_argv

        options = parse_argv('').options
        self.assertEqual(options.select, ())
        self.assertEqual(options.ignore, ('E123', 'E226', 'E24'))

        options = parse_argv('--doctest').options
        self.assertEqual(options.select, ())
        self.assertEqual(options.ignore, ())

        options = parse_argv('--ignore E,W').options
        self.assertEqual(options.select, ())
        self.assertEqual(options.ignore, ('E', 'W'))

        options = parse_argv('--select E,W').options
        self.assertEqual(options.select, ('E', 'W'))
        self.assertEqual(options.ignore, ('',))

        options = parse_argv('--select E --ignore E24').options
        self.assertEqual(options.select, ('E',))
        self.assertEqual(options.ignore, ('',))

        options = parse_argv('--ignore E --select E24').options
        self.assertEqual(options.select, ('E24',))
        self.assertEqual(options.ignore, ('',))

        options = parse_argv('--ignore W --select E24').options
        self.assertEqual(options.select, ('E24',))
        self.assertEqual(options.ignore, ('',))

        pep8style = pep8.StyleGuide(paths=[E11])
        self.assertFalse(pep8style.ignore_code('E112'))
        self.assertFalse(pep8style.ignore_code('W191'))
        self.assertTrue(pep8style.ignore_code('E241'))

        pep8style = pep8.StyleGuide(select='E', paths=[E11])
        self.assertFalse(pep8style.ignore_code('E112'))
        self.assertTrue(pep8style.ignore_code('W191'))
        self.assertFalse(pep8style.ignore_code('E241'))

        pep8style = pep8.StyleGuide(select='W', paths=[E11])
        self.assertTrue(pep8style.ignore_code('E112'))
        self.assertFalse(pep8style.ignore_code('W191'))
        self.assertTrue(pep8style.ignore_code('E241'))

        pep8style = pep8.StyleGuide(select=('F401',), paths=[E11])
        self.assertEqual(pep8style.options.select, ('F401',))
        self.assertEqual(pep8style.options.ignore, ('',))
        self.assertFalse(pep8style.ignore_code('F'))
        self.assertFalse(pep8style.ignore_code('F401'))
        self.assertTrue(pep8style.ignore_code('F402'))

    def test_styleguide_excluded(self):
        pep8style = pep8.StyleGuide(paths=[E11])

        self.assertFalse(pep8style.excluded('./foo/bar'))
        self.assertFalse(pep8style.excluded('./foo/bar/main.py'))

        self.assertTrue(pep8style.excluded('./CVS'))
        self.assertTrue(pep8style.excluded('./subdir/CVS'))
        self.assertTrue(pep8style.excluded('__pycache__'))
        self.assertTrue(pep8style.excluded('./__pycache__'))
        self.assertTrue(pep8style.excluded('subdir/__pycache__'))

        self.assertFalse(pep8style.excluded('draftCVS'))
        self.assertFalse(pep8style.excluded('./CVSoup'))
        self.assertFalse(pep8style.excluded('./CVS/subdir'))

    def test_styleguide_checks(self):
        pep8style = pep8.StyleGuide(paths=[E11])

        # Default lists of checkers
        self.assertTrue(len(pep8style.options.physical_checks) > 4)
        self.assertTrue(len(pep8style.options.logical_checks) > 10)
        self.assertEqual(len(pep8style.options.ast_checks), 0)

        # Sanity check
        for name, check, args in pep8style.options.physical_checks:
            self.assertEqual(check.__name__, name)
            self.assertEqual(args[0], 'physical_line')
        for name, check, args in pep8style.options.logical_checks:
            self.assertEqual(check.__name__, name)
            self.assertEqual(args[0], 'logical_line')

        # Do run E11 checks
        options = pep8.StyleGuide().options
        self.assertTrue(any(func == pep8.indentation
                            for name, func, args in options.logical_checks))
        options = pep8.StyleGuide(select=['E']).options
        self.assertTrue(any(func == pep8.indentation
                            for name, func, args in options.logical_checks))
        options = pep8.StyleGuide(ignore=['W']).options
        self.assertTrue(any(func == pep8.indentation
                            for name, func, args in options.logical_checks))
        options = pep8.StyleGuide(ignore=['E12']).options
        self.assertTrue(any(func == pep8.indentation
                            for name, func, args in options.logical_checks))

        # Do not run E11 checks
        options = pep8.StyleGuide(select=['W']).options
        self.assertFalse(any(func == pep8.indentation
                             for name, func, args in options.logical_checks))
        options = pep8.StyleGuide(ignore=['E']).options
        self.assertFalse(any(func == pep8.indentation
                             for name, func, args in options.logical_checks))
        options = pep8.StyleGuide(ignore=['E11']).options
        self.assertFalse(any(func == pep8.indentation
                             for name, func, args in options.logical_checks))

    def test_styleguide_init_report(self):
        pep8style = pep8.StyleGuide(paths=[E11])

        self.assertEqual(pep8style.options.reporter, pep8.StandardReport)
        self.assertEqual(type(pep8style.options.report), pep8.StandardReport)

        class MinorityReport(pep8.BaseReport):
            pass

        report = pep8style.init_report(MinorityReport)
        self.assertEqual(pep8style.options.report, report)
        self.assertEqual(type(report), MinorityReport)

        pep8style = pep8.StyleGuide(paths=[E11], reporter=MinorityReport)
        self.assertEqual(type(pep8style.options.report), MinorityReport)
        self.assertEqual(pep8style.options.reporter, MinorityReport)

    def test_styleguide_check_files(self):
        pep8style = pep8.StyleGuide(paths=[E11])

        report = pep8style.check_files()
        self.assertTrue(report.total_errors)

        self.assertRaises(TypeError, pep8style.check_files, 42)
        # < 3.3 raises TypeError; >= 3.3 raises AttributeError
        self.assertRaises(Exception, pep8style.check_files, [42])

    def test_check_unicode(self):
        # Do not crash if lines are Unicode (Python 2.x)
        pep8.register_check(DummyChecker, ['Z701'])
        source = '#\n'
        if hasattr(source, 'decode'):
            source = source.decode('ascii')

        pep8style = pep8.StyleGuide()
        count_errors = pep8style.input_file('stdin', lines=[source])

        self.assertFalse(sys.stdout)
        self.assertFalse(sys.stderr)
        self.assertEqual(count_errors, 0)

    def test_check_nullbytes(self):
        pep8.register_check(DummyChecker, ['Z701'])

        pep8style = pep8.StyleGuide()
        count_errors = pep8style.input_file('stdin', lines=['\x00\n'])

        stdout = sys.stdout.getvalue()
        if 'SyntaxError' in stdout:
            # PyPy 2.2 returns a SyntaxError
            expected = "stdin:1:2: E901 SyntaxError"
        else:
            expected = "stdin:1:1: E901 TypeError"
        self.assertTrue(stdout.startswith(expected),
                        msg='Output %r does not start with %r' %
                        (stdout, expected))
        self.assertFalse(sys.stderr)
        self.assertEqual(count_errors, 1)

        # TODO: runner
        # TODO: input_file
