#: Okay
var, var2 = 1, 2
match (var, var2):
    case [2, 3]:
        pass
    case (1, 2):
        pass
    case _:
        print("Default")
#: Okay
var = 0, 1, 2
match var:
    case *_, 1, 2:
        pass
    case 0, *_, 2:
        pass
    case 0, 1, *_:
        pass
    case (*_, 1, 2):
        pass
    case (0, *_, 2):
        pass
    case (0, 1, *_):
        pass
