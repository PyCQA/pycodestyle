# -*- coding: utf-8 -*-
from __future__ import with_statement
from setuptools import setup


def get_version():
    with open('pycodestyle.py') as f:
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
    name='pycodestyle',
    version=get_version(),
    description="Python style guide checker",
    long_description=get_long_description(),
    keywords='pycodestyle, pep8, PEP 8, PEP-8, PEP8',
    author='Johann C. Rocholl',
    author_email='johann@rocholl.net',
    maintainer='Ian Lee',
    maintainer_email='IanLee1521@gmail.com',
    url='https://pycodestyle.readthedocs.io/',
    license='Expat license',
    py_modules=['pycodestyle'],
    namespace_packages=[],
    include_package_data=True,
    zip_safe=False,
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
    install_requires=[
        # Broken with Python 3: https://github.com/pypa/pip/issues/650
        # 'setuptools',
    ],
    entry_points={
        'console_scripts': [
            'pycodestyle = pycodestyle:_main',
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
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    test_suite='testsuite.test_all.suite',
)
