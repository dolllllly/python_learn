# python programming practice----
# Day 17
# ------------------------------------------------------------------------------------------------------------------------------------------

# Iterables, Iterators, iter(), next(), __iter__() & __next__()

## Topic learned:
    #  Iterable
    # Iterator
    # iter()
    # next()
    # StopIteration
    # __iter__()
    # __next__()
    # Iterator state
    # How for works internally
    # Custom iterators
    # Debugging infinite iterators
    # MNC interview questions
    # Custom iterator project
    # GitHub practice 


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# What is an Iterable?
#  an iterable is an object that you can loop over using for.

number=[10,20,30]
for n in number:
    print(n)

# output:
# 10
# 20
# 30

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# What is an Iterator?
# an iterator is an object that gives you elements one at a time.

number=[10,20,30]
iterator=iter(number)
# now you can get values using
print(next(iterator))
print(next(iterator))
print(next(iterator))

# output:
# 10
# 20
# 30


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# iter():
# iter() is a buit-in function that convert an iterable into an iterator.

number=[10,20,30]
it=iter(number)
print(it)

# output:
# <list_iterator object at 0x000002BE36909D80>

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# next():
# next() gets the next value from an iterator.

number=[10,20,30]
it=iter(number)
print(next(it))
# output:
10
print(next(it))
# 20

print(next(it))
# 30


# think of it like a pointer:

# Iterator
#    ↓
# [10, 20, 30]
#  ↑
# current position

# after: next(it)
# the iterator moves forward.


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# what happens after the last element?

number=[10,20,30]
it=iter(number)
print(next(it))
print(next(it))
print(next(it))
print(next(it))

# output:
# 10
# 20
# 30
# StopIteration

# python raise the stopiteration exception.
# it means: there are no more values


# Handling StopIteration
# we can handle it using try-except:


number=[10,20,30]
it=iter(number)
try:
    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))
except StopIteration:
    print("No more element")

# output:
# 10
# 20
# 30
# No more element


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# How Does for Actually Work?

# when you write:
number=[10,20,30]
for num in number:
    print(num)

# python conceptually does somethng similar to:

iterator=iter(number)
while True:
    try:
        num=next(iterator)
        print(num)
    except StopIteration:
        break

# so:
# for loop
#    ↓
# iter()
#    ↓
# iterator
#    ↓
# next()
#    ↓
# next()
#    ↓
# next()
#    ↓
# StopIteration
#    ↓
# loop ends


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Iterable vs Iterator

# | Iterable                                   | Iterator                   |
# | ------------------------------------------ | -------------------------- |
# | Can be looped over                         | Produces values one by one |
# | Can create an iterator                     | Keeps current position     |
# | Example: list                              | Example: `iter(list)`      |
# | Usually works with `for`                   | Works with `next()`        |
# | Doesn't necessarily implement `__next__()` | Implements `__next__()`    |



# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# string example:
name="dolly"
it=iter(name)
print(next(it))
print(next(it))
print(next(it))

# output:
# d
# o
# l

print(next(it))
print(next(it))

# output:
# l
# y

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# dictionary example:

student={"name":"dolly","age":20,"course":"AIML"}

it=iter(student)
print(next(it))

# output:
# name

print(next(it))
print(next(it))

# output:
# age
# course

# by default, iterating over a dictionary gives its keys.

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# range() example:

number=range(1,5)
it=iter(number)
print(next(it))
print(next(it))
print(next(it))
print(next(it))

# output:
# 1
# 2
# 3
# 4


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# __iter__() and __next__():
# An iterator generally implements two special methods:
# __iter__()
# __next__()

# __iter__:
# it is responsible for returning an iterator object.

number=[10,20,30]
iterator=iter(number)

#  this iter(number) internally calls: 
number.__iter__()
# and return an iterator



# __next__():
# Once you have an iterator:
iterator=iter(number)

# you can ask for the next value:
next(iterator)

# which internally calls:
iterator.__next__()


# example:

class count:
    def __init__(self):
        self.number=1
    def __iter__(self):
        return self
    def __next__(self):
        value=self.number
        self.number+=1
        return value
counter=count()
print(next(counter))
print(next(counter))
print(next(counter))

# output:
# 1
# 2
# 3

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Why Does __iter__() Return self?
# For an iterator object, the iterator itself is the object producing the values.

def __iter__(self):
    return self
# means:
# i am already an iterator.


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# A Proper Finite Iterator

# Let's make one that produces:
# 1
# 2
# 3
# 4
# 5

class count:
    def __init__(self,limit):
        self.limit=limit
        self.number=1
    def __iter__(self):
        return self
    def __next__(self):
        if self.number>self.limit:
            raise StopIteration
        value=self.number
        self.number+=1
        return value
counter=count(5)

for number in counter:
    print(number)

# output:
# 1
# 2
# 3
# 4
# 5

# When Python sees:

# for number in counter:

# it roughly does:
# counter
#    ↓
# iter(counter)
#    ↓
# counter.__iter__()
#    ↓
# returns counter
#    ↓
# next(counter)
#    ↓
# 1
#    ↓
# next(counter)
#    ↓
# 2
#    ↓
# ...
#    ↓
# next(counter)
#    ↓
# StopIteration
#    ↓
# loop ends


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Custom Iterator Example: Even Numbers:

class EvenNumber:
    def __init__(self,limit):
        self.limit=limit
        self.number=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.number>self.limit:
            raise StopIteration
        value=self.number
        self.number+=2
        return value
counter=EvenNumber(10)
for number in counter:
    print(number)

# output:
# 0
# 2
# 4
# 6
# 8
# 10


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Iterator State:
# One of the main advantages of an iterator is that it remembers its state.

number= [10, 20, 30]
it = iter(number)
print(next(it))

# output:
# 10
print(next(it))

# output:
# 20
# it doesb't start from 10 again.
# The iterator remembers: "I already gave you 10."


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Iterable Can Create Multiple Iterators

number= [10, 20, 30]

it1 = iter(number)
it2 = iter(number)

print(next(it1))
print(next(it1))
print(next(it2))

# output:
# 10
# 20
# 10
# Because it1 and it2 maintain separate iteration states

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Iterator State Is Shared


number = [10, 20, 30]

it = iter(number)

a = next(it)
b = next(it)

print(a)
print(b)


# output:
# 10
# 20


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#                                                        practice:
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Create an iterator:
        # Countdown(5)

# that produces:
    # 5
    # 4
    # 3
    # 2
    # 1

# and then raises StopIteration.


class CountDown:
    def __init__(self):
        self.number=5
    def __iter__(self):
        return self
    def __next__(self):
        if self.number<1:
            raise StopIteration
        value=self.number
        self.number-=1
        return value
counter=CountDown()
for n in counter:
    print(n)

# output:
# 5
# 4
# 3
# 2
# 1

# OR

class CountDown:
    def __init__(self,start):
        self.current=start
    def __iter__(self):
        return self
    def __next__(self):
        if self.current<1:
            raise StopIteration
        value=self.current
        self.current-=1
        return value
counter=CountDown(6)
for n in counter:
    print(n)

# output:
# 6
# 5
# 4
# 3
# 2
# 1


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# mini project:
# Custom Number Iterator

# Build an iterator that generates numbers between a starting value and ending value.
    # Example:
    # NumberRange(3, 7)

# should produce:
    # 3
    # 4
    # 5
    # 6
    # 7

# Requirements

    # Your class must contain:
        # __init__()
        # __iter__()
        # __next__()

    # and correctly raise:
        # StopIteration



class NumberRange:
    def __init__(self,start,end):
        self.current=start
        self.stop=end
    def __iter__(self):
        return self
    def __next__(self):
        if self.current>self.stop:
            raise StopIteration
        value=self.current
        self.current+=1
        return value
counter=NumberRange(3,7)
for num in counter:
    print(num) 

# output:
# 3
# 4
# 5
# 6
# 7




# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# now modify the code of number range so that it take start , stop, and step
# NumberRange(2,10,2)
# output:
2
4
6
8
10

class NumberRange:
    def __init__(self,start,end,step):
        self.current=start
        self.end=end
        self.step=step
    def __iter__(self):
        return self
    def __next__(self):
        if self.current>self.end:
            raise StopIteration
        value=self.current
        self.current+=self.step
        return value
number=NumberRange(2,10,2)
for i in number:
    print()

# output:
# 2
# 4
# 6
# 8
# 10

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------






# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------






# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------






# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------






# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------






# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


