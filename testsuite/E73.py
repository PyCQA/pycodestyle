#: E731:1:1
f = lambda x: 2 * x
#: E731:1:1 E226:1:16
f = lambda x: 2*x
#: E731:2:5
while False:
    this = lambda y, z: 2 * x
#: Okay
f = object()
f.method = lambda: 'Method'
#: Okay
f = {}
f['a'] = lambda x: x ** 2
#: Okay
f = []
f.append(lambda x: x ** 2)
#: Okay
lambda: 'no-op'
