 # python programming practice----
# Day 9
# ---------------------------------------------------------------------------------------------------------------------------------
# Exception Handling + Error Handling


# Topics Learned:
#     -  Exceptions
#     -  Exception handling
#     -  try
#     -  except
#     -  Specific exceptions
#     -  Multiple except blocks
#     -  as e  
#     -  else
#     -  finally
#     -  raise
#     -  Error handling
#     -  Debugging


# ------------------------------------------------------------------------------------------------------------------------------------------------------

# What is an Exception?
# An exception is an error that occurs while a program is running
# example:

a=10
b=0
print(a/b)

#it shows:
#  ZeroDivisionError: division by zero

# instead of allowing the program to cresh,we can handle the error

# ------------------------------------------------------------------------------------------------------------------------------------------------------

# Exception handling:
# exception handling allows a program to handle unexcepted error during execution in a controlled way,instead of creshing abruptly
# python provides four main type of keywords for handling exception:
# try
# except
# else
# finally 

# syntax:
# try:
#       # Code 
# except SomeException:
#       # Code 
# else:
#      # Code 
# finally:
#     # Code

# ------------------------------------------------------------------------------------------------------------------------------------------------------

# try and except
# try: Runs the risky code that might cause an error
# except: Catches and handles the error if one occurs

# Basic structure:

# try:
#     # risky code
# except:
#     # what to do if error occurs

try:
    a=10
    b=0
    print(a/b)
except:
    print("somthing went wrong")

# output:
# somthing went wrong


# ------------------------------------------------------------------------------------------------------------------------------------------------------

# Catch a Specific Exception
# Catching specific exceptions makes code to respond to different exception types differently
# its better to specify error

try:
    a = 10
    b = 0
    print(a / b)

except ZeroDivisionError:
    print("Cannot divide by zero")

# output:
# cannot divide by zero

# ------------------------------------------------------------------------------------------------------------------------------------------------------

# Multiple Exceptions
#  Multiple exceptions means handling different types of errors separately in the same try block

try:
    number=int(input("enter number: "))
    result=100/number
    print(result)
except ValueError:
    print("plese enter a valid number")
except ZeroDivisionError:
    print("number cannot be zero")

# output:
# enter number: 10
# 10.0

# enter number: 0
# number cannot be zero

# enter number: a
# plese enter a valid number

try:
    a = int(input("Enter a number: "))
    result = 10 / a
    print(result)

except (ValueError, ZeroDivisionError):
    print("Invalid input or division by zero")

# output:
# Enter a number: 0
# Invalid input or division by zero

# Enter a number: a
# Invalid input or division by zero

# Enter a number: 10
1.0



# ------------------------------------------------------------------------------------------------------------------------------------------------------

# as e
# We can store the error in a variable
# this is use for debugging

try:
    number=int("hello")
except ValueError as e:
    print(e)

# output:
# invalid literal for int() with base 10: 'hello'
# ------------------------------------------------------------------------------------------------------------------------------------------------------

# else
# else runs only when no exception occurs

try:
    number=int(input("enter any number: "))
except ValueError as e:
    print(e)
else:
    print("your number:",number)   #execute only if no exception occur

# output:
# enter any number: 10
# your number: 10

# enter any number: ug
# invalid literal for int() with base 10: 'ug'


# flow
# try
#  │
#  ├── error → except
#  │
#  └── no error → else
# ------------------------------------------------------------------------------------------------------------------------------------------------------

# finally
# finally runs whether an error occurs or not
# finally is commonly useful for cleanup, such as closing files or database connections

try:
    number=int(input("enter a number: "))
except ValueError as e:
    print(e)
else:
    print("your number:",number)
finally:
    print("program finished")  #run anyhow


# output:
# enter a number: 10
# your number: 10
# program finished

# enter a number: d
# invalid literal for int() with base 10: 'd'
# program finished

# ------------------------------------------------------------------------------------------------------------------------------------------------------

# Complete Structure

# try:
    # risky code

# except SomeError:
    # handle error

# else:
    # runs if no error

# finally:
    # always runs


# ------------------------------------------------------------------------------------------------------------------------------------------------------

# raise
# raise is used when you want to manually create an exception (error) in your program
try:
    age=int(input("enter age: "))
    if age<0:
        raise ValueError("Age cannot be less than zero")
    print("Age:",age)
except ValueError as e:
    print(e)

# output:
# enter age: -1
# Age cannot be less than zero

# enter age: 89
# Age: 89

# ------------------------------------------------------------------------------------------------------------------------------------------------------

# raise vs except


# raise
# Creates an error
# raise ValueError("Invalid age")

# except
# Handles an error
# except ValueError:
#     print("Invalid age")

# ------------------------------------------------------------------------------------------------------------------------------------------------------

# Why raise Is Useful in AI/ML

# Suppose you're building an ML model that expects a valid prediction input.

def predict(age):

    if age < 0:
        raise ValueError("Age cannot be negative")

    # model prediction

# This prevents invalid data from entering your system

# ------------------------------------------------------------------------------------------------------------------------------------------------------

#                                                              practice:
# ----------------------------------------------------------------------------------------------------------------------------------------------------

# Handle division by zero 
try:
    num1=int(input("enter the first number: "))
    num2=int(input("enter the second number: "))
    result=num1/num2
    print(result)

except ZeroDivisionError as e:
    print(e)

# enter the first number: 10
# enter the second number: 0
# division by zero

# ------------------------------------------------------------------------------------------------------------------------------------------------------

# Ask the user for an integer
# If they enter:
# abc
# display:
# Invalid number

try:
    number=int(input("enter any integer: "))

except ValueError:
    print("invalid number")
else:
    print("your number:"number)


# output:
# enter any integer: anc
# invalid number

# ------------------------------------------------------------------------------------------------------------------------------------------------------

# Write a program that asks for two numbers and performs division.

# Handle:
# ValueError
# ZeroDivisionError

try:
    num1=int(input("enter firs number: "))
    num2=int(input("enter second number: "))
    result=num1/num2
except ValueError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
else:
    print(result)
finally:
    print("done")

# output:
# enter firs number: ie
# invalid literal for int() with base 10: 'ie'
# done

# enter firs number: 10
# enter second number: 0
# division by zero
# done

# ------------------------------------------------------------------------------------------------------------------------------------------------------

# Safe Calculator

# Create:
# Enter first number:
# Enter second number:
# Enter operator (+ - * /):

# Handle:
# invalid numbers
# division by zero
# invalid operator

try:
    num1=int(input("enter first number: "))
    num2=int(input("enter second number: "))
    operator=input("enter operater + for addition, - for substraction ,* for multiplication, and / for division: ")
    if operator=="+":
        print("addition:",num1+num2)
    elif operator=="-":
        print("substraction:",num1-num2)
    elif operator=="*":
        print("multiplication:",num1*num2)
    elif operator=="/":
        print("division:",num1/num2)
    else:
        raise ValueError("invalid operator")
except ValueError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
except:
    print("error")

# output:
# enter first number: 67
# enter second number: 0 
# enter operater + for addition, - for substraction ,* for multiplication, and / for division: /
# division by zero

# enter first number: 78
# enter second number: 89
# enter operater + for addition, - for substraction ,* for multiplication, and / for division: jj
# invalid operator

# enter first number: 78
# enter second number: h
# invalid literal for int() with base 10: 'h'

# ------------------------------------------------------------------------------------------------------------------------------------------------------

# Marks Validator

# Ask:
# Enter marks:
# If marks aren't between 0 and 100:
# raise ValueError(...)
# Otherwise print:
# Valid marks


try:
    mark=int(input("enter mark:"))
    if mark<0 or mark>100:
            raise ValueError("mark should be between 0 and 100")
    print(mark)
except ValueError as e:
      print(e)

# output:
# enter mark:78
# 78

# enter mark:123
# mark should be between 0 and 100

# ------------------------------------------------------------------------------------------------------------------------------------------------------

# Write:

# def withdraw(balance, amount):

# Rules:
# amount must be positive
# amount cannot exceed balance

# Raise appropriate exceptions when the input is invalid.

# Example:
# Balance: 5000
# Amount: 6000
# Insufficient balance

def withdraw(balance,amount):
        if amount<0:
            raise ValueError("amount must be positive")
        if amount>balance:
            raise ValueError("insufficiant balance")
        print("amount:",amount)
        print("balance:",balance)
try:
    amount=int(input("enter amount: "))
    balance=int(input("enter balance: "))
    withdraw(balance,amount)
except ValueError as e:
    print(e)

# output:
# enter amount: 6000
# enter balance: 5000
# insufficiant balance

# enter amount: -87
# enter balance: 78
# amount must be positive

# enter amount: 123
# enter balance: g
# invalid literal for int() with base 10: 'g'



# ------------------------------------------------------------------------------------------------------------------------------------------------------


# ------------------------------------------------------------------------------------------------------------------------------------------------------


# ------------------------------------------------------------------------------------------------------------------------------------------------------