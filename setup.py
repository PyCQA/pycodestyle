from setuptools import setup, find_packages


def get_version():
    f = open('pep8.py')
    try:
        for line in f:
            if line.startswith('__version__'):
                return eval(line.split('=')[-1])
    finally:
        f.close()


def get_long_description():
    descr = []
    for fname in 'README.rst', 'CHANGES.txt':   # , 'TODO.txt'
        f = open(fname)
        try:
            descr.append(f.read())
        finally:
            f.close()
    return '\n\n'.join(descr)


setup(
    name='pep8',
    version=get_version(),
    description="Python style guide checker",
    long_description=get_long_description(),
    keywords='pep8',
    author='Johann C. Rocholl',
    author_email='johann@rocholl.net',
    url='http://github.com/jcrocholl/pep8',
    license='Expat license',
    py_modules=['pep8'],
    namespace_packages=[],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        # -*- Extra requirements: -*-
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
)
