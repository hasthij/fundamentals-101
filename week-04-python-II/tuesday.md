Vocab
Exception, error while running the program
Traceback, error report 
Handle/Catch, deal with exceptions without crashing the program
Raise, Triggering a exception
Bug
Debug
Debuger, line by line  code inspector tool

Exception
ZeroDivisionError
ValueError
TypeError
IndexError
KeyError
FileNotFoundError
NameError
AttributeError

Using try,Except
try , tries to run the code and if an exception pops up, run the matching except condition

Try, always run first
Except X - to catch exceptions
Else - use if no errors happened
finally - used to closing files etc, messages, always runs exception or not

use else to output from try, example print("File read successfully") where try opened the file

catching error messages
try:
    int("abc")
except Value Error as e:
    print("Problem", e)


Raising Own errors
using raise

def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    return age

try:
    set_age(-5)
except ValueError as error:
    print(error)   # Age cannot be negative.

using pbd to pause program
breakpoint()


