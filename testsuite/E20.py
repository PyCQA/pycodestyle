#: E201
spam( ham[1], {eggs: 2})
#: E201
spam(ham[ 1], {eggs: 2})
#: E201
spam(ham[1], { eggs: 2})
#: Okay
spam(ham[1], {eggs: 2})
#:


#: E202
spam(ham[1], {eggs: 2} )
#: E202
spam(ham[1], {eggs: 2 })
#: E202
spam(ham[1 ], {eggs: 2})
#: Okay
spam(ham[1], {eggs: 2})

result = func(
    arg1='some value',
    arg2='another value',
)

result = func(
    arg1='some value',
    arg2='another value'
)

result = [
    item for item in items
    if item > 5
]
#:


#: E203
if x == 4 :
    print x, y
    x, y = y, x
#: E203 E702
if x == 4:
    print x, y ; x, y = y, x
#: E203
if x == 4:
    print x, y
    x, y = y , x
#: Okay
if x == 4:
    print x, y
    x, y = y, x
a[b1, :] == a[b1, ...]
b = a[:, b1]
#:
