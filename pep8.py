#!/usr/bin/python


"""
Check Python source code formatting.

Groups of errors and warnings:
E100 indentation
E110 whitespace
E130 imports
E140 line length
"""


import os
import sys
import inspect
import re
from optparse import OptionParser


__revision__ = '$Rev$'


indent_match = re.compile(r'([ \t]*)').match
last_token_match = re.compile(r'(\w+|\S)\s*$').search


operators = """
+  -  *  /  %  =  <  >  <>
+= -= *= /= %= == <= >= !=
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
        return indent.index('\t'), "W109 indentation contains tabs"


def trailing_whitespace(physical_line):
    """
    JCR: Trailing whitespace is superfluous.
    """
    physical_line = physical_line.rstrip('\n')
    physical_line = physical_line.rstrip('\r')
    stripped = physical_line.rstrip()
    if physical_line != stripped:
        return len(stripped), "W119 trailing whitespace"


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
        return 79, "E140 line is longer than 79 characters (%d)" % length


##############################################################################
# Various checks for logical lines
##############################################################################


def indentation(logical_line_muted, indent_level):
    """
    Use 4 spaces per indentation level.

    For really old code that you don't want to mess up, you can continue to
    use 8-space tabs.
    """
    line = logical_line_muted
    if line == '':
        return
    previous_level = state.get('indent_level', 0)
    indent_expect = state.get('indent_expect', False)
    state['indent_expect'] = line.endswith(':')
    indent_char = state.get('indent_char', ' ')
    state['indent_level'] = indent_level
    if indent_char == ' ' and indent_level % 4:
        return 0, "E102 indentation is not a multiple of four"
    if indent_expect and indent_level <= previous_level:
        return 0, "E103 expected an indented block"
    if not indent_expect and indent_level > previous_level:
        return 0, "E104 unexpected indentation"


def blank_lines(logical_line, indent_level):
    """
    Separate top-level function and class definitions with two blank lines.

    Method definitions inside a class are separated by a single blank line.

    Extra blank lines may be used (sparingly) to separate groups of related
    functions.  Blank lines may be omitted between a bunch of related
    one-liners (e.g. a set of dummy implementations).

    Use blank lines in functions, sparingly, to indicate logical sections.
    """
    first_line = 'blank_lines' not in state
    count = state.get('blank_lines', 0)
    if logical_line == '':
        state['blank_lines'] = count + 1
    else:
        state['blank_lines'] = 0
    if logical_line.startswith('def') and not first_line:
        if indent_level > 0 and count != 1:
            return 0, "E111 expected 1 blank line, found %d" % count
        if indent_level == 0 and count != 2:
            return 0, "E112 expected 2 blank lines, found %d" % count
    if count > 2:
        return 0, "E113 too many blank lines (%d)" % count


def extraneous_whitespace(logical_line_muted):
    """
    Avoid extraneous whitespace in the following situations:

    - Immediately inside parentheses, brackets or braces.

    - Immediately before a comma, semicolon, or colon.
    """
    line = logical_line_muted
    for char in '([{':
        found = line.find(char + ' ')
        if found > -1:
            return found + 1, "E114 whitespace after '%s'" % char
    for char in '}])':
        found = line.find(' ' + char)
        if found > -1 and line[found - 1] != ',':
            return found, "E115 whitespace before '%s'" % char
    for char in ',;:':
        found = line.find(' ' + char)
        if found > -1:
            return found, "E116 whitespace before '%s'" % char


def whitespace_before_parameters(logical_line_muted):
    """
    Avoid extraneous whitespace in the following situations:

    - Immediately before the open parenthesis that starts the argument
      list of a function call.

    - Immediately before the open parenthesis that starts an indexing or
      slicing.
    """
    line = logical_line_muted
    for char in '([':
        found = -1
        while True:
            found = line.find(' ' + char, found + 1)
            if found == -1:
                break
            before = last_token_match(line[:found]).group(1)
            if before in operators:
                continue
            if before in 'if in while and or not ,'.split():
                continue
            return found, "E117 whitespace before '%s'" % char


def whitespace_around_operator(logical_line_muted):
    """
    Avoid extraneous whitespace in the following situations:

    - More than one space around an assignment (or other) operator to
      align it with another.
    """
    line = logical_line_muted
    for operator in operators:
        found = line.find('  ' + operator)
        if found > -1:
            return found, "E118 too much whitespace around operator"


def imports_on_separate_lines(logical_line):
    """
    Imports should usually be on separate lines.
    """
    if logical_line.startswith('import ') and logical_line.count(','):
        return logical_line.index(','), "E130 multiple imports on one line"


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
    if line.count('"""'):
        return bool(line.count('"""') % 2)
    if line.count("'''"):
        return bool(line.count("'''") % 2)
    return False


def get_indent(line):
    """
    Return the amount of indentation.
    Tabs are expanded to the next multiple of 8.
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


def error(filename, location, offset, text):
    """
    Print an error or warning message with parseable location.
    """
    if type(location) is int:
        line_number = location
    else:
        merged_offset = offset
        for start_offset, original_number, indent in location:
            if merged_offset >= start_offset:
                offset = merged_offset - start_offset + indent
                line_number = original_number
    message("%s:%s:%d: %s" %
            (filename, line_number, offset + 1, text))


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
            indent = get_indent(physical[line_number][1])
            next = physical[line_number][1].strip()
            if line.endswith('\\'):
                line = line[-1]
            elif line[-1] in '([{':
                pass
            # elif next[0] in '}])':
            #     pass
            else:
                line += ' '
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


def check_lines(argument_name, lines, filename):
    """
    Find all checks with matching first argument name and run all of
    them on each line.
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
                print line_arg, location[0]
                result = check(line_arg, location[0][2])
            if result is not None:
                error_count += 1
                offset, text = result
                # print name, text
                if options.testsuite:
                    code = text[:4]
                    base = os.path.basename(filename)[:4]
                    if base == code:
                        continue
                    if base[0] == 'E' and code[0] == 'W':
                        continue
                print location, offset
                error(filename, location, offset, text)
                if options.show_source:
                    message('    ' + line)
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
    usage = "usage: %prog [options] input ..."
    parser = OptionParser(usage)
    parser.add_option('-v', '--verbose',
                      default=0, action='count',
                      help="print status messages")
    parser.add_option('-q', '--quiet',
                      default=False, action='store_true',
                      help="report file names only")
    parser.add_option('--exclude', metavar='dirs', default= '.svn,CVS',
                      help="ignore subdirectories (default .svn,CVS)")
    parser.add_option('--ignore', metavar='errors', default='',
                      help="ignore errors (e.g. E301,W120)")
    parser.add_option('--testsuite', metavar='dir',
                      help="run regression tests from dir")
    parser.add_option('--doctest', action='store_true',
                      help="run doctest on pep8.py")
    parser.add_option('--show-source', action='store_true',
                      help="show source code for each error")
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
    if options.ignore:
        options.ignore = options.ignore.split(',')
    else:
        options.ignore = []
    for path in args:
        if os.path.isdir(path):
            input_dir(path)
        else:
            input_file(path)


if __name__ == '__main__':
    _main()
