#: Okay
# https://github.com/python/cpython/issues/90432: fixed in 3.12
def foo():
    pas

\

def bar():
    pass
#: Okay
# new type aliases
type X = int | str
type Y[T] = list[T]
type Z[T: str] = list[T]
#: Okay
# new generics
def f[T](x: T) -> T:
    pass


def g[T: str, U: int](x: T, y: U) -> dict[T, U]:
    pass
#: Okay
# new nested f-strings
f'{
    thing
} {f'{other} {thing}'}'
#: E201:1:4 E202:1:17
f'{ an_error_now }'
#: Okay
f'{x:02x}'
