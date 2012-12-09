# python3 only
#: Okay
def compare(a, b, *, key=None):
    pass
#: E802
def compare(a, b, *, BAD=None):
    pass
#: E802
def compare(a, b, *VERY, bad=None):
    pass
#: E802
def compare(a, b, *ok, fine=None, **BAD):
    pass
