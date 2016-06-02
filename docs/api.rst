===============
pycodestyle API
===============

.. module:: pycodestyle

The library provides classes which are usable by third party tools.

.. contents::
   :local:


.. _main_classes:

Checker Classes
---------------

The :class:`StyleGuide` class is used to configure a style guide checker
instance to check multiple files.

The :class:`Checker` class can be used to check a single file.


.. autoclass:: StyleGuide(parse_argv=False, config_file=None, parser=None, paths=None, report=None, **kwargs)

   .. automethod:: init_report(reporter=None)
   .. automethod:: check_files(paths=None)
   .. automethod:: input_file(filename, lines=None, expected=None, line_offset=0)
   .. automethod:: input_dir(dirname)
   .. automethod:: excluded(filename, parent=None)
   .. automethod:: ignore_code(code)
   .. automethod:: get_checks(argument_name)

.. autoclass:: Checker(filename=None, lines=None, report=None, **kwargs)

   .. automethod:: readline
   .. automethod:: run_check(check, argument_names)
   .. automethod:: check_physical(line)
   .. automethod:: build_tokens_line
   .. automethod:: check_logical
   .. automethod:: check_ast
   .. automethod:: generate_tokens
   .. automethod:: check_all(expected=None, line_offset=0)


.. _report_classes:

Report Classes
--------------

.. autoclass:: BaseReport(options)

   .. automethod:: start
   .. automethod:: stop
   .. automethod:: init_file(filename, lines, expected, line_offset)
   .. automethod:: increment_logical_line
   .. automethod:: error(line_number, offset, text, check)
   .. automethod:: get_file_results
   .. automethod:: get_count(prefix='')
   .. automethod:: get_statistics(prefix='')
   .. automethod:: print_statistics(prefix='')
   .. automethod:: print_benchmark

.. autoclass:: FileReport

.. autoclass:: StandardReport

.. autoclass:: DiffReport


Utilities
---------

.. autofunction:: expand_indent(line)
.. autofunction:: mute_string(text)
.. autofunction:: read_config(options, args, arglist, parser)
.. autofunction:: process_options(arglist=None, parse_argv=False, config_file=None)
.. autofunction:: register_check(func_or_cls, codes=None)

..
  These ones are used internally, but they don't need advertising
  .. autofunction:: readlines(filename)
  .. autofunction:: isidentifier(word)
  .. autofunction:: stdin_get_value()
  .. autofunction:: parse_udiff(diff, patterns=None, parent='.')
  .. autofunction:: filename_match(filename, patterns, default=True)
  .. autofunction:: get_parser(prog='pycodestyle', version=pycodestyle.__version__)
  .. autofunction:: init_checks_registry()
