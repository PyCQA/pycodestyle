#: Okay
var, var2 = 1, 2
match (var, var2):
    case [2, 3]:
        pass
    case (1, 2):
        pass
    case _:
        print("Default")
