# # python programming practice----
# Day 7
# ----------------------------------------------------------------------------------------------
# Advanced Functions & Lambda
# - *args
# - **kwargs
# - Positional arguments
# - Keyword arguments
# - Local scope
# - Global scope
# - global keyword
# - Nested functions
# - Functions as objects
# - Lambda functions
# - map()
# - filter()
# - reduce()
# - Recursion
# - Base condition
# - Recursive factorial

# ---------------------------------------------------------------------------------------------------------

# *args — Multiple Positional Arguments
# *args syntax allows a function to accept any number of positional arguments
#  All passed values are collected into a tuple, which can then be accessed or iterated inside the function
#  This is useful when the number of arguments is not known beforehand



# args become tuple

def test(*args):
    print(args)

test(10, 20, 30)

# output:
# (10, 20, 30)

def add(*num):
    total=0
    for i in num:
      total+=i
    return total
print(add(10,20))
print(add(10,20,30))
print(add(10,20,30,40))
print(add(10,20,49,48,34,89))

# output:
# 30
# 60
# 100
# 250



# ---------------------------------------------------------------------------------------------------------
# **kwargs — Multiple Keyword Arguments
# **kwargs syntax allows a function to accept any number of keyword arguments
#  All arguments are collected into a dictionary, where the argument names become keys and their corresponding values become dictionary values

# **kwargs become dictionary

def student(**kwargs):
   print(kwargs)
student(name="dolly",age=20,marks=90)

# output:
# {'name': 'dolly', 'age': 20, 'marks': 90}

def student(**details):
   for key,value in details.items():
      print(key,"=",value)
student(name="dolly",age=21,marks=90,city="odisha")

# output:
# name = dolly
# age = 21
# marks = 90
# city = odisha


# ---------------------------------------------------------------------------------------------------------

# *args + **kwargs
# we can use both

def details(*args,**kwargs):
   print("argument:",args)
   print("keyword argument:",kwargs)
details(10,20,30,name="dolly",age=20)

# output:
# argument: (10, 20, 30)       #tuple
# keyword argument: {'name': 'dolly', 'age': 20}    #dictionary


# ---------------------------------------------------------------------------------------------------------

# Argument Order
# When using different types of parameters, the usual order is: normal,*args,**kwargs

def details(name,*num,**info):
   print("normal:",name)
   print("argument:",num)
   print("keyword argument:",info)

details("dolly",90,89,94,age=21,city="odisha")

# output:
# normal: dolly
# argument: (90, 89, 94)
# keyword argument: {'age': 21, 'city': 'odisha'}


# ---------------------------------------------------------------------------------------------------------

# Nested Functions
# A function defined inside another function is called  nested function

def outer():

   def inner():
      print("inside inner function")
   inner()
outer()

# output:
# inside inner function

# ---------------------------------------------------------------------------------------------------------

# Function Returning a Function

def outer():              #  line1
   def inner():           #line2
      print("hello")      #line3
   return inner            #line4
x=outer()                  #line5
x()        #inner()         #line6

# line of execution:
1-5-2-3-4-5-6

# output:
# hello


# ---------------------------------------------------------------------------------------------------------

# Lambda Function
# A lambda is a small anonymous function
# lambda function are creates using lambda keyword
# result of the expression returned automatically,no return keyword needed
# syntax : lambda argument:expression
# normal function
def square(x):
   return x*x
square(2)

# lambda function:
square=lambda x: x*x
print(square(2))

# output
# 4


# ---------------------------------------------------------------------------------------------------------

# lambda example

# add
add=lambda a,b:a+b
print(add(10,20))

# output
# 30

# even / odd
check=lambda x: "even" if x%2==0 else "odd"
print(check(45))
print(check(28))

# output:
# odd
# even

# Cube
cube=lambda x: x**3
print(cube(3))

# output:
# 27

# ---------------------------------------------------------------------------------------------------------
# map()
#  This function applies a lambda expression to each element and returns a map object
# It can be converted to a list using list()

num=[10,20,30,40,50]
result=map(lambda x:x*2,num)
print(list(result))

# output:
# [20, 40, 60, 80, 100]


# ---------------------------------------------------------------------------------------------------------

# filter()
# filter() selects elements that satisfy a condition

num=[10,45,56,34,67,35]
result=filter(lambda x: x%2==0,num)
print("even_list:",list(result))

# output:
# even_list: [10, 56, 34]


# ---------------------------------------------------------------------------------------------------------

# map() vs filter()
# map() transforms data
# while filter() select data

num=[1,2,3,4,5]
result1=map(lambda x: x*x,num)
result2=filter(lambda x:x%2!=0,num)
print("transform data:",list(result1))
print("selected data:",list(result2))

# output:
# transform data: [1, 4, 9, 16, 25]
# selected data: [1, 3, 5]


# ---------------------------------------------------------------------------------------------------------

# reduce()
#  This function repeatedly applies a lambda expression to elements of a list to combine them into a single result
# it is available through functools

from functools import reduce
num=[10,20,30,40,50]
result=reduce(lambda a,b:a+b,num)
print(result)

# output:
# 150

# it work like
# 10+20=30
# 30+30=60
# 60+40=100
# 100+50=150

from functools import reduce
num=[10,20,30,40]
result=reduce(lambda a,b:a*b,num)
print(result)

# output:
# 240000



# ---------------------------------------------------------------------------------------------------------

# recursion:
# Recursion is a programming technique where a function calls itself either directly or indirectly 
#recursive function have tow key part:
#  Base Case: stopping condition that prevents infinite recursion.
# Recursive Case: part of the function where it calls itself with modified parameters
def countdown(n):
   if n==0:
      return      #base case
   print(n)
   countdown(n-1)
countdown(5)

#output: 
# 5
# 4
# 3
# 2
# 1
# ---------------------------------------------------------------------------------------------------------

# Recursive Factorial

# normal factorial
def factorial(n):
   result=1
   for i in range(1,n+1):
      result*=i
   return result
print(factorial(5))

# output:
# 120

def fectorial(n):
   if n==0 or n==1:
      return 1
   
   return n*fectorial(n-1)
print(fectorial(5))

# output:
# 120

#   × factorial(4)
# 5 × 4 × factorial(3)
# 5 × 4 × 3 × factorial(2)
# 5 × 4 × 3 × 2 × factorial(1)
# 5 × 4 × 3 × 2 × 1  

# ---------------------------------------------------------------------------------------------------------
#                                                       practice:
# --------------------------------------------------------------------------

# Create:
# def multiply(*args):
# It should multiply any number of values.

def multiply(*num):
   multiple=1
   for i in num:
      multiple*=i
   return multiple

print(multiply(2,3,4))

# output:
# 24

# ---------------------------------------------------------------------------------------------------------

# Create:
# def display(**kwargs):
# for display(name="dolly",age=20,city="odisha") and print every key value pair

def display(**details):
   for key,value in details.items():
      print(key,":",value)

display(name="dolly",age=20,city="odisha")

# output:
# name : dolly
# age : 20
# city : odisha

# ---------------------------------------------------------------------------------------------------------

# Create a lambda that returns the square of a number

square=lambda x:x*x
n=int(input("enter any number: "))
print(square(n))

# output:
# enter any number: 8
# 64

# ---------------------------------------------------------------------------------------------------------

# Use map() to double:
# numbers = [10, 20, 30, 40]

numbers=[10,20,30,40]
double=map(lambda x:x*2,numbers)
print(list(double))

# output:
numbers=[10,20,30,40]
double=map(lambda x:x*2,numbers)
# [20, 40, 60, 80]


# ---------------------------------------------------------------------------------------------------------

# Use filter() to extract numbers greater than 50:

numbers = [20, 60, 45, 80, 30, 90]
check=filter(lambda x:x>50,numbers)
print(list(check))

# output:
# [60, 80, 90]

# ---------------------------------------------------------------------------------------------------------

# Create a lambda that checks whether a number is:
# -  Positive
# -  Negative
# -  Zero

check=lambda x: "positive" if x>0 else "negative" if x<0 else "zero"
print(check(0))
print(check(-2))
print(check(90))

# output:
# zero
# negative
# positive

# ---------------------------------------------------------------------------------------------------------

# Map

# Given:
# numbers = [1, 2, 3, 4, 5]
# Use map() to create:
# [1, 4, 9, 16, 25]

numbers=[1,2,3,4,5]
square=map(lambda x:x*x,numbers)
print(numbers,"turns into",list(square))
# output:
# [1, 2, 3, 4, 5] turns into [1, 4, 9, 16, 25]

# ---------------------------------------------------------------------------------------------------------

# Given:
# numbers = [12, 15, 18, 21, 24, 27, 30]
# Use filter() to get numbers divisible by 3

numbers=[12,15,18,21,24,27,50]
divisible=filter(lambda x:x%3==0,numbers)
print(list(divisible))

# output
# [12, 15, 18, 21, 24, 27]

# ---------------------------------------------------------------------------------------------------------

# Reduce

# Using reduce(), calculate the product:
# numbers = [2, 3, 4, 5]

from functools import reduce
numbers=[2,3,4,5]
product=reduce(lambda x,y:x*y,numbers)
print(product)

# /output:
# 120

# ---------------------------------------------------------------------------------------------------------

# Second Largest:

def second_largest(num):
   second=num[0]
   first=num[0]
   for i in num:
      if i>first:
         second=first
         first=i
      elif i>second and i!=first:
         second=i
   return second
numbers=[10,50,20,80,55]  
print(second_largest(numbers))

# output:
# 55

# ---------------------------------------------------------------------------------------------------------

# Frequency Function:
def frequency(text):
   frequency={}
   for i in text:
      if i in frequency:
         frequency[i]+=1
      else:
         frequency[i]=1
   for key,value in frequency.items():
      print(key,"->",value)
text="programming"
frequency(text)

# output:
# p -> 1
# r -> 2
# o -> 1
# g -> 2
# a -> 1
# m -> 2
# i -> 1
# n -> 1



# ---------------------------------------------------------------------------------------------------------

# First Unique Character

def first_unique_character(text):
   dict={}
   for i in text:
      if i in dict:
         dict[i]+=1
      else:
         dict[i]=1
   for key,value in dict.items():
      if value==1:
         print(key)
         break
text="aabbcdde"
first_unique_character(text)

# output:
# c

# ---------------------------------------------------------------------------------------------------------

# Data Processing Pipeline

# Create:
# numbers = [10, 15, 20, 25, 30, 35, 40, 45, 50]
# Your program should:
# -  Step 1
#      Use filter() to select numbers divisible by 5
# -  Step 2
#      Use map() to square them
# -  Step 3
#       Use reduce() to calculate their total

from functools import reduce
numbers=[10,25,84,20,56,55,45]
divisible=filter(lambda x:x%5==0,numbers)
divisible_by_5=list(divisible)
square=map(lambda x:x*x,divisible_by_5)
square_result=list(square)
final=reduce(lambda x,y:x+y,square_result)
print(final)

# output:
# 6175

# ---------------------------------------------------------------------------------------------------------



         
      