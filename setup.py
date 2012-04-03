from setuptools import setup, find_packages

version = '1.0'
long_description = '\n\n'.join([open('README.rst').read(),
                                open('CHANGES.txt').read(),
#                               open('TODO.txt').read(),
                               ])

setup(
    name='pep8',
    version=version,
    description="Python style guide checker",
    long_description=long_description,
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
