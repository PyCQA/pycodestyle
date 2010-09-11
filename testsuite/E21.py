#: E211
spam (1)
#: E211
dict ['key'] = list [index]
#: E211
dict['key'] ['subkey'] = list[index]
#: E225
def squares(n):
    return (i**2 for i in range(n))
#: Okay
spam(1)
dict['key'] = list[index]


# This is not prohibited by PEP8, but avoid it.
class Foo (Bar, Baz):
    pass
