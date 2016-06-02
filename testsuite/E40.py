#: E401
import os, sys
#: Okay
import os
import sys

from subprocess import Popen, PIPE

from myclass import MyClass
from foo.bar.yourclass import YourClass

import myclass
import foo.bar.yourclass
#: Okay
__all__ = ['abc']

import foo
#: Okay
__version__ = "42"

import foo
#: Okay
__author__ = "Simon Gomizelj"

import foo
#: Okay
try:
    import foo
except ImportError:
    pass
else:
    print('imported foo')
finally:
    print('made attempt to import foo')

import bar
#: E402
VERSION = '1.2.3'

import foo
#: E402
import foo

a = 1

import bar
