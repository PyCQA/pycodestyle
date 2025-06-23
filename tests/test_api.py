import io
import os.path
import shlex
import sys
import unittest

import pycodestyle
from testing.support import ROOT

E11 = os.path.join(ROOT, 'testing', 'data', 'E11.py')


class DummyChecker:
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
        self._saved_checks = pycodestyle._checks
        sys.stdout = io.StringIO()
        sys.stderr = io.StringIO()
        pycodestyle._checks = {
            k: {f: (vals[0][:], vals[1]) for (f, vals) in v.items()}
            for k, v in self._saved_checks.items()
        }

    def tearDown(self):
        sys.stdout = self._saved_stdout
        sys.stderr = self._saved_stderr
        pycodestyle._checks = self._saved_checks

    def reset(self):
        sys.stdout.seek(0)
        sys.stdout.truncate()
        sys.stderr.seek(0)
        sys.stderr.truncate()

    def test_register_physical_check(self):
        def check_dummy(physical_line, line_number):
            raise NotImplementedError
        pycodestyle.register_check(check_dummy, ['Z001'])

        self.assertTrue(check_dummy in pycodestyle._checks['physical_line'])
        codes, args = pycodestyle._checks['physical_line'][check_dummy]
        self.assertTrue('Z001' in codes)
        self.assertEqual(args, ['physical_line', 'line_number'])

        options = pycodestyle.StyleGuide().options
        functions = [func for _, func, _ in options.physical_checks]
        self.assertIn(check_dummy, functions)

    def test_register_logical_check(self):
        def check_dummy(logical_line, tokens):
            raise NotImplementedError
        pycodestyle.register_check(check_dummy, ['Z401'])

        self.assertTrue(check_dummy in pycodestyle._checks['logical_line'])
        codes, args = pycodestyle._checks['logical_line'][check_dummy]
        self.assertTrue('Z401' in codes)
        self.assertEqual(args, ['logical_line', 'tokens'])

        pycodestyle.register_check(check_dummy, [])
        pycodestyle.register_check(check_dummy, ['Z402', 'Z403'])
        codes, args = pycodestyle._checks['logical_line'][check_dummy]
        self.assertEqual(codes, ['Z401', 'Z402', 'Z403'])
        self.assertEqual(args, ['logical_line', 'tokens'])

        options = pycodestyle.StyleGuide().options
        functions = [func for _, func, _ in options.logical_checks]
        self.assertIn(check_dummy, functions)

    def test_register_ast_check(self):
        pycodestyle.register_check(DummyChecker, ['Z701'])

        self.assertTrue(DummyChecker in pycodestyle._checks['tree'])
        codes, args = pycodestyle._checks['tree'][DummyChecker]
        self.assertTrue('Z701' in codes)
        self.assertTrue(args is None)

        options = pycodestyle.StyleGuide().options
        classes = [cls for _, cls, _ in options.ast_checks]
        self.assertIn(DummyChecker, classes)

    def test_register_invalid_check(self):
        class InvalidChecker(DummyChecker):
            def __init__(self, filename):
                raise NotImplementedError

        def check_dummy(logical, tokens):
            raise NotImplementedError

        pycodestyle.register_check(InvalidChecker, ['Z741'])
        pycodestyle.register_check(check_dummy, ['Z441'])

        for checkers in pycodestyle._checks.values():
            self.assertTrue(DummyChecker not in checkers)
            self.assertTrue(check_dummy not in checkers)

        self.assertRaises(TypeError, pycodestyle.register_check)

    def test_styleguide(self):
        report = pycodestyle.StyleGuide().check_files()
        self.assertEqual(report.total_errors, 0)
        self.assertFalse(sys.stdout.getvalue())
        self.assertFalse(sys.stderr.getvalue())
        self.reset()

        report = pycodestyle.StyleGuide().check_files(['missing-file'])
        stdout = sys.stdout.getvalue().splitlines()
        self.assertEqual(len(stdout), report.total_errors)
        self.assertEqual(report.total_errors, 1)
        # < 3.3 returns IOError; >= 3.3 returns FileNotFoundError
        assert stdout[0].startswith("missing-file:1:1: E902 ")
        self.assertFalse(sys.stderr.getvalue())
        self.reset()

        report = pycodestyle.StyleGuide().check_files([E11])
        stdout = sys.stdout.getvalue().splitlines()
        self.assertEqual(len(stdout), report.total_errors)
        self.assertEqual(report.total_errors, 24)
        self.assertFalse(sys.stderr.getvalue())
        self.reset()

        # Passing the paths in the constructor gives same result
        report = pycodestyle.StyleGuide(paths=[E11]).check_files()
        stdout = sys.stdout.getvalue().splitlines()
        self.assertEqual(len(stdout), report.total_errors)
        self.assertEqual(report.total_errors, 24)
        self.assertFalse(sys.stderr.getvalue())
        self.reset()

    def test_styleguide_options(self):
        # Instantiate a simple checker
        pep8style = pycodestyle.StyleGuide(paths=[E11])

        # Check style's attributes
        self.assertEqual(pep8style.checker_class, pycodestyle.Checker)
        self.assertEqual(pep8style.paths, [E11])
        self.assertEqual(pep8style.runner, pep8style.input_file)
        self.assertEqual(pep8style.options.ignore_code, pep8style.ignore_code)
        self.assertEqual(pep8style.options.paths, pep8style.paths)

        # Check unset options
        for o in ('benchmark', 'config', 'count', 'diff',
                  'quiet', 'show_pep8', 'show_source',
                  'statistics', 'verbose'):
            oval = getattr(pep8style.options, o)
            self.assertTrue(oval in (None, False), msg=f'{o} = {oval!r}')

        # Check default options
        self.assertTrue(pep8style.options.repeat)
        self.assertEqual(pep8style.options.benchmark_keys,
                         ['directories', 'files',
                          'logical lines', 'physical lines'])
        self.assertEqual(pep8style.options.exclude,
                         ['.svn', 'CVS', '.bzr', '.hg',
                          '.git', '__pycache__', '.tox'])
        self.assertEqual(pep8style.options.filename, ['*.py'])
        self.assertEqual(pep8style.options.format, 'default')
        self.assertEqual(pep8style.options.select, ())
        self.assertEqual(pep8style.options.ignore, ('E226', 'E24', 'W504'))
        self.assertEqual(pep8style.options.max_line_length, 79)

    def test_styleguide_ignore_code(self):
        def parse_argv(argstring):
            _saved_argv = sys.argv
            sys.argv = shlex.split('pycodestyle %s /dev/null' % argstring)
            try:
                return pycodestyle.StyleGuide(parse_argv=True)
            finally:
                sys.argv = _saved_argv

        options = parse_argv('').options
        self.assertEqual(options.select, ())
        self.assertEqual(
            options.ignore,
            ('E121', 'E123', 'E126', 'E226', 'E24', 'E704', 'W503', 'W504')
        )

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

        options = parse_argv('--max-doc-length=72').options
        self.assertEqual(options.max_doc_length, 72)

        options = parse_argv('').options
        self.assertEqual(options.max_doc_length, None)

        pep8style = pycodestyle.StyleGuide(paths=[E11])
        self.assertFalse(pep8style.ignore_code('E112'))
        self.assertFalse(pep8style.ignore_code('W191'))
        self.assertTrue(pep8style.ignore_code('E241'))

        pep8style = pycodestyle.StyleGuide(select='E', paths=[E11])
        self.assertFalse(pep8style.ignore_code('E112'))
        self.assertTrue(pep8style.ignore_code('W191'))
        self.assertFalse(pep8style.ignore_code('E241'))

        pep8style = pycodestyle.StyleGuide(select='W', paths=[E11])
        self.assertTrue(pep8style.ignore_code('E112'))
        self.assertFalse(pep8style.ignore_code('W191'))
        self.assertTrue(pep8style.ignore_code('E241'))

        pep8style = pycodestyle.StyleGuide(select=('F401',), paths=[E11])
        self.assertEqual(pep8style.options.select, ('F401',))
        self.assertEqual(pep8style.options.ignore, ('',))
        self.assertFalse(pep8style.ignore_code('F'))
        self.assertFalse(pep8style.ignore_code('F401'))
        self.assertTrue(pep8style.ignore_code('F402'))

    def test_styleguide_excluded(self):
        pep8style = pycodestyle.StyleGuide(paths=[E11])

        self.assertFalse(pep8style.excluded('./foo/bar'))
        self.assertFalse(pep8style.excluded('./foo/bar/main.py'))

        self.assertTrue(pep8style.excluded('./CVS'))
        self.assertTrue(pep8style.excluded('./.tox'))
        self.assertTrue(pep8style.excluded('./subdir/CVS'))
        self.assertTrue(pep8style.excluded('__pycache__'))
        self.assertTrue(pep8style.excluded('./__pycache__'))
        self.assertTrue(pep8style.excluded('subdir/__pycache__'))

        self.assertFalse(pep8style.excluded('draftCVS'))
        self.assertFalse(pep8style.excluded('./CVSoup'))
        self.assertFalse(pep8style.excluded('./CVS/subdir'))

    def test_styleguide_checks(self):
        pep8style = pycodestyle.StyleGuide(paths=[E11])

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
        options = pycodestyle.StyleGuide().options
        functions = [func for _, func, _ in options.logical_checks]
        self.assertIn(pycodestyle.indentation, functions)
        options = pycodestyle.StyleGuide(select=['E']).options
        functions = [func for _, func, _ in options.logical_checks]
        self.assertIn(pycodestyle.indentation, functions)
        options = pycodestyle.StyleGuide(ignore=['W']).options
        functions = [func for _, func, _ in options.logical_checks]
        self.assertIn(pycodestyle.indentation, functions)
        options = pycodestyle.StyleGuide(ignore=['E12']).options
        functions = [func for _, func, _ in options.logical_checks]
        self.assertIn(pycodestyle.indentation, functions)

        # Do not run E11 checks
        options = pycodestyle.StyleGuide(select=['W']).options
        functions = [func for _, func, _ in options.logical_checks]
        self.assertNotIn(pycodestyle.indentation, functions)
        options = pycodestyle.StyleGuide(ignore=['E']).options
        functions = [func for _, func, _ in options.logical_checks]
        self.assertNotIn(pycodestyle.indentation, functions)
        options = pycodestyle.StyleGuide(ignore=['E11']).options
        functions = [func for _, func, _ in options.logical_checks]
        self.assertNotIn(pycodestyle.indentation, functions)

    def test_styleguide_init_report(self):
        style = pycodestyle.StyleGuide(paths=[E11])

        standard_report = pycodestyle.StandardReport

        self.assertEqual(style.options.reporter, standard_report)
        self.assertEqual(type(style.options.report), standard_report)

        class MinorityReport(pycodestyle.BaseReport):
            pass

        report = style.init_report(MinorityReport)
        self.assertEqual(style.options.report, report)
        self.assertEqual(type(report), MinorityReport)

        style = pycodestyle.StyleGuide(paths=[E11], reporter=MinorityReport)
        self.assertEqual(type(style.options.report), MinorityReport)
        self.assertEqual(style.options.reporter, MinorityReport)

    def test_styleguide_check_files(self):
        pep8style = pycodestyle.StyleGuide(paths=[E11])

        report = pep8style.check_files()
        self.assertTrue(report.total_errors)

        self.assertRaises(TypeError, pep8style.check_files, 42)
        # < 3.3 raises TypeError; >= 3.3 raises AttributeError
        self.assertRaises(Exception, pep8style.check_files, [42])

    def test_check_nullbytes(self):
        pycodestyle.register_check(DummyChecker, ['Z701'])

        pep8style = pycodestyle.StyleGuide()
        count_errors = pep8style.input_file('stdin', lines=['\x00\n'])

        stdout = sys.stdout.getvalue()
        if sys.version_info < (3, 11, 4):  # pragma: <3.11 cover
            expected = ["stdin:1:1: E901 ValueError: source code string cannot contain null bytes"]  # noqa: E501
        elif sys.version_info < (3, 12):  # pragma: <3.12 cover  # pragma: >=3.11 cover  # noqa: E501
            expected = ["stdin:1:1: E901 SyntaxError: source code string cannot contain null bytes"]  # noqa: E501
        else:  # pragma: >=3.12 cover
            expected = [
                "stdin:1:1: E901 SyntaxError: source code string cannot contain null bytes",   # noqa: E501
                "stdin:1:1: E901 TokenError: source code cannot contain null bytes",   # noqa: E501
            ]
        self.assertEqual(stdout.splitlines(), expected)
        self.assertFalse(sys.stderr.getvalue())
        self.assertEqual(count_errors, len(expected))

    def test_styleguide_unmatched_triple_quotes(self):
        pycodestyle.register_check(DummyChecker, ['Z701'])
        lines = [
            'def foo():\n',
            '    """test docstring""\'\n',
        ]

        pep8style = pycodestyle.StyleGuide()
        pep8style.input_file('stdin', lines=lines)
        stdout = sys.stdout.getvalue()

        if sys.version_info < (3, 10):  # pragma: <3.10 cover
            expected = [
                'stdin:2:5: E901 TokenError: EOF in multi-line string',
                'stdin:2:26: E901 SyntaxError: EOF while scanning triple-quoted string literal',  # noqa: E501
            ]
        elif sys.version_info < (3, 12):  # pragma: >=3.10 cover  # pragma: <3.12 cover  # noqa: E501
            expected = [
                'stdin:2:5: E901 TokenError: EOF in multi-line string',
                'stdin:2:6: E901 SyntaxError: unterminated triple-quoted string literal (detected at line 2)',  # noqa: E501
            ]
        else:  # pragma: >=3.12 cover
            expected = [
                'stdin:2:6: E901 SyntaxError: unterminated triple-quoted string literal (detected at line 2)',  # noqa: E501
                'stdin:2:6: E901 TokenError: EOF in multi-line string',
            ]
        self.assertEqual(stdout.splitlines(), expected)

    def test_styleguides_other_indent_size(self):
        pycodestyle.register_check(DummyChecker, ['Z701'])
        lines = [
            'def foo():\n',
            '    pass\n',
            '\n',
            '\n',
            'def foo_correct():\n',
            '   pass\n',
            '\n',
            '\n',
            'def bar():\n',
            '   [1, 2, 3,\n',
            '     4, 5, 6,\n',
            '     ]\n',
            '\n',
            '\n',
            'if (1 in [1, 2, 3]\n',
            '      and bool(0) is False\n',
            '     and bool(1) is True):\n',
            '   pass\n'
        ]

        pep8style = pycodestyle.StyleGuide()
        pep8style.options.indent_size = 3
        count_errors = pep8style.input_file('stdin', lines=lines)
        stdout = sys.stdout.getvalue()
        self.assertEqual(count_errors, 4)
        expected = (
            'stdin:2:5: '
            'E111 indentation is not a multiple of 3'
        )
        self.assertTrue(expected in stdout)
        expected = (
            'stdin:11:6: '
            'E127 continuation line over-indented for visual indent'
        )
        self.assertTrue(expected in stdout)
        expected = (
            'stdin:12:6: '
            'E124 closing bracket does not match visual indentation'
        )
        self.assertTrue(expected in stdout)
        expected = (
            'stdin:17:6: '
            'E127 continuation line over-indented for visual indent'
        )
        self.assertTrue(expected in stdout)
