#: E261
pass # an inline comment
#: E262
x = x + 1  #Increment x
#: E262
x = x + 1  #  Increment x
#: E262
x = y + 1  #:  Increment x
#: E265
#Block comment
a = 1
#: E265
m = 42
#! This is important
mx = 42 - 42
#: Okay
#!/usr/bin/env python

pass  # an inline comment
x = x + 1   # Increment x
y = y + 1   #: Increment x

# Block comment
a = 1

# Block comment1

# Block comment2
aaa = 1


# example of docstring (not parsed)
def oof():
    """
    #foo not parsed
    """
