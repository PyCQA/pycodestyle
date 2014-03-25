#: E711
if res == None:
    pass
#: E712
if res == True:
    pass
#: E712
if res != False:
    pass

#
#: E713
if not X in Y:
    pass
#: E713
if not X.B in Y:
    pass
#: E713
if not X in Y and Z == "zero":
    pass
#: E713
if X == "zero" or not Y in Z:
    pass

#
#: E714
if not X is Y:
    pass
#: E714
if not X.B is Y:
    pass
#: Okay
if x not in y:
    pass
if not (X in Y or X is Z):
    pass
if not (X in Y):
    pass
if x is not y:
    pass
#:
