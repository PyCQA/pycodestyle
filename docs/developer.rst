.. currentmodule:: pycodestyle

=================
Developer's notes
=================


Source code
~~~~~~~~~~~

The source code is currently `available on GitHub`_ under the terms and
conditions of the :ref:`Expat license <license>`.  Fork away!

* `Source code <https://github.com/pycqa/pycodestyle>`_ and
  `issue tracker <https://github.com/pycqa/pycodestyle/issues>`_ on GitHub.
* `Continuous tests <http://travis-ci.org/pycqa/pycodestyle>`_ against Python
  2.6 through 3.5 as well as the nightly Python build and PyPy, on `Travis-CI
  platform <https://docs.travis-ci.com//>`_.

.. _available on GitHub: https://github.com/pycqa/pycodestyle


Direction
~~~~~~~~~

Some high-level aims and directions to bear in mind for contributions:

* ``pycodestyle`` is intended to be as fast as possible.
  Using the ``ast`` module defeats that purpose.
  The `pep8-naming <https://github.com/flintwork/pep8-naming>`_ plugin exists
  for this sort of functionality.
* If you want to provide extensibility / plugins,
  please see `flake8 <https://gitlab.com/pycqa/flake8>`_ -
  ``pycodestyle`` doesn't want or need a plugin architecture.
* Python 2.6 support is still deemed important.
* ``pycodestyle`` aims to have no external dependencies.


Contribute
~~~~~~~~~~

You can add checks to this program by writing plugins.  Each plugin is
a simple function that is called for each line of source code, either
physical or logical.

Physical line:

* Raw line of text from the input file.

Logical line:

* Multi-line statements converted to a single line.
* Stripped left and right.
* Contents of strings replaced with ``"xxx"`` of same length.
* Comments removed.

The check function requests physical or logical lines by the name of
the first argument::

  def maximum_line_length(physical_line)
  def extraneous_whitespace(logical_line)
  def blank_lines(logical_line, blank_lines, indent_level, line_number)

The last example above demonstrates how check plugins can request
additional information with extra arguments.  All attributes of the
:class:`Checker` object are available.  Some examples:

* ``lines``: a list of the raw lines from the input file
* ``tokens``: the tokens that contribute to this logical line
* ``line_number``: line number in the input file
* ``total_lines``: number of lines in the input file
* ``blank_lines``: blank lines before this one
* ``indent_char``: indentation character in this file (``" "`` or ``"\t"``)
* ``indent_level``: indentation (with tabs expanded to multiples of 8)
* ``previous_indent_level``: indentation on previous line
* ``previous_logical``: previous logical line

Check plugins can also maintain per-file state. If you need this, declare
a parameter named ``checker_state``. You will be passed a dict, which will be
the same one for all lines in the same file but a different one for different
files. Each check plugin gets its own dict, so you don't need to worry about
clobbering the state of other plugins.

The docstring of each check function shall be the relevant part of
text from `PEP 8`_.  It is printed if the user enables ``--show-pep8``.
Several docstrings contain examples directly from the `PEP 8`_ document.

::

  Okay: spam(ham[1], {eggs: 2})
  E201: spam( ham[1], {eggs: 2})

These examples are verified automatically when ``pycodestyle.py`` is run with
the ``--doctest`` option.  You can add examples for your own check functions.
The format is simple: ``"Okay"`` or error/warning code followed by colon and
space, the rest of the line is example source code.  If you put ``'r'`` before
the docstring, you can use ``\n`` for newline and ``\t`` for tab.

Then be sure to pass the tests::

  $ python pycodestyle.py --testsuite testsuite
  $ python pycodestyle.py --doctest
  $ python pycodestyle.py --verbose pycodestyle.py

When contributing to pycodestyle, please observe our `Code of Conduct`_.

To run the tests, the core developer team and Travis-CI use tox::

    $ pip install -r dev-requirements.txt
    $ tox

All the tests should pass for all available interpreters, with the summary of::

    congratulations :)

.. _PEP 8: http://www.python.org/dev/peps/pep-0008/
.. _Code of Conduct: http://meta.pycqa.org/en/latest/code-of-conduct.html


Changes
~~~~~~~

.. include:: ../CHANGES.txt
   :start-line: 3
