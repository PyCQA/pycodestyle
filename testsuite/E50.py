#: E501
a = '12345678901234567890123456789012345678901234567890123456789012345678901234567890'
#: E502
a = ('123456789012345678901234567890123456789012345678901234567890123456789'  \
     '01234567890')
#: E502
a = ('AAA  \
      BBB' \
     'CCC')
#
#: Okay
a = ('AAA'
     'BBB')

a = ('AAA  \
      BBB'
     'CCC')

a = 'AAA'    \
    'BBB'    \
    'CCC'

a = ('AAA\
BBBBBBBBB\
CCCCCCCCC\
DDDDDDDDD')
#
#: Okay
if aaa:
    pass
elif bbb or \
        ccc:
    pass

ddd = \
    ccc
