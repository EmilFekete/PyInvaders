==========
PyInvaders
==========

A recreation of the classic arcade game "Space Invaders" using the PyGame library.


**************
Project set up
**************
The project uses pipenv as a higher level packaging tool (see: https://docs.pipenv.org/ ).
To install dependencies for Python 3.5.2, using the PyCharm IDE on Windows:

1. Use command line tool with administrator privileges:
::
    $ pip install pipenv

2. Now set up the enviroment variable PIPENV_VENV_IN_PROJECT so that the virtual env will be located inside the project:
::
    $ set PIPENV_VENV_IN_PROJECT=true

3. Navigate to project directory, and install dependencies:
::
    $ pipenv install

Pipenv now will configure a virtualenv (see: https://virtualenv.pypa.io/en/stable/ ), and install the projects dependencies based on the information in "Pipfile" (managed automatically).

4. Inside PyCharm set up the project interpreter to use the created venv (.\.venv\Scripts\python.exe).

5. Now you should be able to run main.py.

***********************
Contribution guidelines
***********************
1. The commits should be flagged with the type of the code change:
::
    [f] - (feature) if you added a new feature
    [m] - (modification) something that changed currently existing behaviour
    [b] - (bug fix) very small changes, so the feature now works as intended.
    [r] - (refactor) small changes in code structure, naming etc.

2. The commits should also be flagged with an affected area to help others, to pinpoint where, the changes took place.
This should not be the concrete files that had changed, but the abstract part of the program it effects.

Commit message example:
::
    [r][Constants] Refactored constant names to follow PEP8 coding conventions.

**********
Coding Style
**********

1. Typically each class should have their separate python file.
2. The package structure of the test files should mirror the source package structure.
3. Each file should have their own test with the same name and a "_test" suffix.
4. Please follow the PEP8 style conventions (see: https://www.python.org/dev/peps/pep-0008/ ).
