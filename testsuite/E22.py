#: E221
a = 12 + 3
b = 4  + 5
#: E221
x             = 1
y             = 2
long_variable = 3
#: E221
x[0]          = 1
x[1]          = 2
long_variable = 3
#: E221
x = f(x)          + 1
y = long_variable + 2
z = x[0]          + 3
#: Okay
x = 1
y = 2
long_variable = 3
#:


#: E222
a = a +  1
b = b + 10
#: E222
x =            -1
y =            -2
long_variable = 3
#: E222
x[0] =          1
x[1] =          2
long_variable = 3
#:


#: E223
foobart = 4
a	= 3  # aligned with tab
#:


#: E224
a +=	1
b += 1000
#:


#: E225
i=i+1
#: E225
submitted +=1
#: E225
x = x*2 - 1
#: E225
hypot2 = x*x + y*y
#: E225
c = (a+b) * (a-b)
#: E225
c = (a + b)*(a - b)
#: E225
c = (a +b)*(a - b)
#: E225
c =-1
#: E225
c = alpha -4
#: E225
z = (x + 1) **y
#: E225
norman = True+False
#: E225
_1MB = 2 ** 20
_1kB = _1MB >>10
#:
#: Okay
i = i + 1
submitted += 1
x = x * 2 - 1
hypot2 = x * x + y * y
c = (a + b) * (a - b)
foo(bar, key='word', *args, **kwargs)
baz(**kwargs)
negative = -1
spam(-1)
-negative
lambda *args, **kw: (args, kw)
lambda a, b=h[:], c=0: (a, b, c)
if not -5 < x < +5:
    print >>sys.stderr, "x is out of range."
print >> sys.stdout, "x is an integer."

if True:
    *a, b = (1, 2, 3)
#:
