#!/usr/bin/python


"""
Check Python source code formatting.
"""


import os, sys, inspect, re
from optparse import OptionParser


__revision__ = '$Rev$'


options = None
state = {}


##############################################################################
# Various checks for physical lines
##############################################################################


indent_match = re.compile(r'[ \t]*').match
def tabs_or_spaces(physical_line):
    indent = indent_match(physical_line).group(0)
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


def trailing_whitespace(physical_line):
    physical_line = physical_line.rstrip('\n')
    physical_line = physical_line.rstrip('\r')
    stripped = physical_line.rstrip()
    if physical_line != stripped:
        return (len(stripped), "W110 trailing whitespace")


##############################################################################
# Various checks for logical lines
##############################################################################


def indentation(logical_line, indent):
    """
    Check for correct amount of indentation.
    """
    previous = state.get('indent_level', 0)
    indent_expect = state.get('indent_expect', False)
    state['indent_expect'] = logical_line.endswith(':')
    indent_char = state.get('indent_char', ' ')
    if indent_char == ' ':
        if indent % 4:
            return indent, "E102 indentation is not a multiple of four"
        indent_level = indent / 4
    elif indent_char == '\t':
        indent_level = indent
    state['indent_level'] = indent_level
    if indent_expect and indent_level <= previous:
        return indent, "E103 expected an indented block"
    if not indent_expect and indent_level > previous:
        return indent, "E104 unexpected indentation"


named_arguments_space = re.compile(r'(.+?\(.+?)(=\s|\s=)\)').match
def named_arguments(logical_line):
    """
    Check formatting of named arguments.
    """
    # match = named_arguments_space(logical_line)
    pass


##############################################################################
# Framework to run all checks
##############################################################################


def message(text):
    """Print a program name and message to stderr."""
    # print >> sys.stderr, options.prog + ': ' + text
    print >> sys.stderr, text


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


def count_parens(line, chars):
    """
    Count parens, but not in strings.
    """
    result = 0
    pos = 0
    while pos < len(line):
        if line[pos] in chars:
            result += 1
        if line[pos] == '"':
            pos += 1
            while line[pos] != '"':
                pos += 1
        if line[pos] == "'":
            pos += 1
            while line[pos] != "'":
                pos += 1
        pos += 1
    return result


def triple_quoted_incomplete(line):
    """
    Test if line is an incomplete triple-quoted string.
    """
    if line.startswith('"""'):
        return line.count('"""') % 2
    if line.startswith("'''"):
        return line.count("'''") % 2
    return False


def indent_strip(line):
    """
    Remove indentation and trailing whitespace.
    Return number of indentation characters and the stripped string.
    """
    line = line.rstrip()
    before = len(line)
    line = line.lstrip()
    after = len(line)
    return before - after, line


def physical_to_logical(physical):
    """
    Convert multi-line statements to single lines.
    """
    logical = []
    line_number = 0
    while line_number < len(physical):
        indent, line = indent_strip(physical[line_number][1])
        mapping = [(0, line_number + 1, indent)]
        while (line.endswith('\\') or
               triple_quoted_incomplete(line) or
               count_parens(line, '([{') > count_parens(line, ')]}')):
            if line.endswith('\\'):
                line = line[-1]
            else:
                line += ' '
            line_number += 1
            indent, next = indent_strip(physical[line_number][1])
            mapping.append((len(line), line_number + 1, indent))
            line += next
        logical.append((mapping, line))
        line_number += 1
    return logical


def find_checks(argument_name):
    checks = []
    function_type = type(find_checks)
    for name, function in globals().iteritems():
        if type(function) is function_type:
            args = inspect.getargspec(function)[0]
            if len(args) >= 1 and args[0] == argument_name:
                checks.append((name, function, args))
    checks.sort()
    return checks


def check_lines(argument_name, lines, filename):
    """
    Run all checks matching argument_name on each line.
    """
    global state
    state = {}
    checks = find_checks(argument_name)
    if options.verbose > 1:
        message(' '.join(map(lambda x: x[0], checks)))
    for location, line in lines:
        for name, check, args in checks:
            if len(args) == 1:
                result = check(line)
            elif len(args) == 2 and args[1] == 'indent':
                result = check(line, location[0][2])
            if result is not None:
                offset, text = result
                if type(location) is int:
                    line_number = location
                else:
                    merged_offset = offset
                    for start_offset, original_number, indent in location:
                        if merged_offset >= start_offset:
                            offset = merged_offset - start_offset
                            line_number = original_number
                message("%s:%s:%d: %s" %
                        (filename, line_number, offset + 1, text))


def input_file(filename):
    """
    Run all checks on a Python source file.
    """
    if options.verbose:
        message('checking ' + filename)
    physical = load(filename)
    check_lines('physical_line', physical, filename)
    logical = physical_to_logical(physical)
    check_lines('logical_line', logical, filename)


def input_dir(dirname):
    """
    Check all Python source files in this directory and all subdirectories.
    """
    for root, dirs, files in os.walk(dirname):
        if options.verbose:
            message('directory ' + root)
        for dirname in options.exclude:
            if dirname in dirs:
                dirs.remove(dirname)
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
    options, args = parser.parse_args()
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
