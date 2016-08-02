Contributing to pycodestyle
===========================

When contributing to pycodestyle, please observe our `Code of Conduct`_.

Step 1: Forking pycodestyle for editing
---------------------------------------

Fork the pycodestyle repository on GitHub. This will add
pycodestyle to your GitHub account. You will push your changes to your
fork and then make pull requests into the official pycodestyle repository.

GitHub has an excellent `guide`_ that has screenshots on how to do this.

Next, clone your fork of the pycodestyle repository to your system for
editing::

    $ git clone https://www.github.com/<your_username>/pycodestyle

Now you have a copy of the pycodestyle codebase that is almost ready for
edits.  Next we will setup `virtualenv`_ which will help create an isolated
environment to manage dependancies.


Step 2: Use virtualenv when developing
--------------------------------------

`virtualenv`_ is a tool to create isolated python environments.
First, install virtualenv with::

    $ pip install virtualenv

Next, ``cd`` to the pycodestyle repository that you cloned earlier and
create, then activate a virtualenv::

    $ cd pycodestyle
    $ virtualenv pycodestyle-venv
    $ source pycodestyle-venv/bin/activate

Now you can install the pycodestyle requirements::

    $ pip install -r dev-requirements.txt

To deactivate the virtualenv you can type::

    $ deactivate

For more information see `virtualenv`_'s documentation.


Step 3: Run tests
-----------------

Before creating a pull request you should run the tests to make sure that the
changes that have been made haven't caused any regressions in functionality.
To run the tests, the core developer team and Travis-CI use `tox`_::

    $ pip install -r dev-requirements.txt
    $ tox

All the tests should pass for all available interpreters, with the summary of::

    congratulations :)

At this point you can create a pull request back to the official pycodestyles
repository for review! For more information on how to make a pull request,
GitHub has an excellent `guide`_.

.. _virtualenv: http://docs.python-guide.org/en/latest/dev/virtualenvs/
.. _guide: https://guides.github.com/activities/forking/
.. _tox: https://tox.readthedocs.io/en/latest/
.. _Code of Conduct: http://meta.pycqa.org/en/latest/code-of-conduct.html
