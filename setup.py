from setuptools import setup, find_packages

version = '0.4'
long_description = '\n\n'.join([open('README.rst').read(),
                                open('CHANGES.txt').read(),
                                open('TODO.txt').read()])

setup(name='pep8',
      version=version,
      description="Python style guide checker",
      long_description=long_description,
      classifiers=[],
      keywords='pep8',
      author='Johann C. Rocholl',
      author_email='johann@browsershots.org',
      url='http://github.com/cburroughs/pep8.py/tree/master',
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
      )
