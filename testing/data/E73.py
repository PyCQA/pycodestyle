#: E731:1:1
f = lambda x: 2 * x
#: E731:1:1
f = (  # some long comment that forces this to be on a new line
    lambda x: 731 * x
)
#: E731:1:1 E226:1:16
f = lambda x: 2*x
#: E731:2:5
while False:
    this = lambda y, z: 2 * x
#: Okay
f = object()
f.method = lambda: 'Method'

f = (lambda o: o.lower()) if isinstance('a', str) else (lambda o: o)

f = (
    lambda o: o.lower(),
    lambda o: o.upper(),
)

f = {}
f['a'] = lambda x: x ** 2

f = []
f.append(lambda x: x ** 2)

lambda: 'no-op'
