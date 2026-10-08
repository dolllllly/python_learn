# python programming practice----
# Day 18
# ------------------------------------------------------------------------------------------------------------------------------------------

# Generators & yield

# # Topic Learned:
        # - Generators
        # - yield
        # - return vs yield
        # - next()
        # - StopIteration
        # - Lazy Evaluation
        # - Generator Expressions
        # - Memory Efficiency



# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# What is a Generator?
# A generator is a special type of iterator that produces values one at a time instead of creating all values at once.
# the main keyword is: yield

# normal function:
def numbers():
    return [1,2,3,4,5]
print(numbers())

# output:
# [1,2,3,4,5]
# the entire list created and returned.

# generator

def numbers():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
g= numbers()
print(g)

# output:
# <generator object numbers at 0x0000024F6E844A90>

# here  g os a generstor object.

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# yield vs return

# return:
# once return executed . the function ends

def test():
    return 10
    return 20
    return 30
print(test())

# output:
# 10
# because after returning 10 the function end

# yield:
# yield pauses the function insted of destorying its state

def test():
    yield 10
    yield 20
    yield 30
g=test()
print(next(g))
print(next(g))
print(next(g))

# output:
# 10
# 20
# 30


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# How yield Works

def numbers():
    print("start")
    yield 1
    print("middle")
    yield 2
    print("end")
    yield 3
g=numbers()    #generator object is created

print(next(g))

# output:
# start
# 1

#  the function stop at yield 1
# next:

print(next(g))

# output:
# middle
# 2

# it continue from where it stopped
# next
print(next(g))

# output:
# End 
# 3


# What happens after the last yield?
# the generator automatically raise: StopIteration

def test():
    yield 10
    yield 20
    yield 30
g=test()
print(next(g))
print(next(g))
print(next(g))
print(next(g))

# output:
# 10
# 20
# 30
# StopIteration



# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Generator with a for loop
# Usually you don't manually call next()

def numbers():
    yield 1
    yield 2
    yield 3
    for i in numbers():
        print(i)

# output:
# 1
# 2
# 3

# the for  loop automatically handles the iteration
# conceptually:

# generator
#    ↓
# next()
#    ↓
# value
#    ↓
# next()
#    ↓
# value
#    ↓
# next()
#    ↓
# value
#    ↓
# StopIteration


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Generator vs List
# list:
def numbers():
    return [1,2,3,4,5]
# all values are stored in memory

# generator:

def numbers():
    for i in range(1,6):
        yield i
for i in numbers():
    print(i)

# values are produce one at a time
# output:
# 1
# 2
# 3
# 4
# 5

# this is called lazy evalution.

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Why are generators useful?
# Generators are useful mainly because they produce values one at a time instead of storing all values in memory at once
        # memory efficiency
        # lazy evaluation
        # useful for large data

# suppose you need numbers from 1 to 10 crore.

# a normal approach might create/store a huge collection
numbers=[i for i in range (1,100000000)]
# that require a lots of memory.

# a generator:

def numbers():
    for i in range(1,100000000):
        yield i
# it doesn't craeate all 100 values at once.

# it gives you:
# 1 → next()
# 2 → next()
# 3 → next()
# ...
# only the value needed at theat moment is produced.

# It is lazy
# This is called  lazy evaluation.

# normal:
def number():
    return [1,2,3,4,5]
# everything is created immediately.

# generator :
def numbers():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

# value are produced only when requested

g=numbers()
print(next(g))  # 1
print(next(g))  # 2
#  the generator doesn't continue to 3 until you ask for another value.

    
# They are useful for:
        # large datasets
        # reading large files
        # data pipelines
        # streaming data
        # ML preprocessing
        # API data processing
        # processing records one at a time

# example:
def read_lines(filename):
    with open(filename,"r") as file:
        for line in file:
            yield line.strip()

for line in read_lines("data.txt"):
    print(line)

# or

def read_lines(filename):
    with open(filename,"r") as file:
        for line in file:
            yield line.strip()

g=read_lines("data.txt")
print(next(g))
print(next(g))

# only required data is processed at a time.


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# generator with loop

def even_number(n):
    for i in range(1,n+1):
        if i %2==0:
            yield i
for even in even_number(10):
    print(even)

# output:
# 2
# 4
# 6
# 8
# 10

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# generator maintains state

def counter():
    count=1
    while count<=3:
        yield count
        count+=1
c=counter()
print(next(c))
print(next(c))
print(next(c))

# output:
# 1
# 2
# 3
#  the value pf count is preserved between cells

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Generator Expression
# There is also a shorter way to create generators

# List comprehension
numbers=[x*2 for x in range(5)]
print(numbers)

# generator expression

numbers=(x*2 for x in range(5))
# print(numbers)  #this create a generator
for x in numbers:
    print(x)

# output:
# 0
# 2
# 4
# 6
# 8

# Key difference

# creates a list.
# [expression for item in iterable]

# creates a generator.
# (expression for item in iterable)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#                                                                            practice:

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Squares
# Create a generator that produces squares from 1 to n

def square_number(n):
    for i in range (1,n+1):
        yield i**2
for i in square_number(5):
    print(i)

# output:
# 1
# 4
# 9
# 16
# 25

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# odd numbers:
# Create a generator that produces odd number from 1 to n

def odd_number(n):
    for i in range(1,n,2):
            yield i
for i in odd_number(10):
    print(i)

# output:
# 1
# 3
# 5
# 7
# 9

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Countdown
# Create a generator:

def countdown(n):
    count=n
    while count>0:
        yield count
        count-=1
for i in countdown(5):
    print(i)

# output:
# 5
# 4
# 3
# 2
# 1


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Multiplication table
# Create a generator that produces the multiplication table of a number.

def table(n):
    for i in range (1,11):
        yield n*i
for i in table(5):
    print(i)

# 5
# 10
# 15
# 20
# 25
# 30
# 35
# 40
# 45
# 50

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Fibonacci
# Create a generator that produces Fibonacci numbers

def fibonacci(n):
    a=0
    b=1
    for i in range(n):
        yield a
        a,b=b,a+b
for i in fibonacci(10):
    print(i)

# output:
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Mini Project 
# Lazy Number Processor

# Create:
    # def process_numbers(numbers):
    # ...

# It should:
    # Receive a list of numbers.
    # Generate only even numbers.
    # Square each even number.
    # Return them using yield

# Challenge

# Don't create another list.

# Use:

# yield

def process_number(numbers):
    for i in numbers:
        if i%2==0:
            yield i**2
numbers=[1,2,3,4,5,6]
for i in process_number(numbers):
    print(i)

# output:
# 4
# 16
# 36


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------





