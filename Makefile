test :
	python pep8.py --testsuite testsuite

selftest :
	python pep8.py --statistics pep8.py

doctest :
	python pep8.py --doctest

alltest : test selftest doctest

multitest :
	python2.5 pep8.py --testsuite testsuite
	python2.6 pep8.py --testsuite testsuite
	python2.7 pep8.py --testsuite testsuite
	python3.1 pep8.py --testsuite testsuite
	python3.2 pep8.py --testsuite testsuite
	python2.5 pep8.py --doctest
	python2.6 pep8.py --doctest
	python2.7 pep8.py --doctest
	python3.1 pep8.py --doctest
	python3.2 pep8.py --doctest
	python2.5 pep8.py --statistics pep8.py
	python2.6 pep8.py --statistics pep8.py
	python2.7 pep8.py --statistics pep8.py
	python3.1 pep8.py --statistics pep8.py
	python3.2 pep8.py --statistics pep8.py
