#: Okay
class X:
    pass
#: Okay

def foo():
    pass
#: Okay
# -*- coding: utf-8 -*-
class X:
    pass
#: Okay
# -*- coding: utf-8 -*-
def foo():
    pass
#: Okay
class X:

    def a():
        pass

    # comment
    def b():
        pass

    # This is a
    # ... multi-line comment

    def c():
        pass


# This is a
# ... multi-line comment

@some_decorator
class Y:

    def a():
        pass

    # comment

    def b():
        pass

    @property
    def c():
        pass


try:
    from nonexistent import Bar
except ImportError:
    class Bar(object):
        """This is a Bar replacement"""


def with_feature(f):
    """Some decorator"""
    wrapper = f
    if has_this_feature(f):
        def wrapper(*args):
            call_feature(args[0])
            return f(*args)
    return wrapper


try:
    next
except NameError:
    def next(iterator, default):
        for item in iterator:
            return item
        return default


def a():
    pass


class Foo():
    """Class Foo"""

    def b():

        pass


# comment
def c():
    pass


# comment


def d():
    pass

# This is a
# ... multi-line comment

# And this one is
# ... a second paragraph
# ... which spans on 3 lines


# Function `e` is below
# NOTE: Hey this is a testcase

def e():
    pass


def a():
    print

    # comment

    print

    print

# Comment 1

# Comment 2


# Comment 3

def b():

    pass


# Nested functions
def c():
    def d():
        pass
    def f():
        pass
    @decorated
    def g():
        pass
    def h():
        pass


# Function nested in a method
class Foo(object):
    def foo(self):
        def bar():
            pass
        def bar2():
            pass
        @decorated
        def bar3():
            pass
        def bar4():
            pass

    def bar(self):
        pass


# Class nested in a function
def foo():
    class A(object):
        def a(self):
            pass
        def b(self):
            pass
        @decorated
        def c(self):
            pass
        def d(self):
            pass
    class B(object):
        def c(self):
            pass
