#!/usr/bin/env python3
from typing import ClassVar, List


# Annotated function (Issue #29)
def foo(x: int) -> int:
    return x + 1


# Annotated variables #575
CONST: int = 42


class Class:
    # Camel-caes
    cls_var: ClassVar[str]
    for_var: ClassVar[str]
    while_var: ClassVar[str]
    def_var: ClassVar[str]
    if_var: ClassVar[str]
    elif_var: ClassVar[str]
    else_var: ClassVar[str]
    try_var: ClassVar[str]
    except_var: ClassVar[str]
    finally_var: ClassVar[str]
    with_var: ClassVar[str]
    forVar: ClassVar[str]
    whileVar: ClassVar[str]
    defVar: ClassVar[str]
    ifVar: ClassVar[str]
    elifVar: ClassVar[str]
    elseVar: ClassVar[str]
    tryVar: ClassVar[str]
    exceptVar: ClassVar[str]
    finallyVar: ClassVar[str]
    withVar: ClassVar[str]

    def m(self):
        xs: List[int] = []
