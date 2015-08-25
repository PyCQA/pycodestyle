# Test suite to work on issue https://github.com/PyCQA/pep8/issues/399
import math
import itertools

# Code examples from GvR
# https://mail.python.org/pipermail/python-dev/2015-April/139054.html

# Correct ###


def foo_ok(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return None


def bar_ok(x):
    if x < 0:
        return None
    return math.sqrt(x)


def foobar_ok(x):
    if True:
        return None
    else:
        pass


# Not correct ###
#: W741:1:1
def foo_ko(x):
    if x >= 0:
        return math.sqrt(x)
#: W740:3:9
def bar_ko(x):
    if x < 0:
        return
    return math.sqrt(x)

# More examples for the sake of testings

# Correct ###


def foo_ok(x):
    if x >= 0:
        return math.sqrt(x)
    elif x == 0:
        return 0
    else:
        return None


def goldbach_conjecture_ok():
    for i in itertools.count(2):
        if not can_be_expressed_as_prime_sum(i):
            return i
    assert not True


def outer_function():

    def nested_function():
        return 6 * 9

    print(42 == nested_function())
    return
# Not correct ###
#: W741:1:1
def foo_ko(x):
    if x >= 0:
        return math.sqrt(x)
    elif x == 0:
        return 0
#: W741:1:1
def goldbach_conjecture_ko():
    for i in itertools.count(2):
        if not can_be_expressed_as_prime_sum(i):
            return i


# W741:1:1
def return_finally1():  # return 1
    try:
        return 1
    finally:
        pass
#: W740:5:9
def return_finally2():  # return None
    try:
        return 2
    finally:
        return
#: W740:3:9
def return_finally3():  # return 4
    try:
        return
    finally:
        return 4
