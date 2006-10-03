#!/usr/bin/python
# pep8.py - Check Python source code formatting, according to PEP 8
# Copyright (C) 2006 Johann C. Rocholl <johann@browsershots.org>
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
# BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
Check Python source code formatting, according to PEP 8:
http://www.python.org/dev/peps/pep-0008/

This tool is not a complete implementation of all the recommendations
in PEP 8. Many parts of PEP 8 are impossible to check automatically.
Even of the possible parts, this early version of pep8.py checks only
a small subset.

For usage and a list of options, try this:
$ python pep8.py -h

Groups of errors and warnings:
E100 indentation
E200 whitespace
E300 blank lines
E400 imports
E500 line length

This program and its regression test suite live here:
http://svn.browsershots.org/trunk/devtools/pep8/
http://trac.browsershots.org/browser/trunk/devtools/pep8/

You can add checks to this program simply by adding a new check
function. All checks operate on single lines. Where necessary, any
state is kept in the global dict 'state'. The check function requests
physical or logical lines by the name of the first argument:

def tabs_or_spaces(physical_line)
def indentation(logical_line, indent_level)

The second example above demonstrates how check functions can request
additional information with extra arguments, for example the level of
indentation (with tabs expanded to the next multiple of 8).

The docstring of each check function shall be the respective part of
text from PEP 8. It is printed if the user enables --show-pep8.
"""

import os
import sys
import inspect
import re
from optparse import OptionParser
from keyword import iskeyword

__version__ = '0.1.0'
__revision__ = '$Rev$'

indent_match = re.compile(r'([ \t]*)').match
last_token_match = re.compile(r'(\w+|\S)\s*$').search

operators = """
+  -  *  /  %  ^  &  |  =  <  >
+= -= *= /= %= ^= &= |= == <= >=
!= <> :
in is or not and
""".split()

options = None
state = {}


##############################################################################
# Various checks for physical lines
##############################################################################


def tabs_or_spaces(physical_line):
    """
    Never mix tabs and spaces.

    The most popular way of indenting Python is with spaces only.  The
    second-most popular way is with tabs only.  Code indented with a mixture
    of tabs and spaces should be converted to using spaces exclusively.  When
    invoking the Python command line interpreter with the -t option, it issues
    warnings about code that illegally mixes tabs and spaces.  When using -tt
    these warnings become errors.  These options are highly recommended!
    """
    indent = indent_match(physical_line).group(1)
    if not indent:
        return
    if 'indent_char' in state:
        indent_char = state['indent_char']
    else:
        indent_char = indent[0]
        state['indent_char'] = indent_char
    for offset, char in enumerate(indent):
        if char != indent_char:
            return offset, "E101 indentation contains mixed spaces and tabs"


def tabs_obsolete(physical_line):
    """
    For new projects, spaces-only are strongly recommended over tabs.  Most
    editors have features that make this easy to do.
    """
    indent = indent_match(physical_line).group(1)
    if indent.count('\t'):
        return indent.index('\t'), "W191 indentation contains tabs"


def trailing_whitespace(physical_line):
    """
    JCR: Trailing whitespace is superfluous.
    """
    physical_line = physical_line.rstrip('\n') # chr(10), newline
    physical_line = physical_line.rstrip('\r') # chr(13), carriage return
    physical_line = physical_line.rstrip('\x0c') # chr(12), form feed, ^L
    stripped = physical_line.rstrip()
    if physical_line != stripped:
        return len(stripped), "W291 trailing whitespace"


def maximum_line_length(physical_line):
    """
    Limit all lines to a maximum of 79 characters.

    There are still many devices around that are limited to 80 character
    lines; plus, limiting windows to 80 characters makes it possible to have
    several windows side-by-side.  The default wrapping on such devices looks
    ugly.  Therefore, please limit all lines to a maximum of 79 characters.
    For flowing long blocks of text (docstrings or comments), limiting the
    length to 72 characters is recommended.
    """
    length = len(physical_line.rstrip())
    if length > 79:
        return 79, "E501 long line, %d characters" % length


##############################################################################
# Various checks for logical lines
##############################################################################


def indentation(logical_line, indent_level):
    """
    Use 4 spaces per indentation level.

    For really old code that you don't want to mess up, you can continue to
    use 8-space tabs.
    """
    line = logical_line
    if line == '':
        return
    previous_level = state.get('indent_level', 0)
    indent_expect = state.get('indent_expect', False)
    state['indent_expect'] = line.rstrip('#').rstrip().endswith(':')
    indent_char = state.get('indent_char', ' ')
    state['indent_level'] = indent_level
    if indent_char == ' ' and indent_level % 4:
        return 0, "E111 indentation is not a multiple of four"
    if indent_expect and indent_level <= previous_level:
        return 0, "E112 expected an indented block"
    if not indent_expect and indent_level > previous_level:
        return 0, "E113 unexpected indentation"


def blank_lines(logical_line, indent_level):
    """
    Separate top-level function and class definitions with two blank lines.

    Method definitions inside a class are separated by a single blank line.

    Extra blank lines may be used (sparingly) to separate groups of related
    functions.  Blank lines may be omitted between a bunch of related
    one-liners (e.g. a set of dummy implementations).

    Use blank lines in functions, sparingly, to indicate logical sections.
    """
    line = logical_line
    first_line = 'blank_lines' not in state
    count = state.get('blank_lines', 0)
    if line == '':
        state['blank_lines'] = count + 1
    else:
        state['blank_lines'] = 0
    if line.startswith('def ') and not first_line:
        if indent_level > 0 and count != 1:
            return 0, "E301 expected 1 blank line, found %d" % count
        if indent_level == 0 and count != 2:
            return 0, "E302 expected 2 blank lines, found %d" % count
    if count > 2:
        return 0, "E303 too many blank lines (%d)" % count


def extraneous_whitespace(logical_line):
    """
    Avoid extraneous whitespace in the following situations:

    - Immediately inside parentheses, brackets or braces.

    - Immediately before a comma, semicolon, or colon.
    """
    line = logical_line
    for char in '([{':
        found = line.find(char + ' ')
        if found > -1:
            return found + 1, "E201 whitespace after '%s'" % char
    for char in '}])':
        found = line.find(' ' + char)
        if found > -1 and line[found - 1] != ',':
            return found, "E202 whitespace before '%s'" % char
    for char in ',;:':
        found = line.find(' ' + char)
        if found > -1:
            return found, "E203 whitespace before '%s'" % char


def whitespace_before_parameters(logical_line):
    """
    Avoid extraneous whitespace in the following situations:

    - Immediately before the open parenthesis that starts the argument
      list of a function call.

    - Immediately before the open parenthesis that starts an indexing or
      slicing.
    """
    line = logical_line
    for char in '([':
        found = -1
        while True:
            found = line.find(' ' + char, found + 1)
            if found == -1:
                break
            before = last_token_match(line[:found]).group(1)
            if (before in operators or
                before == ',' or
                iskeyword(before) or
                line.startswith('class')):
                continue
            return found, "E211 whitespace before '%s'" % char


def whitespace_around_operator(logical_line):
    """
    Avoid extraneous whitespace in the following situations:

    - More than one space around an assignment (or other) operator to
      align it with another.
    """
    line = logical_line
    for operator in operators:
        found = line.find('  ' + operator)
        if found > -1:
            return found, "E221 multiple spaces before operator"
        found = line.find('\t' + operator)
        if found > -1:
            return found, "E222 tab before operator"


def imports_on_separate_lines(logical_line):
    """
    Imports should usually be on separate lines.
    """
    line = logical_line
    if line.startswith('import '):
        found = line.find(',')
        if found > -1:
            return found, "E401 multiple imports on one line"


##############################################################################
# Helper functions
##############################################################################


def quoted_quote(line, pos):
    """
    Is line[pos] preceded with an odd number of backslashes?

    >>> quoted_quote('\\\\""', 1)
    True
    >>> quoted_quote('\\\\\\\\""', 2)
    False
    """
    count = 0
    while pos > count and line[pos - count - 1] == '\\':
        count += 1
    return bool(count % 2)


def find_real_quote(line, char, pos):
    """
    Find the next quote character that is not quoted with backslashes.

    >>> find_real_quote('abc\\\\"abc"abc\\\\"abc', '"', 0)
    8
    >>> find_real_quote('abc', '\"', 0)
    -1
    """
    pos = line.find(char, pos)
    while quoted_quote(line, pos):
        pos = line.find(char, pos + 1)
    return pos


def mute_strings(line):
    """
    Overwrite strings with 'xxxxx' to prevent syntax matching.

    >>> mute_strings('list("abc")')
    'list("xxx")'
    >>> mute_strings("list('abc')")
    "list('xxx')"
    """
    for quote in '\'"':
        start = -1
        while True:
            start = find_real_quote(line, quote, start + 1)
            stop = find_real_quote(line, quote, start + 1)
            if start == -1 or stop == -1:
                break
            middle = 'x' * (stop - start - 1)
            line = line[:start+1] + middle + line[stop:]
            start = stop
    return line


def mute_comment(line):
    """
    Delete comment text to prevent syntax matching.

    >>> mute_comment('# abc')
    '#'
    >>> mute_comment('abc # xyz')
    'abc #'
    """
    found = line.find('#')
    if found == -1:
        return line
    return line[:found+1]


def count_parens(line, chars):
    """
    Count parens, but not in strings.

    >>> count_parens('abc', '([{')
    0
    >>> count_parens('([{', '([{')
    3
    >>> count_parens('abc()', '(')
    1
    >>> count_parens('abc("xyz()")', '(')
    1
    """
    result = 0
    pos = 0
    while pos < len(line):
        if line[pos] in chars:
            result += 1
        if line[pos] == '"':
            pos += 1
            while pos < len(line) and (
                line[pos] != '"' or quoted_quote(line, pos)):
                pos += 1
        if pos >= len(line):
            break
        if line[pos] == "'":
            pos += 1
            while pos < len(line) and (
                line[pos] != "'" or quoted_quote(line, pos)):
                pos += 1
        pos += 1
    return result


def triple_quoted_incomplete(line):
    """
    Test if line contains an incomplete triple-quoted string.

    >>> triple_quoted_incomplete("'''")
    True
    >>> triple_quoted_incomplete("''''''")
    False
    >>> triple_quoted_incomplete("'''''''''")
    True
    """
    line = mute_strings(line)
    single = line.find("'''")
    double = line.find('"""')
    if single > -1 and double > -1:
        if single < double:
            return bool(line.count("'''") % 2)
        else:
            return bool(line.count('"""') % 2)
    elif single > -1:
        return bool(line.count("'''") % 2)
    elif double > -1:
        return bool(line.count('"""') % 2)
    return False


def get_indent(line):
    """
    Return the amount of indentation.
    Tabs are expanded to the next multiple of 8.

    >>> get_indent('    abc')
    4
    >>> get_indent('\\tabc')
    8
    >>> get_indent('    \\tabc')
    8
    >>> get_indent('       \\tabc')
    8
    >>> get_indent('        \\tabc')
    16
    """
    result = 0
    for char in line:
        if char == '\t':
            result = result / 8 * 8 + 8
        elif char == ' ':
            result += 1
        else:
            break
    return result


##############################################################################
# Framework to run all checks
##############################################################################


def message(text):
    """Print a message."""
    # print >> sys.stderr, options.prog + ': ' + text
    # print >> sys.stderr, text
    print text


def load(filename):
    """
    Load lines from a file and add line numbers.
    """
    lines = []
    line_number = 0
    for line in file(filename):
        line_number += 1
        lines.append((line_number, line))
    return lines


def physical_to_logical(physical):
    """
    Convert multi-line statements to single lines.
    """
    logical = []
    line_number = 0
    while line_number < len(physical):
        indent = get_indent(physical[line_number][1])
        line = physical[line_number][1].strip()
        mapping = [(0, line_number + 1, indent)]
        while (line.endswith('\\') or
               triple_quoted_incomplete(line) or
               count_parens(line, '([{') > count_parens(line, ')]}')):
            line_number += 1
            if line_number >= len(physical):
                break
            indent = get_indent(physical[line_number][1])
            next = physical[line_number][1].strip()
            if line.endswith('\\'):
                line = line[:-1]
            elif line[-1] in '([{':
                pass
            # elif next[0] in '}])':
            #     pass
            else:
                line += ' '
            # print line_number, line, '+', next
            mapping.append((len(line), line_number + 1, indent))
            line += next
        logical.append((mapping, line))
        line_number += 1
    return logical


def find_checks(argument_name):
    """
    Find all globally visible functions where the first argument name
    starts with argument_name.
    """
    checks = []
    function_type = type(find_checks)
    for name, function in globals().iteritems():
        if type(function) is function_type:
            args = inspect.getargspec(function)[0]
            if len(args) >= 1 and args[0].startswith(argument_name):
                checks.append((name, function, args))
    checks.sort()
    return checks


def ignore_code(code):
    """
    Check if options.ignore contains a prefix of the error code.
    """
    for ignore in options.ignore:
        if code.startswith(ignore):
            return True


def extract_subline(location, offset, line):
    """
    Extract a physical line from a logical line.
    """
    if type(location) is int:
        return location, offset, line
    else:
        for start_offset, original_number, indent in location:
            if offset >= start_offset:
                subline_indent = indent
                subline_start = start_offset
                subline_offset = offset - start_offset + indent
                subline_number = original_number
        subline_end = len(line)
        for index in range(1, len(location)):
            if location[index - 1][0] == subline_start:
                subline_end = location[index][0]
        subline = ' ' * subline_indent + line[subline_start:subline_end]
        return subline_number, subline_offset, subline


def report_error(filename, location, offset, line, check, text):
    """
    Report an error, according to options.
    """
    code = text[:4]
    if options.testsuite:
        base = os.path.basename(filename)[:4]
        if base == code:
            return
        if base[0] == 'E' and code[0] == 'W':
            return
    if ignore_code(code):
        return
    # print location, offset
    subline_number, subline_offset, subline = extract_subline(
        location, offset, line)
    message("%s:%s:%d: %s" %
            (filename, subline_number, subline_offset + 1, text))
    if options.show_source:
        message(subline.rstrip())
        message(' ' * subline_offset + '^')
    if options.show_pep8:
        message(check.__doc__.lstrip('\n').rstrip())


def check_lines(argument_name, lines, filename):
    """
    Find all checks with matching first argument name. Then iterate
    over the input lines and run all checks on each line.
    """
    global state
    state = {} # {'previous_line': None}
    error_count = 0
    checks = find_checks(argument_name)
    for location, line in lines:
        line_muted = mute_comment(mute_strings(line))
        for name, check, args in checks:
            if args[0].endswith('_line'):
                line_arg = line
            elif args[0].endswith('_muted'):
                line_arg = line_muted
            else:
                raise NotImplementedError('unsupported argument %s' % args[0])
            if len(args) == 1:
                result = check(line_arg)
            elif len(args) == 2 and args[1] == 'indent_level':
                # print line_arg, location[0]
                result = check(line_arg, location[0][2])
            if result is not None:
                error_count += 1
                offset, text = result
                if options.quiet:
                    message(filename)
                    return 1
                else:
                    report_error(filename, location, offset, line, check, text)
        # state['previous_line'] = line
    return error_count


def input_file(filename):
    """
    Run all checks on a Python source file.
    """
    if options.verbose:
        message('checking ' + filename)
    physical = load(filename)
    errors = check_lines('physical_line', physical, filename)
    logical = physical_to_logical(physical)
    errors += check_lines('logical_line', logical, filename)
    if options.testsuite and not errors:
        message("%s: %s" % (filename, "no errors found"))


def input_dir(dirname):
    """
    Check all Python source files in this directory and all subdirectories.
    """
    dirname = dirname.rstrip('/')
    if dirname in options.exclude:
        return
    for root, dirs, files in os.walk(dirname):
        if options.verbose:
            message('directory ' + root)
        for dirname in options.exclude:
            if dirname in dirs:
                dirs.remove(dirname)
        dirs.sort()
        files.sort()
        for filename in files:
            input_file(os.path.join(root, filename))


def _main():
    """
    Parse command line options and run checks on Python source.
    """
    global options
    usage = "%prog [options] input ..."
    parser = OptionParser(usage)
    parser.add_option('-v', '--verbose',
                      default=0, action='count',
                      help="print status messages")
    parser.add_option('-q', '--quiet',
                      default=False, action='store_true',
                      help="report file names only")
    parser.add_option('--exclude', metavar='dirs', default= '.svn,CVS',
                      help="skip subdirectories (default .svn,CVS)")
    parser.add_option('--ignore', metavar='errors', default='',
                      help="e.g. E4,W for imports and all warnings")
    parser.add_option('--show-source', action='store_true',
                      help="show source code for each error")
    parser.add_option('--show-pep8', action='store_true',
                      help="show text of PEP 8 for each error")
    parser.add_option('--testsuite', metavar='dir',
                      help="run regression tests from dir")
    parser.add_option('--doctest', action='store_true',
                      help="run doctest on myself")
    options, args = parser.parse_args()
    if options.doctest:
        import doctest
        return doctest.testmod()
    if options.testsuite:
        args.append(options.testsuite)
    if len(args) == 0:
        parser.error('input not specified')
    options.prog = os.path.basename(sys.argv[0])
    options.exclude = options.exclude.split(',')
    for index in range(len(options.exclude)):
        options.exclude[index] = options.exclude[index].rstrip('/')
    if options.ignore:
        options.ignore = options.ignore.split(',')
    else:
        options.ignore = []
    # print options.exclude, options.ignore
    for path in args:
        if os.path.isdir(path):
            input_dir(path)
        else:
            input_file(path)


if __name__ == '__main__':
    _main()
