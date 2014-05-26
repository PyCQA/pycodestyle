.. currentmodule:: pep8

=================
Developer's notes
=================


Source code
~~~~~~~~~~~

The source code is currently `available on GitHub`_ under the terms and
conditions of the :ref:`Expat license <license>`.  Fork away!

* `Source code <https://github.com/jcrocholl/pep8>`_ and
  `issue tracker <https://github.com/jcrocholl/pep8/issues>`_ on GitHub.
* `Continuous tests <http://travis-ci.org/jcrocholl/pep8>`_ against Python
  2.6 through 3.4 and PyPy, on `Travis-CI platform
  <http://about.travis-ci.org/>`_.

.. _available on GitHub: https://github.com/jcrocholl/pep8


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

The docstring of each check function shall be the relevant part of
text from `PEP 8`_.  It is printed if the user enables ``--show-pep8``.
Several docstrings contain examples directly from the `PEP 8`_ document.

::

  Okay: spam(ham[1], {eggs: 2})
  E201: spam( ham[1], {eggs: 2})

These examples are verified automatically when pep8.py is run with the
``--doctest`` option.  You can add examples for your own check functions.
The format is simple: ``"Okay"`` or error/warning code followed by colon
and space, the rest of the line is example source code.  If you put ``'r'``
before the docstring, you can use ``\n`` for newline and ``\t`` for tab.

Then be sure to pass the tests::

  $ python pep8.py --testsuite testsuite
  $ python pep8.py --doctest
  $ python pep8.py --verbose pep8.py

.. _PEP 8: http://www.python.org/dev/peps/pep-0008/


Changes
~~~~~~~

.. include:: ../CHANGES.txt
   :start-line: 3
