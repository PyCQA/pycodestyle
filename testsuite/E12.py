#: E121
print "E121", (
  "dent")
#: E122
print "E122", (
"dent")
#: E123
print "E123", ("visual",
               "indent_two"
              )
#: E124
print "E124", ("visual",
               "indent_five"
)
#: E124
a = (123,
)
#: E125
if (row < 0 or self.moduleCount <= row or
    col < 0 or self.moduleCount <= col):
    raise Exception("%s,%s - %s" % (row, col, self.moduleCount))
#: E126
print "E126", (
            "dent")
#: E126
print "E126", (
        "dent")
#: E127
print "E127", ("over-",
                  "over-indent")
#: E128
print "E128", ("visual",
    "hanging")
#: E128
print "E128", ("under-",
              "under-indent")
#:


#: E123 W291
print "E123", (   
    "bad", "hanging", "close"
    )
#
#: E123
result = {
    'foo': [
        'bar', {
            'baz': 'frop',
            }
        ]
    }
#: E121
result = {
   'key1': 'value',
   'key2': 'value',
}
#: E121
rv.update(dict.fromkeys((
    'qualif_nr', 'reasonComment_en', 'reasonComment_fr',
    'reasonComment_de', 'reasonComment_it'),
          '?'),
          "foo")
#:


#: E125
if foo is None and bar is "frop" and \
    blah == 'yeah':
    blah = 'yeahnah'
#: E125
# Further indentation required as indentation is not distinguishable


def long_function_name(
    var_one, var_two, var_three,
    var_four):
    print(var_one)
#
#: E125


def qualify_by_address(
    self, cr, uid, ids, context=None,
    params_to_check=frozenset(QUALIF_BY_ADDRESS_PARAM)):
    """ This gets called by the web server """
#: E125
if (a == 2 or
    b == "abc def ghi"
    "jkl mno"):
    return True
#:


#: E126
fixed = re.sub(r'\t+', ' ', target[c::-1], 1)[::-1] + \
        target[c + 1:]
#: E126
rv.update(dict.fromkeys((
            'qualif_nr', 'reasonComment_en', 'reasonComment_fr',
            'reasonComment_de', 'reasonComment_it'),
        '?'),
    "foo")
#: E126 E124
eat_a_dict_a_day({
        "foo": "bar",
})
#: E126 E124
if (
    x == (
            3
    ) or
        y == 4):
    pass
#: E126 E124
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


#: E128
# Arguments on first line forbidden when not using vertical alignment
foo = long_function_name(var_one, var_two,
    var_three, var_four)
#
#: E128
print('l.%s\t%s\t%s\t%r' %
    (token[2][0], pos, tokenize.tok_name[token[0]], token[1]))
#: E128


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
