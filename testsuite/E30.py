#: E301:5:5
class X:

    def a():
        pass
    def b():
        pass
#: E301:6:5
class X:

    def a():
        pass
    # comment
    def b():
        pass
#:


#: E302:3:1
#!python
# -*- coding: utf-8 -*-
def a():
    pass
#: E302:2:1
"""Main module."""
def _main():
    pass
#: E302:2:1
import sys
def get_sys_path():
    return sys.path
#: E302:4:1
def a():
    pass

def b():
    pass
#: E302:6:1
def a():
    pass

# comment

def b():
    pass
#:


#: E303:5:1
print



print
#: E303:5:1
print



# comment

print
#: E303:5:5 E303:8:5
def a():
    print


    # comment


    # another comment

    print
#:


#: E304:3:1
@decorator

def function():
    pass
#: E303:5:1
#!python



"""This class docstring comes on line 5.
It gives error E303: too many blank lines (3)
"""
#:
