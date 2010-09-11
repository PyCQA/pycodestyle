#: E251
def foo(bar = False):
    '''Test function with an error in declaration'''
    pass
#: E251
foo(bar= True)
#: E251
foo(bar =True)
#: E251
foo(bar = True)
#: Okay
foo(bar=(1 == 1))
foo(bar=(1 != 1))
foo(bar=(1 >= 1))
foo(bar=(1 <= 1))
