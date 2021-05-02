var, var2 = 1, 2
#: Okay
match (var, var2):
    #: Okay
    case [2, 3]:
        pass
    #: Okay
    case (1, 2):
        pass
    #: Okay
    case _:
        print("Default")
