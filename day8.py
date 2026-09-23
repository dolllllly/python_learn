# # python programming practice----
# Day 7
# ---------------------------------------------------------------------------------------------------------------------------------
# Comprehensions, enumerate(), zip() & Advanced Sorting

# -  List Comprehension
# -  List Comprehension with Conditions
# -  Dictionary Comprehension
# -  Set Comprehension
# -  enumerate()
# -  zip()
# -  sorted()
# -  sorted() with key=
# -  Lambda with sorted()
# -  Reverse Sorting
# -  Data Transformation

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------

# List Comprehension
# List comprehension is a short and easy way to create a new list from an existing sequence

# basic structure:
# [expression for item in iterable]

# normanl way:
number=[1,2,3,4,5]
square=[]
for i in number:
    square.append(i*i)
print(square)

# [1, 4, 9, 16, 25]

# comprehension way
 
number=[1,2,3,4,5]
square=[x*x for x in number]
print(square)

# output:
# [1, 4, 9, 16, 25]

numbers=[1,2,3,4,5]
double=[x*2 for x in numbers]
print(double)

# output:
# [2, 4, 6, 8, 10]

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------

# List Comprehension with Condition
# syntex:  
# [expression for item in iterable if condition]

# normal way:
numbers=[1,2,3,4,5,6]
even=[]

for i in numbers:
    if i%2==0:
        even.append(i)
print(even)

# [2, 4, 6]

# comprehension way:
numbers=[1,2,3,4,5,6]
even=[i for i in numbers if i%2==0]
print(even)

# output:
# [2, 4, 6]

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------

# transform + Filter

# normal waays:
numbers=[1,2,3,4,5,6]
even=filter(lambda x:x%2==0,numbers)
filtered=list(even)

result=map(lambda x:x*x,filtered)
print(list(result))

# [4, 16, 36]

# comprehension way
numbers=[1,2,3,4,5,6]
result=[n*n for n in numbers if n%2==0]
print(result)

# output
# [4, 16, 36]

# process:
# 1 → ignored
# 2 → 2 × 2 → 4
# 3 → ignored
# 4 → 4 × 4 → 16
# 5 → ignored
# 6 → 6 × 6 → 36

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------

# String Comprehension

# normal way:
names=["dolly","anu","adiba"]
upper_name=[]
for i in names:
    upper_name.append(i.upper())
print(upper_name)

# ['DOLLY', 'ANU', 'ADIBA']


# comprehension way
names=["dolly","anu","adiba"]
upper_names=[name.upper() for name in names]
print(upper_names)

# output:
# ['DOLLY', 'ANU', 'ADIBA']

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Dictionary Comprehension
# syntax:
# {key: value for item in iterable}

# normal way:
numbers=[1,2,3,4,5]
square={}
for n in numbers:
    square[n]=n*n
print(square)

# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# comprehension way:
numbers=[1,2,3,4,5]
square={n:n*n for n in numbers}
print(square)

# output:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}



# --------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Set Comprehension

numbers=[1,2,3,3,5,4,5]
square={n*n for n in numbers}
print(square)

# output:
# {1, 4, 9, 16, 25}

# Remember:
#    [] → list comprehension
#    {key: value} → dictionary comprehension
#    {expression} → set comprehension

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------

# enumerate()
# enumerate() is used when you want to loop through a sequence and get both the index and the value at the same time


# normal ways
names=["dolly","anu","adiba"]
for i in range(len(names)):
    print(i,names[i])

# output:
# 0 dolly
# 1 anu
# 2 adiba

# comprehension way:
names=["dolly","anu","adiba"]
for index, name in enumerate(names):
    print(index,name)

# output:
#  0 dolly
# 1 anu
# 2 adiba

# /start from 1
names=["dolly","anu","adiba"]
for index,name in enumerate(names,start=1):
    print(index,name)

# output:
# 1 dolly
# 2 anu
# 3 adiba

# AI/ML connection:
# When processing datasets, you'll often need: index + value at the same time
# enumerate() is perfect for this.


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------

# zip() 
#  zip() is used to combine two or more sequences together, matching their elements by position

names=['dolly','anu','adiba']
marks=[99,88,96]
result=zip(names,marks)
for name,mark in result:
    print(name,mark)

# output:
# dolly 99
# anu 88
# adiba 96


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Convert zip() to a list

names=['dolly','khushi','adiba','anu']
marks=[99,85,89,90]

result=list(zip(names,marks))
print(result)

# output:
#  [('dolly', 99), ('khushi', 85), ('adiba', 89), ('anu', 90)]

# zip() with three lists

names=['dolly','anu','adiba']
marks=[90,98,95]
subjects=['python',"c++","java"]

for name,mark,subject in zip(names,marks,subjects):
    print(name,subject,mark)

# output:
# dolly python 90
# anu c++ 98
# adiba java 95


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Important: Different lengths
# zip() stops when the shortest sequence ends

names=['dolly','anu','adiba']
marks=[90,98]
print(list(zip(names,marks)))

# output:
# [('dolly', 90), ('anu', 98)]

# so "adiba" is not included


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------

# zip() with enumerate()

names=['dolly','anu','adiba']
marks=[90,98,95]

for index,(name, mark) in enumerate(zip(names,marks)):
    print(index,name,mark)

# output:
# 0 dolly 90
# 1 anu 98
# 2 adiba 95



# --------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Remember
# Function:	                       Main purpose:
# enumerate()	                      Gives index + value
# zip()	                              Combines values from multiple sequences
# map()	                              Applies a function to each value
# filter()	                          Selects values based on a condition
# reduce()	                          Reduces values to one result


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------

# sorted() with key=
# sorted() is used to sort items in a list or other iterable
# The key= argument tells Python what value to use for sorting

names=['dolly','anu','zuli','adiba']
result=sorted(names,key=len)  #sorting based on length
print(result)

# output:
# ['anu', 'zuli', 'dolly', 'adiba']

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Sort in Reverse

numbers=[10,20,30,40,50]
result=sorted(numbers,reverse=True)
print(result)

# output:
# [50, 40, 30, 20, 10]


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Sort Dictionary Data
# This is extremely important for interviews

students={
    'dolly':90,
    'anu':98,
    'adiba':93,
}
result=sorted(students.items(),key=lambda x:x[1])  #sorting based on mark
print(result)

# output:
# [('dolly', 90), ('adiba', 93), ('anu', 98)]


# why x[1]?

# Each item is:
# ("Dolly", 90)

# So:
# x[0] → name
# x[1] → marks

# Therefore:
# key=lambda x: x[1]

# Highest Marks First

students={
    'dolly':90,
    'anu':98,
    'adiba':93,
}
result=sorted(students.items(),key=lambda x:x[1],reverse=True)  #sorting based on mark
print(result)

# output:
# [('anu', 98), ('adiba', 93), ('dolly', 90)]


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------

#                                                   practice
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Create squares from:
# numbers = [1, 2, 3, 4, 5, 6, 7, 8]

numbers=[1,2,3,4,5,6,7,8]
square=[n*n for n in numbers]
print(square)

# output:
# [1, 4, 9, 16, 25, 36, 49, 64]

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Using comprehension, create only odd numbers:

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
odd=[n for n in numbers if n%2!=0]
print(odd)

# output:
[1, 3, 5, 7, 9]

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Convert:
# names = ["dolly", "khushi", "dipti"]
# into uppercase using comprehension

names = ["dolly", "khushi", "dipti"]
upper_case=[n.upper() for n in names]
print(upper_case)

# output:
# ['DOLLY', 'KHUSHI', 'DIPTI']

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------

# enumerate()
languages = ["Python", "Java", "C++", "SQL"]
for index,language in enumerate(languages,start=1):
    print(index,language)

# output:
# 1 Python
# 2 Java
# 3 C++
# 4 SQL


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------

# zip()
names = ["Dolly", "Khushi", "Anu", "Adiba"]
scores = [92, 85, 90, 98]

for name,score in zip(names,scores):
    print(name,"scored",score)

# output:
# Dolly scored 92
# Khushi scored 85
# Anu scored 90
# Adiba scored 98

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Dictionary comprehension
# expected outcome: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

num=[1,2,3,4,5]
power={n:n*n for n in num}
print(power)

# output:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Given:

# students = {
#     "Dolly": 82,
#     "Khushi": 95,
#     "Divya": 76,
#     "Anu": 91,
#     "Adiba": 88
# }
# Task:
# Sort students according to marks from highest to lowest

students = {
    "Dolly": 82,
    "Khushi": 95,
    "Divya": 76,
    "Anu": 91,
    "Adiba": 88
}

result=sorted(students.items(),key=lambda x:x[1],reverse=True)
for key,value in result:
    print(key,value)

# output:
# Khushi 95
# Anu 91
# Adiba 88
# Dolly 82
# Divya 76


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------

# AI/ML Connection:
# These concepts may look small, but you'll use them heavily later.
# For example, preprocessing data:

data = [10, 20, 30, 40, 50]

normalized = [x / 100 for x in data]

# Filtering data:

data = [10, 20, 30, 40, 50]

filtered = [x for x in data if x >= 30]

# Combining features and labels:

features = ["age", "salary", "experience"]
values = [22, 45000, 2]

data = dict(zip(features, values))

print(data)

# Output:

# {'age': 22, 'salary': 45000, 'experience': 2}


# This type of data transformation becomes very common when we reach NumPy, Pandas and Machine Learning.

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------



# --------------------------------------------------------------------------------------------------------------------------------------------------------------------



# --------------------------------------------------------------------------------------------------------------------------------------------------------------------



# --------------------------------------------------------------------------------------------------------------------------------------------------------------------



# --------------------------------------------------------------------------------------------------------------------------------------------------------------------



# --------------------------------------------------------------------------------------------------------------------------------------------------------------------

