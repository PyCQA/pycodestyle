#: Okay
try:
    ...
except* OSError as e:
    pass
#: Okay
from typing import Generic
from typing import TypeVarTuple


Ts = TypeVarTuple('Ts')


class Shape(Generic[*Ts]):
    pass


def f(*args: *Ts) -> None:
    ...


def g(x: Shape[*Ts]) -> Shape[*Ts]:
    ...
