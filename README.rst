==========
PyInvaders
==========

A recreation of the classic arcade game "Space Invaders" using the PyGame library.


**************
Project set up
**************
The project uses pipenv as a higher level packaging tool (see: https://docs.pipenv.org/ ).
To install dependencies for Python 3.5.2 using a virtualenv (see: https://virtualenv.pypa.io/en/stable/ ), using the PyCharm IDE:

1. Use command line tool with administrator privileges:
::
    $ pip install pipenv

2. Now open the directory with PyCharm and use a new virtual enviroment as interpreter (see: https://www.jetbrains.com/help/pycharm-edu/creating-virtual-environment.html ).

3. Use pyCharms terminal, and install dependencies:
::
    $ (venv) pipenv install

Pipenv now will install the projects dependencies to the virtualenv based on the information in Pipfile.

4. In PyCharm setting -> project structure mark the src folder as Sources.

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
