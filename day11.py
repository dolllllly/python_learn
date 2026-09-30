# python programming practice----
# Day 11
# ------------------------------------------------------------------------------

# Modules, Packages & __name__

# Topics Learned
# -  Python Modules
# -  import
# -  from ... import
# -  Module aliases
# -  Custom modules
# -  Python packages
# -  __init__.py
# -  __name__
# -  __main__
# -  if __name__ == "__main__"

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# What is a module?
# a  module is simply a python file containing code that you can reuse in another python file
# for example you have two files:
# calculator.py and main.py
# calculator.py is a module. 
# you can import its functions into main.py instead of writing the same code again

# calculator.py
def add(a,b):
    return a+b
def substract(a,b):
    return a-b

# this is a module .its module name is calculator

# Why use modules?

    # Code reuse: Write a function once and use it in multiple files
    # Organization: Keep related functions together
    # Maintenance: Fix or update code in one place
    # Readability: Avoid putting an entire project in one huge file

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# importing modules
# python provides different ways to import code

# import the entiree module

import math
print(math.sqrt(25))
print(math.pi)

# output:
# 5.0
# 3.141592653589793

# when you import a module this way, use the module name followed by dot to access its members


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# import a specific function
# syntax:- 
# from module_name import function_name

from math import sqrt
print(sqrt(36))

# output:
# 6.0

# here you can use sqrt() directly instead of math.sqrt()

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# import multiple function
# from module_name import function_1,function_2,..function_n

from math import sqrt,factorial
print(sqrt(49))
print(factorial(5))

# output:
# 7.0
# 120

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# use an allias
# an alias gives a module or function a shorter name

import math as m
print(m.sqrt(49))

# output
#  7.0

# you can also alias a specific function:

from math import factorial as fact
print(fact(4))

# output:
# 24



# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Avoid from module import *

from math import *

# this import many names directly into your file. it can make code harder to understand and may cause naming conflicts.


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Useful built-in Python modules
# python includes many modules that you can use wihout installing extra packages

#   module                     purpose                                          example
# math module:          mathematical operations:                       math.sqrt(25)
# random module:        random values:                                  random.randit(1,10)
# datatime module:      dates and times:                               datetimes.date.today()
# os module:            operating-system operations:                    os.getcwd()
# pathlib module:       working with file paths :                       path("data.txt")
# json:                 read and write JSON :                           json.load(file)
# statastics:           basic statistics:                               statistic.mean{[2,4,6]}


# example:
import random
number=random.randint(1,10)
print("ramdom number is: ",number)

# output
# ramdom number is:  3
# ramdom number is:  6

import statistics
marks = [70, 80, 90, 60, 100]
print(statistics.mean(marks))
print(statistics.median(marks))

# output:
# 80
# 80

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# creating your own module:
# a module becomes useful when you import it from another file

# first:
# create two python file in the same directory 

# 1. text_processing.py
# 2. main.py

# in text_processing.py

def count_words(text):
    return len(text.split())

def reverse_words(text):
    return " ".join(text.split()[::-1])

def count_vowels(text):
    vowels="aeiou"
    return sum(1 for char in text.lower() if char in vowels)

# in main.py

import text_processing

sentence="how are you ?"
print(text_processing.count_words(sentence))
print(text_processing.reverse_words(sentence))
print(text_processing.count_vowels(sentence))

# run in main.py:
# 4
# ? you are how
# 5
 
# what happens during import?
# 
# when python executes:
# import text_processing

# it generally:
            # searches for the module using its impport system
            # create or retrives the module object
            # executes the module's top level code when it is first loaded
            # makes its definations accessible through text_processing

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# packages and __init__.py

# a package helps us organize related python modules into a folder, 
# while __init__.py is a special file used to initializ a package and control what it exposes

# package:-
# a package is a folder that contains related python modules
    #   module: a single python file (.py)
# for example, imagine you are building a student management system:

# student_management/
        # __init__.py
        # student.py
        # marks.py
        # attendance.py

# here:
# student_management is the package
# student.py , mark.py , and attendence.py are modules
# __init__.py is the package initialization file

# what is __init__.py?
# __init__.py is a special python filed placed inside a package folder.
# it is commonly used to:
            # make a directory as a regular python package
            # run initialization code when the package is imported
            # make selected functions or classes available directly from the package
#
# in traditional python packages, this file is importent. morden python also supports namespace package without __init__.py



# folder structure:
# python/
#      cal_package/
#         __init__.py
#         calculator.py
#      main.py

# inside calculator.py

def add(a,b):
    return a+b
def substract(a,b):
    return a-b

# inside __init__.py

print("package initialized")

# now in separate python file package_practice.py:

import cal_package.calculator
print(cal_package.calculator.add(10,5))

# output:
# package initialized
# 15

# the initialization message apper when the package is first importes in that python process

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# importing function using __init__.py
# you can also use __init__.py to make functions easier to import

# supose your folder structure is:
# python/
#      cal_package/
#         __init__.py
#         calculator.py
#      main.py


# inside __init__.py
from .calculator import add

# the dot(.) means the current package

# import the function im package_practice.py:

from cal_package import add
print(add(10,20))

# output:
30

# without exposing add through __init__.py , you could normally write:
from cal_package.calculator import add

# both approch work


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# the special variable __name__

# python automatically provides a special variable named __name__ in every module
# it tells us how a python file is being used- wheather it is being run directly or imported into another file

# its value depends on how the file is executed:
        # if you run a python file directly, __name__ is set to "__main__"
        # if you import that file into another python file, __name__ is set to module's name

# example:

# inside text_processing.py
def count_words(text):
    return len(text.split())
def reverse_words(text):
    return " ".join(text.split()[::-1])
def count_vowels(text):
    vowels="aeiou"
    return sum(1 for char in text.lower() if char in vowels)
print( "module name:",__name__)

# if you run text_processing.py directly output will be:
# module name: __main__

# but if you import text.processing in module_practice.py file 
# in module_practice.py
import text_processing

# the output is:
# module name: text_processing

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# if __name__=="__main__":

# it ensure that a block of code runs only when the file is executed directly ,rather than when it is imported.
# It allows a file to be both:
        # Imported as a reusable module
        # Run directly as a program

# example:

# inside add_calculator.py

def add(a,b):
    return a+b
def main():
    print(add(10,20))
if __name__=="__main__":
        main()

# if you run calculator.py
# output:
30

# if you import it 

import add_calculator
print(add_calculator.add(5,7))

# output:-
# 12

# the 30 is not printed because the if condition inside add_calculator.py is false during the import in another file
# __name__==add_calculator after import


# why do we use it?
# the if __name__=="__main__": pattern is useful for:
        # testing function: run text code without executing it during imports
        # organizing projects: separate resuable functions from the main program
        # prevent unwanted execution: avoid running certain statements whenever another file imports your module
        # creating resuable modules: allow the same file to work as both a standalone program and an imported module 

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# import execution,catching and circular imports

# import execution:
# when python import a module for the first time, it executes the model's top-level code

# This includes variable assignments, function definitions, class definitions, and any statements written outside functions or classes

# example:
# project/
#     main.py
#     maths.py

# file1:maths.py
print("math module is executing")
x=10
def add (a,b):
    return a+b
print("math module finished")

# file2: main.py

print("Main started")
import maths
print(maths.add(5, 3))
print("Main finished")

# run main.py:
# Main started
# Maths module is executing
# Maths module finished
# 8
# Main finished

# line of execution:
        # Python starts executing main.py
        # It prints Main started
        # Python encounters import maths
        # Python loads and executes the top-level statements in maths.py
        # The function add() is defined, but its body does not execute yet
        # Execution returns to main.py
        # maths.add(5, 3) calls the function and prints 8
        # The main program finishes

# Important: Importing a module executes its top-level code, but it does not automatically call every function defined inside it.

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Import caching

# Python caches imported modules in a dictionary called sys.modules
# When a module has already been imported, Python normally reuses the cached module instead of executing its top-level code again

# Example
# file:maths.py
print("Maths module loaded")

# file:main.py
import maths
import maths
import maths
print("Program finished")

# Output:
# Maths module loaded
# Program finished

# Why is "Maths module loaded" printed only once?
        # First import: Python loads and executes maths.py
        # Second import: Python finds maths in the cache
        # Third import: Python reuses the same cached module


# How to check the cache

import sys
import maths

print("maths" in sys.modules)

# Output:
# True

# sys.modules stores references to modules that Python has loaded. The cache is associated with the current Python interpreter process


# What about importlib.reload()?
# If you explicitly want to execute a module again, you can use importlib.reload().

import maths
import importlib

importlib.reload(maths)

# This re-executes the module's code
#  It is different from importing the module a second time

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# What is a circular import?

# A circular import occurs when two modules depend on each other.

# file:a.py

print("A started")
import b
def func_a():
    return "Hello from A"

# file:b.py

print("B started")
import a
print(a.func_a())

# This can cause confusing errors, especially when one module tries to access a name that has not yet been defined.

# Common solutions:
        # Move shared functions into a third module
        # Reduce dependencies between modules
        # Move an import inside a function when it genuinely needs to be delayed
        # Reconsider the project structure

# A delayed import can help in some cases, but it is not a universal fix. The cleanest solution is often to remove the circular dependency.

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Build a reusable validation module

    # Create validators.py with these functions:
    # is_valid_email(email)
    # is_valid_password(password)
    # is_valid_age(age)

# Requirements:

    # Email must contain @ and a dot after @
    # Password must contain at least 8 characters.
    # Age must be an integer between 18 and 100, inclusive.
    # Import the functions into another file in same directory.
    # Test valid and invalid inputs.

# inside validator.py:

def is_valid_email(id):
    if "@" in id and "." in id.split("@")[1] :
        return "valid email"
    return "invalid email"
def is_valid_password(password):
    if len(password)>=8:
        return "valid password"
    return "invalid password"
def is_valid_age(age):
    if age>=18 and age<=100:
        return "valid age"
    return "invalid age"

if __name__=="__main__":
    print("dolly@.com  : ",is_valid_email("dolly@.com"))
    print("dolly@cm  : ",is_valid_email("dolly@cm"))
    print("dolly.@cm  : ",is_valid_email("dolly.@cm"))
    print("dolly@example.com  : ",is_valid_email("dolly@example.com"))
    print("1234dvff3  : ",is_valid_password("1234dvff3"))
    print("1234dv3  : ",is_valid_password("1234dv3"))
    print("100  : ",is_valid_age(100))
    print("56  : ",is_valid_age(56))
    print("12  : ",is_valid_age(12))

# if we directly run it in the same file
# output:
# dolly@.com  :  valid email
# dolly@cm  :  invalid email
# dolly.@cm  :  invalid email
# dolly@example.com  :  valid email
# 1234dvff3  :  valid password
# 1234dv3  :  invalid password
# 100  :  valid age
# 56  :  valid age
# 12  :  invalid age

# it is basically for testing the code directly without importing

# in another file (validator_practice.py.py for me):
import validator
email=input("enter your email: ")
password=input("enter your password: ")
age=int(input("enter your age: "))
print(email ," : ", validator.is_valid_email(email))
print(password," : ", validator.is_valid_password(password))
print(age," : ", validator.is_valid_age(age))

# run the validator_practice.py file

# enter your email: python@gmail.com
# enter your password: 1234567hj
# enter your age: 19
# python@gmail.com  :  valid email
# 1234567hj  :  valid password
# 19  :  valid age

# enter your email: python.gmail@hi 
# enter your password: 9723490
# enter your age: 12
# python.gmail@hi  :  invalid email
# 9723490  :  invalid password
# 12  :  invalid age



# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Design a small text analysis library that can be imported into multiple programs.

# Required modules:
    # cleaning.py — normalize text.
    # metrics.py — count words, characters, and vowels.
    # report.py — format the analysis results.
    # __init__.py — expose selected functions.
    # main.py — accept input and display the report.

# Additional requirements:
    # No input prompts should run during import.
    # Every module must have one clear responsibility.
    # Write at least five test cases.
    # Include empty-string and whitespace-only inputs.
    # Avoid circular imports.
    # Add a README explaining how to run the program.

# inside cleaning.py — normalize text

def cleaned(text):
    return " ".join(text.lower().split())

if __name__=="__main__":    # execute only if you run it directly
    print(cleaned("    PYTHon  is Fun  "))

# inside metrics.py — count words, characters, and vowels

def count_word(text):
    return len(text.split())

def count_character(text):
    return sum(1 for i in " ".join(text.split())) 

def count_vowels(text):
    vowels="aeiou"
    return sum(1 for i in text.lower() if i in vowels)

if __name__=="__main__":
    text="  PYTHon Is  fUN   "
    print(count_word(text))
    print(count_character(text))
    print(count_vowels(text))

# inside report.py — format the analysis results
from .cleaning import cleaned
from .metrics import count_vowels,count_character,count_word

def generate_report(text):
    cleaned_text=cleaned(text)
    words=count_word(cleaned_text)
    characters=count_character(cleaned_text)
    vowels=count_vowels(cleaned_text)

    return (
         "\n----------------text report--------------------------\n"

        f"cleaned text: {cleaned_text}\n"
        f"total words: {words}\n"
        f"total characters: {characters}\n"
        f"total vowels: {vowels}"

    )

# inside  __init__.py
from .cleaning import cleaned
from .metrics import count_vowels,count_character,count_word
from .report import generate_report

# inside main.py — accept input and display the report

from analyzer import generate_report

def main():
    text=input("enter text: ")
    report=generate_report(text)
    print(report)

if __name__=="__main__":
    main()

# now run main.py file
# output:
# enter text:   pYTHon IS fuN  
# 
# ----------------text report--------------------------
# cleaned text: python is fun
# total words: 3
# total characters: 13
# total vowels: 3



# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



