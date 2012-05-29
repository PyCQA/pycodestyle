#: E126
print "E126", ("visual",
    "hanging")
#: E126
print "E126", ("under-",
              "under-indent")
#: E127
print "E127", ("over-",
                  "over-indent")
#: E124
print "E124", (
"dent")
#: E122
print "E122", (
  "dent")
#: E125
print "E125", (
            "dent")
#: E125
print "E125", (
        "dent")
#: Okay
if (foo == bar and
        baz == frop):
    pass
#: Okay
if (
    foo == bar and
    baz == frop
):
    pass
#: Okay
if start[1] > end_col and not (
        over_indent == 4 and indent_next):
    return(0, "E121 continuation line over-"
           "indented for visual indent")
#: Okay
print "OK", ("visual",
             "indent")
#: E126
# Arguments on first line forbidden when not using vertical alignment
foo = long_function_name(var_one, var_two,
    var_three, var_four)
#: Okay
# Aligned with opening delimiter
foo = long_function_name(var_one, var_two,
                         var_three, var_four)
#: Okay
# Extra indentation is not necessary.
foo = long_function_name(
    var_one, var_two,
    var_three, var_four)
#: E126
print "Okay", ("visual",
               "indent_two"
              )
#: Okay
print "Okay", ("visual",
               "indent_three"
               )
#: E126
print "E126", ("visual",
               "indent_five"
)
#: E121 W291
print "E121", (   
    "bad", "hanging", "close"
    )
#: Okay
print "a-ok", (
    "there",
    "dude",
)
#: Okay
print "hello", (
    "there",
    "dude")
#: Okay
print "hello", (
    "there", "dude")
#: Okay
print "hello", (
    "there", "dude",
)
#: E123
# Further indentation required as indentation is not distinguishable


def long_function_name(
    var_one, var_two, var_three,
    var_four):
    print(var_one)
#: Okay


def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)
#: E122
result = {
   'key1': 'value',
   'key2': 'value',
}
#: E121
result = {
    'foo': [
        'bar', {
            'baz': 'frop',
            }
        ]
    }
#: Okay
result = {
    'foo': [
        'bar', {
            'baz': 'frop',
        }
    ]
}
#: Okay
if bar:
    return(
        start, 'E121 lines starting with a '
        'closing bracket should be indented '
        "to match that of the opening "
        "bracket's line"
    )
#: Okay
# you want vertical alignment, so use a parens
if ((foo.bar("baz") and
     foo.bar("frop")
     )):
    print "yes"

# also ok, but starting to look like LISP
if ((foo.bar("baz") and
     foo.bar("frop"))):
    print "yes"
#: Okay
# print('l.%s\t%s\t%s\t%r' %
#     (token[2][0], pos, tokenize.tok_name[token[0]], token[1]))
print 'l.{line}\t{pos}\t{name}\t{text}'.format(
    line=token[2][0],
    pos=pos,
    name=tokenize.tok_name[token[0]],
    text=repr(token[1]),
)
#: Okay
if os.path.exists(os.path.join(path, PEP8_BIN)):
    cmd = ([os.path.join(path, PEP8_BIN)] +
           self._pep8_options(targetfile))
#: E125
fixed = re.sub(r'\t+', ' ', target[c::-1], 1)[::-1] + \
        target[c + 1:]
#: Okay
fixed = (re.sub(r'\t+', ' ', target[c::-1], 1)[::-1] +
         target[c + 1:])
fixed = (
    re.sub(r'\t+', ' ', target[c::-1], 1)[::-1] +
    target[c + 1:]
)
#: E123
if foo is None and bar is "frop" and \
    blah == 'yeah':
    blah = 'yeahnah'
#: Okay
if foo is None and bar is "frop" and \
        blah == 'yeah':
    blah = 'yeahnah'
#: Okay
"""This is a multi-line
   docstring."""
##: E502
#if (foo is None and bar is "e127" and \
#        blah == 'yeah'):
#    blah = 'yeahnah'
#: Okay
if blah:
    # is this actually readable?  :)
    multiline_literal = """
while True:
    if True:
        1
""".lstrip()
    multiline_literal = (
        """
while True:
    if True:
        1
""".lstrip()
    )
    multiline_literal = (
        """
while True:
    if True:
        1
"""
        .lstrip()
    )
#: Okay
if blah:
    multiline_visual = ("""
while True:
    if True:
        1
"""
                        .lstrip())
