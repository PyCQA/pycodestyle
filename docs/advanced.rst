.. currentmodule:: pycodestyle

==============
Advanced usage
==============


Automated tests
---------------

You can also execute ``pycodestyle`` tests from Python code.  For example, this
can be highly useful for automated testing of coding style conformance
in your project::

  import unittest
  import pycodestyle


  class TestCodeFormat(unittest.TestCase):

      def test_conformance(self):
          """Test that we conform to PEP-8."""
          style = pycodestyle.StyleGuide(quiet=True)
          result = style.check_files(['file1.py', 'file2.py'])
          self.assertEqual(result.total_errors, 0,
                           "Found code style errors (and warnings).")

If you are using ``nosetests`` for running tests, remove ``quiet=True``
since Nose suppresses stdout.

There's also a shortcut for checking a single file::

  import pycodestyle

  fchecker = pycodestyle.Checker('testsuite/E27.py', show_source=True)
  file_errors = fchecker.check_all()

  print("Found %s errors (and warnings)" % file_errors)


Configuring tests
-----------------

You can configure automated ``pycodestyle`` tests in a variety of ways.

For example, you can pass in a path to a configuration file that ``pycodestyle``
should use::

  import pycodestyle

  style = pycodestyle.StyleGuide(config_file='/path/to/tox.ini')

You can also set specific options explicitly::

  style = pycodestyle.StyleGuide(ignore=['E501'])


Skip file header
----------------

Another example is related to the `feature request #143
<https://github.com/pycqa/pycodestyle/issues/143>`_: skip a number of lines
at the beginning and the end of a file.  This use case is easy to implement
through a custom wrapper for the PEP 8 library::

  #!python
  import pycodestyle

  LINES_SLICE = slice(14, -20)

  class StyleGuide(pycodestyle.StyleGuide):
      """This subclass of pycodestyle.StyleGuide will skip the first and last lines
      of each file."""

      def input_file(self, filename, lines=None, expected=None, line_offset=0):
          if lines is None:
              assert line_offset == 0
              line_offset = LINES_SLICE.start or 0
              lines = pycodestyle.readlines(filename)[LINES_SLICE]
          return super(StyleGuide, self).input_file(
              filename, lines=lines, expected=expected, line_offset=line_offset)

  if __name__ == '__main__':
      style = StyleGuide(parse_argv=True, config_file=True)
      report = style.check_files()
      if report.total_errors:
          raise SystemExit(1)

This module declares a lines' window which skips 14 lines at the beginning
and 20 lines at the end.  If there's no line to skip at the end, it could be
changed with ``LINES_SLICE = slice(14, None)`` for example.

You can save it in a file and use it with the same options as the
original ``pycodestyle``.
