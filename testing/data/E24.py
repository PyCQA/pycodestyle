#: E241
a = (1,  2)
#: Okay
b = (1, 20)
#: E242
a = (1,	2)  # tab before 2
#: Okay
b = (1, 20)  # space before 20
#: E241 E241 E241
# issue 135
more_spaces = [a,    b,
               ef,  +h,
               c,   -d]
#: E243:1:5
spam .eggs
#: E243:1:6
spam. eggs
#: E243:1:5 E243:1:7
spam . eggs
#: Okay
spam.eggs
#: Okay
from . import eggs
from ..spam import eggs
#: Okay
(
    spam
    .eggs
)
