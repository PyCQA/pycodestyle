#: E721
if type(res) == type(42):
    pass
#: E721
if type(res) != type(""):
    pass
#: E721
import types

if res == types.IntType:
    pass
#: E721
import types

if type(res) is not types.ListType:
    pass
#: Okay
import types

if isinstance(res, int):
    pass
if isinstance(res, str):
    pass
if isinstance(res, types.MethodType):
    pass
if type(a) != type(b) or type(a) == type(ccc):
    pass
