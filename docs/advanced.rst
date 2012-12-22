.. currentmodule:: pep8

==============
Advanced usage
==============


Automated tests
---------------

You can also execute `pep8` tests from Python code.  For example, this
can be highly useful for automated testing of coding style conformance
in your project::

  import unittest
  import pep8


  class TestCodeFormat(unittest.TestCase):

      def test_pep8_conformance(self):
          """Test that we conform to PEP8."""
          pep8style = pep8.StyleGuide(quiet=True)
          result = pep8style.check_files(['file1.py', 'file2.py'])
          self.assertEqual(result.total_errors, 0,
                           "Found code style errors (and warnings).")

If you are using `nosetests` for running tests, remove `quiet=True`
since Nose suppresses stdout.

There's also a shortcut for checking a single file::

  import pep8

  fchecker = pep8.Checker('testsuite/E27.py', show_source=True)
  file_errors = fchecker.check_all()

  print("Found %s errors (and warnings)" % file_errors)


Skip file header
----------------

Another example is related to the `feature request #143
<https://github.com/jcrocholl/pep8/issues/143>`_: skip a number of lines
at the beginning and the end of a file.  This use case is easy to implement
through a custom wrapper for the PEP 8 library::

  #!python
  import pep8

  LINES_SLICE = slice(14, -20)

  class PEP8(pep8.StyleGuide):
      """This subclass of pep8.StyleGuide will skip the first and last lines
      of each file."""

      def input_file(self, filename, lines=None, expected=None, line_offset=0):
          if lines is None:
              assert line_offset == 0
              line_offset = LINES_SLICE.start or 0
              lines = pep8.readlines(filename)[LINES_SLICE]
          return super(PEP8, self).input_file(
              filename, lines=lines, expected=expected, line_offset=line_offset)

  if __name__ == '__main__':
      pep8style = PEP8(parse_argv=True, config_file=True)
      report = pep8style.check_files()
      if report.total_errors:
          raise SystemExit(1)

This module declares a lines' window which skips 14 lines at the beginning
and 20 lines at the end.  If there's no line to skip at the end, it could be
changed with ``LINES_SLICE = slice(14, None)`` for example.

You can save it in a file and use it with the same options as the
original ``pep8``.
