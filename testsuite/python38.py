#: Okay
def f1(a, /, b):
    pass


def f2(a, b, /):
    pass


def f3(
        a,
        /,
        b,
):
    pass


lambda a, /: None
#: Okay
if x := 1:
    print(x)
if m and (token := m.group(1)):
    pass
stuff = [[y := f(x), x / y] for x in range(5)]
#: E225:1:5
if x:= 1:
    pass
#: E225:1:18
if False or (x :=1):
    pass
#: Okay
import typing as t

__all__: t.List[str] = []

import logging

logging.getLogger(__name__)
#: E402
import typing as t

all_the_things: t.List[str] = []

import logging
#: E221:1:5 E222:1:9 E221:3:6
if x  :=  1:
    pass
if (x  := 2):
    pass
#: E223:1:5 E224:1:8
if x	:=	2:
    pass
#: E221:1:6 E221:1:19
if (x  := 1) == (y  := 2):
    pass
