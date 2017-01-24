#!/usr/bin/env python3
from typing import ClassVar, List


# Annotated function (Issue #29)
def foo(x: int) -> int:
    return x + 1


# Annotated variables #575
CONST: int = 42


class Class:
    cls_var: ClassVar[str]

    def m(self):
        xs: List[int] = []
