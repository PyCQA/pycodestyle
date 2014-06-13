# -*- coding: utf-8 -*-
from __future__ import with_statement
from setuptools import setup


def get_version():
    with open('pep8.py') as f:
        for line in f:
            if line.startswith('__version__'):
                return eval(line.split('=')[-1])


def get_long_description():
    descr = []
    for fname in 'README.rst', 'CHANGES.txt':
        with open(fname) as f:
            descr.append(f.read())
    return '\n\n'.join(descr)


setup(
    name='pep8',
    version=get_version(),
    description="Python style guide checker",
    long_description=get_long_description(),
    keywords='pep8',
    author='Johann C. Rocholl',
    author_email='johann@rocholl.net',
    url='http://pep8.readthedocs.org/',
    license='Expat license',
    py_modules=['pep8'],
    namespace_packages=[],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # Broken with Python 3: https://github.com/pypa/pip/issues/650
        # 'setuptools',
    ],
    entry_points={
        'console_scripts': [
            'pep8 = pep8:_main',
        ],
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    test_suite='testsuite.test_all.suite',
)
