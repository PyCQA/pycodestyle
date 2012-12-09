#: Okay
def b1():
    pass
#: Okay
def b2(a):
    pass
#: Okay
def b3(a, b, c, d):
    pass
#: Okay
def b4(a, b, c, *fuck):
    pass
#: Okay
def b5(*fuck):
    pass
#: Okay
def b6(a, b, c, **kwargs):
    pass
#: Okay
def b7(**kwargs):
    pass
#: Okay
def b8(*args, **kwargs):
    pass
#: Okay
def b9(a, b, c, *args, **kwargs):
    pass
#: Okay
def b10(a, b, c=3, d=4, *args, **kwargs):
    pass
#: E802
def b11(**BAD):
    pass
#: E802
def b12(*BAD):
    pass
#: E802
def b13(BAD, *VERYBAD, **EXTRABAD):
    pass
#: E802
def b14(BAD):
    pass
#: E802 E802
class Test(object):
    def __init__(self, BAD):
        pass

    @classmethod
    def test(cls, BAD):
        pass
