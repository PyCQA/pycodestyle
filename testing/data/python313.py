type Alias[T: (int, str) = str] = list[T]


class C[T: (int, str) = str]:
    pass


def f[T: (int, str) = str](t: T) -> T:
    pass
