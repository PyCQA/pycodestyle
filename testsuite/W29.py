#: Okay
# 情
#: W291
print 
#: Okay
"""this is a multi-line string
trailing whilespace here  
"""
#: Okay
"""trailing whitespace here 
and on the following line
    
"""
#: W291
"""trailing whitespace not allowed after the string""" 
#: W293
class Foo(object):
    
    bang = 12
#: W292
# This line doesn't have a linefeed