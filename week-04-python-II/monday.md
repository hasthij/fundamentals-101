A module, is a set of tools used by your code using import
example: import math

import methods:
1) as alias : import pyautogui as pag
2) one submodule from the main library: from math import pi
3) standard import: import math

writing your own modules
you have two files(if one is a library and one is uses the library)
file 1: main.py
file 2: exlib.py

naming rules for module files
1)don't name after a already existing module
2)file names must be valid python names
3)importing runs the code once

__name__, is a hidden variabl in any module used to find how the module is imported, either run directly, or an import from a file
__name__ = "__main__" run directly
__name__ = "<module name>"

names with double underscores are called dunder names

__init__ is a file that tells python to teach the modules as a one package

modules are searched in python at sys.path

example
main.py
tools
|-__init__.py -->used to recgonize the module as a whole package
|-exlib.py --> runtime checker
|-s_math.py --> functions: add(),subtract(),multiply(),divide()

why __init__
1)Shorter imports can use from tools import add instead of from tools.s_math import add
2)reliability - distinguishes packages from other scripts such as tests
3)Setup Code, run once
4)Folder Clarity

importing library from PyPI or UV
pip installs come from PyPI(the python package index which is a free online store of free python libraries)
why UV instead of PyPI , UV is faster

pip install <library name>
pip list - shows installed libraries
pip show <library name> - shows library details
pip uninstall <library name>

