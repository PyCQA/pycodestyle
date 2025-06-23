type Alias[T: (int, str) = str] = list[T]
type Alias2[T = str] = list[T]


class C[T: (int, str) = str]:
    pass


class C2[T = str]:
    pass


class C3[T, U: str = str]:
    pass


def f[T: (int, str) = str](t: T) -> T:
    pass


def f2[T = str](t: T) -> T:
    pass
