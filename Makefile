release:
	umask 022 && chmod -R a+rX . && python setup.py sdist bdist_wheel
	# twine upload dist/*

test:
	tox
