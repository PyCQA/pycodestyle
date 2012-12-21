.. currentmodule:: pep8

=================
Developer's notes
=================


Source code
~~~~~~~~~~~

The source code is currently available on github. Fork away!
Then be sure to pass the tests::

  $ python pep8.py --testsuite testsuite
  $ python pep8.py --doctest
  $ python pep8.py --verbose pep8.py

* `Source code <https://github.com/jcrocholl/pep8>`_ and
  `issue tracker <https://github.com/jcrocholl/pep8/issues>`_ on GitHub.
* `Continuous tests <http://travis-ci.org/jcrocholl/pep8>`_ against Python
  2.5 through 3.2 and PyPy, on `Travis-CI platform
  <http://about.travis-ci.org/>`_.


Third-party integration
~~~~~~~~~~~~~~~~~~~~~~~

You can also execute `pep8` tests from Python code. For example, this
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

See also:

* the `list of error codes
  <https://github.com/jcrocholl/pep8/wiki/ErrorCodes>`_.
* the `list of related tools
  <https://github.com/jcrocholl/pep8/wiki/RelatedTools>`_.


Changes
~~~~~~~

.. include:: ../CHANGES.txt
   :start-line: 3
