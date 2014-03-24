#: E101 W191
for a in 'abc':
    for b in 'xyz':
        print a  # indented with 8 spaces
	print b  # indented with 1 tab
#: Okay
"""The next line starts with <tab> and then <space>
	 but that's fine by pep8
since this is inside a string."""
