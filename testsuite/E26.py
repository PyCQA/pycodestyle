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
#: Okay
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
