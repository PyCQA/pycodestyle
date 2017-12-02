#: Okay
def okay_a(x):
    if x:
        return 1
    else:
        return 2
#: Okay
def okay_b(x):
    if x:
        x += 1
        return
    z.append(x)
    return
#: E750:5:9
def not_okay_a():
    if True:
        return None
    else:
        return
#: Okay
def okay_nested_a():
    def f():
        if 1:
            return
        else:
            return
    return f
#: Okay
def okay_nested_b():
    def f():
        if 1:
            return 3
        else:
            return 4
    return
#: E750:6:5
def not_okay_nested_a(x):
    def f():
        return
    if not x:
        return
    return f
#: E750:6:13
def not_okay_nested_b():
    def f():
        if 1:
            return 3
        else:
            return
    return
