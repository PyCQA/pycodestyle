#: Okay
def test():
    good = 1
#: Okay
def test():
    def test2():
        good = 1
#: Okay
GOOD = 1
#: Okay
class Test(object):
    GOOD = 1
#: E805
def test():
    Bad = 1
#: E805
def test():
    VERY = 2
#: E805
def test():
    def test2():
        class Foo(object):
            def test3(self):
                Bad = 3
#: Okay
def good():
    global Bad
    Bad = 1
#: E805
def bad():
    global Bad

    def foo():
        Bad = 1
