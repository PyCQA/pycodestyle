#: W601
if a.has_key("b"):
    print a
#: W602
raise DummyError, "Message"
#: W602
raise ValueError, "hello %s %s" % (1, 2)
#: Okay
raise type_, val, tb
raise Exception, Exception("f"), t
#: W603
if x <> 0:
    x = 0
#: W604
val = `1 + 2`
#: W605
regex = '\.png$'
#: W605
regex = '''
\.png$
'''
#: Okay
regex = r'\.png$'
regex = '\\.png$'
regex = r'''
\.png$
'''
regex = r'''
\\.png$
'''
s = '\\'
#: W606
async = 42
#: W606
await = 42
#: W606
def async():
    pass
#: W606
def await():
    pass
#: W606
class async:
    pass
#: W606
class await:
    pass
#: Okay
async def read_data(db):
    data = await db.fetch('SELECT ...')
#: Okay
if await fut:
    pass
if (await fut):
    pass
if await fut + 1:
    pass
if (await fut) + 1:
    pass
pair = await fut, 'spam'
pair = (await fut), 'spam'
with await fut, open():
    pass
with (await fut), open():
    pass
await foo()['spam'].baz()()
return await coro()
return (await coro())
res = await coro() ** 2
res = (await coro()) ** 2
func(a1=await coro(), a2=0)
func(a1=(await coro()), a2=0)
await foo() + await bar()
(await foo()) + (await bar())
-await foo()
-(await foo())
