#: E301
class X:

    def a():
        pass
    def b():
        pass
#: E301
class X:

    def a():
        pass
    # comment
    def b():
        pass
#:


#: E302
#!python
# -*- coding: utf-8 -*-
def a():
    pass
#: E302
"""Main module."""
def _main():
    pass
#: E302
import sys
def get_sys_path():
    return sys.path
#: E302
def a():
    pass

def b():
    pass
#: E302
def a():
    pass

# comment

def b():
    pass
#:


#: E303
print



print
#: E303
print



# comment

print
#: E303
def a():
    print


    # comment

    print
#:


#: E304
@decorator

def function():
    pass
#:
