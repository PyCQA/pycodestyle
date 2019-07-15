#: E231
a = (1,2)
#: E231
a[b1,:]
#: E231
a = [{'a':''}]
#: E231
a = [{'a': '', 'b':''}]
#: E231
a = [{'a': a['a'], 'b':''}]
#: E231
a = [{'a': a[3:], 'b':''}]
#: Okay
a = (4,)
b = (5, )
c = {'text': text[5:]}
d = {'text': '', 'text2': text[5:]}
e = {'text': '', 'text2': text[5:6]}

result = {
    'key1': 'value',
    'key2': 'value',
}
