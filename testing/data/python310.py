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
    case {"x": 42}:
        pass
    case SomeClass(arg=2):
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
#: E271:2:9 E271:3:9 E271:6:9 E271:7:9 E271:8:9
match var:
    case  (2, 3): pass
    case  (
        2, 3
    ): pass
    case  {"x": 42}: pass
    case  [{"y": 2}, 3]: print()  # comment
    case  "Hello: World": pass
#: E221:6:5 E221:7:5
# Don't emit false-positives
# Only E221 (multiple spaces before operator), not E271!
match: int = 42
case: int = 42
matched = {"true": True, "false": False}
case  = {"x": 42}
case  = "Hello: World"
