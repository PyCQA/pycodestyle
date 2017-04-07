#!/usr/bin/env python3
from typing import ClassVar, List


# Annotated function (Issue #29)
def foo(x: int) -> int:
    return x + 1


# Annotated variables #575
CONST: int = 42


class Class:
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
    For_var: ClassVar[str]
    While_var: ClassVar[str]
    Def_var: ClassVar[str]
    If_var: ClassVar[str]
    Elif_var: ClassVar[str]
    Else_var: ClassVar[str]
    Try_var: ClassVar[str]
    Except_var: ClassVar[str]
    Finally_var: ClassVar[str]
    With_var: ClassVar[str]
        
    def m(self):
        xs: List[int] = []
