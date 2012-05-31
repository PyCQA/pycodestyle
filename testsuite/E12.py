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
#: E121
print "E121", ("visual",
               "indent_two"
              )
#: E128
print "E128", ("visual",
               "indent_five"
)
#: E128
a = (123,
)
#: E123
if (row < 0 or self.moduleCount <= row or
    col < 0 or self.moduleCount <= col):
    raise Exception("%s,%s - %s" % (row, col, self.moduleCount))
#:


#: E121 W291
print "E121", (   
    "bad", "hanging", "close"
    )
#
#: E121
result = {
    'foo': [
        'bar', {
            'baz': 'frop',
            }
        ]
    }
#: E122
result = {
   'key1': 'value',
   'key2': 'value',
}
#: E122
rv.update(dict.fromkeys((
    'qualif_nr', 'reasonComment_en', 'reasonComment_fr',
    'reasonComment_de', 'reasonComment_it'),
          '?'),
          "foo")
#:


#: E123
if foo is None and bar is "frop" and \
    blah == 'yeah':
    blah = 'yeahnah'
#: E123
# Further indentation required as indentation is not distinguishable


def long_function_name(
    var_one, var_two, var_three,
    var_four):
    print(var_one)
#
#: E123


def qualify_by_address(
    self, cr, uid, ids, context=None,
    params_to_check=frozenset(QUALIF_BY_ADDRESS_PARAM)):
    """ This gets called by the web server """
#: E123
if (a == 2 or
    b == "abc def ghi"
    "jkl mno"):
    return True
#:


#: E125
fixed = re.sub(r'\t+', ' ', target[c::-1], 1)[::-1] + \
        target[c + 1:]
#: E125
rv.update(dict.fromkeys((
            'qualif_nr', 'reasonComment_en', 'reasonComment_fr',
            'reasonComment_de', 'reasonComment_it'),
        '?'),
    "foo")
#: E125 E128
eat_a_dict_a_day({
        "foo": "bar",
})
#: E125 E128
if (
    x == (
            3
    ) or
        y == 4):
    pass
#: E125 E128
if (
    x == (
        3
    ) or
    x == (
            3
    ) or
        y == 4):
    pass
#:


#: E126
# Arguments on first line forbidden when not using vertical alignment
foo = long_function_name(var_one, var_two,
    var_three, var_four)
#
#: E126
print('l.%s\t%s\t%s\t%r' %
    (token[2][0], pos, tokenize.tok_name[token[0]], token[1]))
#: E126


def qualify_by_address(self, cr, uid, ids, context=None,
        params_to_check=frozenset(QUALIF_BY_ADDRESS_PARAM)):
    """ This gets called by the web server """
#:


#: E127
print "hello", (

    "there",
     # "john",
    "dude")
#:
