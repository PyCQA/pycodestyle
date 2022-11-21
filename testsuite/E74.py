#: E741:1:8
lambda l: dict(zip(l, range(len(l))))
#: E741:1:7 E704:1:1
def f(l): print(l, l, l)
#: E741:2:12
x = (
    lambda l: dict(zip(l, range(len(l)))),
)
#: E741:2:12 E741:3:12
x = (
    lambda l: dict(zip(l, range(len(l)))),
    lambda l: dict(zip(l, range(len(l)))),
)
