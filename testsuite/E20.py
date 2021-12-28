#: E201:1:6
spam( ham[1], {eggs: 2})
#: E201:1:10
spam(ham[ 1], {eggs: 2})
#: E201:1:15
spam(ham[1], { eggs: 2})
#: E201:1:6
spam(	ham[1], {eggs: 2})
#: E201:1:10
spam(ham[	1], {eggs: 2})
#: E201:1:15
spam(ham[1], {	eggs: 2})
#: Okay
spam(ham[1], {eggs: 2})
#:


#: E202:1:23
spam(ham[1], {eggs: 2} )
#: E202:1:22
spam(ham[1], {eggs: 2 })
#: E202:1:11
spam(ham[1 ], {eggs: 2})
#: E202:1:23
spam(ham[1], {eggs: 2}	)
#: E202:1:22
spam(ham[1], {eggs: 2	})
#: E202:1:11
spam(ham[1	], {eggs: 2})
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


#: E203:1:10
if x == 4 :
    print x, y
    x, y = y, x
#: E203:1:10
if x == 4	:
    print x, y
    x, y = y, x
#: E203:2:15 E702:2:16
if x == 4:
    print x, y ; x, y = y, x
#: E203:2:15 E702:2:16
if x == 4:
    print x, y	; x, y = y, x
#: E203:3:13
if x == 4:
    print x, y
    x, y = y , x
#: E203:3:13
if x == 4:
    print x, y
    x, y = y	, x
#: E203:1:20
ham[lower + offset  : upper + offset]
#: E203:1:12
ham[lower : : upper]
#: E203:1:14
ham[(lambda x : x)(5) :]
#: E203:1:9
ham[{"a" : 6}["a"] :]
#: E203:1:38
ham[{"a": [1, {}, {"a": [{}, []], "b" :[3]}, 3][1 : 3]}["a"] :]
#: Okay
if x == 4:
    print x, y
    x, y = y, x
a[b1, :] == a[b1, ...]
b = a[:, b1]
ham[1:9], ham[1:9:3], ham[:9:3], ham[1::3], ham[1:9:]
ham[lower:upper], ham[lower:upper:], ham[lower::step]
ham[: upper_fn(x) : step_fn(x)], ham[:: step_fn(x)]
ham[{"a": [1, {}, {"a": [{}, []], "b": [3]}, 3][1 : 3]}["a"] :]
append_leaves(
    new_line, line, LL[string_idx + 1 : rpar_idx] + LL[rpar_idx + 1 :]
)
if token.PERCENT in {leaf.type for leaf in LL[idx - 1 : next_idx]}
#:
