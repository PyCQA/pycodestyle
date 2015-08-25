#: W601 E901:python3
if a.has_key("b"):
    print a
#: W602 E901:python3
raise DummyError, "Message"
#: W602 E901:python3
raise ValueError, "hello %s %s" % (1, 2)
#: E901:python3
raise type_, val, tb
raise Exception, Exception("f"), t
#: W603 E901:python3
if x <> 0:
    x = 0
#: W604 E901:python3
val = `1 + 2`
