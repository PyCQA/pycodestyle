test :
	python pycodestyle.py --testsuite testsuite

selftest :
	python pycodestyle.py --statistics pycodestyle.py

doctest :
	python pycodestyle.py --doctest

unittest :
	python -m testsuite.test_all

alltest : test selftest doctest unittest
