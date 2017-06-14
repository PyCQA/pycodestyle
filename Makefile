release:
	umask 022 && chmod -R a+rX . && python setup.py sdist bdist_wheel

test :
	python pycodestyle.py --testsuite testsuite

selftest :
	python pycodestyle.py --statistics pycodestyle.py

doctest :
	python pycodestyle.py --doctest

unittest :
	python -m testsuite.test_all

alltest : test selftest doctest unittest
