#: Okay
# silence E501
url = 'https://api.github.com/repos/sigmavirus24/Todo.txt-python/branches/master?client_id=xxxxxxxxxxxxxxxxxxxxxxxxxxxx&?client_secret=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'  # noqa

# silence E128
from functools import (partial, reduce, wraps,  # noqa
    cmp_to_key)

from functools import (partial, reduce, wraps,
    cmp_to_key)   # noqa

a = 1
if a == None:   # noqa
    pass
#:


#: Okay
a = [
     1,  2,  3,     # noqa: E241
    10, 20, 30      # noqa: E241
]
#:

# Still reported as error by default if noqa not added
#: E126 E131 E241 E241
b = [
     1,  2,  3,
    10, 20, 30
]
#:
