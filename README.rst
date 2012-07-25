pep8 - Python style guide checker
=================================

pep8 is a tool to check your Python code against some of the style
conventions in `PEP 8`_.

.. _PEP 8: http://www.python.org/dev/peps/pep-0008/


Mailing List
------------
http://groups.google.com/group/pep8


Features
--------

* Plugin architecture: Adding new checks is easy.

* Parseable output: Jump to error location in your editor.

* Small: Just one Python file, requires only stdlib. You can use just
  the pep8.py file for this purpose.

* Comes with a comprehensive test suite.

Installation
------------

You can install, upgrade, uninstall pep8.py with these commands::

  $ pip install pep8
  $ pip install --upgrade pep8
  $ pip uninstall pep8

There's also a package for Debian/Ubuntu, but it's not always the
latest version::

  $ sudo apt-get install pep8

Example usage and output
------------------------

::

  $ pep8 --first optparse.py
  optparse.py:69:11: E401 multiple imports on one line
  optparse.py:77:1: E302 expected 2 blank lines, found 1
  optparse.py:88:5: E301 expected 1 blank line, found 0
  optparse.py:222:34: W602 deprecated form of raising exception
  optparse.py:347:31: E211 whitespace before '('
  optparse.py:357:17: E201 whitespace after '{'
  optparse.py:472:29: E221 multiple spaces before operator
  optparse.py:544:21: W601 .has_key() is deprecated, use 'in'

You can also make pep8.py show the source code for each error, and
even the relevant text from PEP 8::

  $ pep8 --show-source --show-pep8 testsuite/E40.py
  testsuite/E40.py:2:10: E401 multiple imports on one line
  import os, sys
           ^
      Imports should usually be on separate lines.

      Okay: import os\nimport sys
      E401: import sys, os


Or you can display how often each error was found::

  $ pep8 --statistics -qq Python-2.5/Lib
  232     E201 whitespace after '['
  599     E202 whitespace before ')'
  631     E203 whitespace before ','
  842     E211 whitespace before '('
  2531    E221 multiple spaces before operator
  4473    E301 expected 1 blank line, found 0
  4006    E302 expected 2 blank lines, found 1
  165     E303 too many blank lines (4)
  325     E401 multiple imports on one line
  3615    E501 line too long (82 characters)
  612     W601 .has_key() is deprecated, use 'in'
  1188    W602 deprecated form of raising exception

Quick help is available on the command line::

  $ pep8 -h
  Usage: pep8 [options] input ...

  Options:
    --version            show program's version number and exit
    -h, --help           show this help message and exit
    -v, --verbose        print status messages, or debug with -vv
    -q, --quiet          report only file names, or nothing with -qq
    -r, --repeat         (obsolete) show all occurrences of the same error
    --first              show first occurrence of each error
    --exclude=patterns   exclude files or directories which match these comma
                         separated patterns (default: .svn,CVS,.bzr,.hg,.git)
    --filename=patterns  when parsing directories, only check filenames matching
                         these comma separated patterns (default: *.py)
    --select=errors      select errors and warnings (e.g. E,W6)
    --ignore=errors      skip errors and warnings (e.g. E4,W)
    --show-source        show source code for each error
    --show-pep8          show text of PEP 8 for each error (implies --first)
    --statistics         count errors and warnings
    --count              print total number of errors and warnings to standard
                         error and set exit code to 1 if total is not null
    --max-line-length=n  set maximum allowed line length (default: 79)
    --format=format      set the error format [default|pylint|<custom>]
    --diff               report only lines changed according to the unified diff
                         received on STDIN

    Testing Options:
      --testsuite=dir    run regression tests from dir
      --doctest          run doctest on myself
      --benchmark        measure processing speed

    Configuration:
      The project options are read from the [pep8] section of the .pep8 file
      located in any parent folder of the path(s) being processed. Allowed
      options are: exclude, filename, select, ignore, max-line-length,
      count, format, quiet, show-pep8, show-source, statistics, verbose.

      --config=path      config file location (default: /home/user/.config/pep8)

Feedback
--------

Your feedback is more than welcome. Write email to
johann@rocholl.net or post bugs and feature requests on github:

http://github.com/jcrocholl/pep8/issues

Source download
---------------

.. image:: https://secure.travis-ci.org/jcrocholl/pep8.png?branch=master
   :target: https://secure.travis-ci.org/jcrocholl/pep8
   :alt: Build status

The source code is currently available on github. Fork away!

http://github.com/jcrocholl/pep8/
