#: E901
= [x
#: E901 E101 W191
while True:
    try:
	    pass
	except:
		print 'Whoops'
#: Okay

# Issue #119
# Do not crash with Python2 if the line endswith '\r\r\n'
EMPTY_SET = set()
SET_TYPE = type(EMPTY_SET)
toto = 0 + 0
#:
