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
