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
#: E271:2:6 E271:3:9 E271:5:9 E271:7:9
var = 1
match  var:
    case  1:
        pass
    case	2:
        pass
    case  (
        3
    ):
        pass
#: E275:2:6 E275:3:9 E275:5:9
var = 1
match(var):
    case(1):
        pass
    case_:
        pass
