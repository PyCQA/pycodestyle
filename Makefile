test :
	python pep8.py --testsuite testsuite

multitest :
	python2.4 pep8.py --testsuite testsuite
	python2.5 pep8.py --testsuite testsuite
	python2.6 pep8.py --testsuite testsuite

selftest :
	python pep8.py --repeat pep8.py


doctest :
	python pep8.py --doctest
