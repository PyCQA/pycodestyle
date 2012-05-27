#: E120
print "E120", ("visual",
    "hanging")
#: E120
print "E120", ("under-",
              "under-indent")
#: E121
print "E121", ("over-",
                  "over-indent")
#: E123
print "E123", (
"dent")
#: E124
print "E124", (
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
    return(0, "E115 continuation line over-"
           "indented for visual indent")
#: Okay
print "OK", ("visual",
             "indent")
#: E120
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
#: E120
print "Okay", ("visual",
               "indent_two"
              )
#: Okay
print "Okay", ("visual",
               "indent_three"
               )
#: E120
print "E120", ("visual",
               "indent_five"
)
#: E122 W291
print "E122", (   
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
#: E126
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
#: E124
result = {
   'key1': 'value',
   'key2': 'value',
}
#: E122
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
        start, 'E122 lines starting with a '
        'closing bracket should be indented '
        "to match that of the opening "
        "bracket's line"
    )
