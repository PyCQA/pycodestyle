#: E211
spam (1)
#: E211 E211
dict ['key'] = list [index]
#: E211
dict['key'] ['subkey'] = list[index]
#: Okay
spam(1)
dict['key'] = list[index]
#: E211
print ('abc')
#: Okay
print('abc')
#: Okay
from __future__ import print_function
print ('abc')


# This is not prohibited by PEP8, but avoid it.
class Foo (Bar, Baz):
    pass
