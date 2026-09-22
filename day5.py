#  python programming practice----
# Day 4
# ----------------------------------------------------------
# Python Tuples, Sets & Dictionaries
# ----------------------------------------------------------
# -Tuples
# -Tuple indexing
# -Tuple slicing
# -Tuple immutability
# -Tuple methods
# -Tuple unpacking
# -Swapping values
# -Sets
# -Set uniqueness
# -Adding and removing set elements
# -Union
# -Intersection
# -Difference
# -Symmetric difference
# -Dictionaries
# -Key-value pairs
# -Adding and updating dictionary values
# -Removing dictionary values
# -keys()
# -values()
# -items()
# - get()
# -Dictionary loops
# -Nested dictionaries
# -Dictionary with lists
# -Frequency counting

# ----------------------------------------------------------------------------------------------------------------------------------------------------------

                                                              # Tuple

# ----------------------------------------------------------------------------------------------------------------------------------------------------------

# A tuple is like a list, but it cannot be changed after creation

student=("dolly",20,"python")
print(student)

#output
#  ('dolly', 20, 'python')

# ----------------------------------------------------------------------------------------------

# indexing
# o        1     2
# 'dolly', 20, 'python'
# -3       -2     -1

student=('dolly',20,'python')
print(student[0])
print(student[-1])
print(student[::-1])

# output
# dolly
# python
# ('python', 20, 'dolly')

# ---------------------------------------------------------------------------------------------

# immutable: cannot be changed:

student=('dolly',20,'python')
student[1]=21
print(student)

# TypeError: 'tuple' object does not support item assignment

# -----------------------------------------------------------------------------------------------------

# count() methods : count the total occurance of the given element

t=(10,20,30,40,10)
print(t.count(10))

# output:
# 2

# --------------------------------------------------------------------------------------

# index(): return yhe index of the given element

t=(10,20,30,40,10)
print(t.index(10))
print(t.index(40))

# output:
# 0
# 3

# ------------------------------------------------------------------------------------------

# tuple unpacking

student=("dolly",20,'python')
name,age,course=student
print(name)
print(age)
print(course)

# dolly
# 20
# python

# ------------------------------------------------------------------------------------------------

                                                                # Set

#----------------------------------------------------------------------------------------------------------- 
# A set stores unique values
# A set:
#    -does not allow duplicates
#    -is unordered
#    -is mutable
#    -does not support indexing


number={10,20,30}
print(number)

# output:
# {10, 20, 30}

number={10,20,30,20,10}
print(number)   #it remove duplicate value 

# output:
# {10, 20, 30}


# ---------------------------------------------------------------------------------------------------

# does not support indexing:

number={10,20,30}
print(number[0])

# TypeError: 'set' object is not subscriptable

# -------------------------------------------------------------------------------------

# set methods:

# add()
# Adds an element to the set

number={10,20,30,40}
number.add(50)
print(number)

# output:
# number={10,20,30,40}
# number.add(50)
# print(number)

# -------------------------------------------------------------------------------------------------

# remove:
 
number={10,33,23,54}
number.remove(33)
print(number)

# output:
# {10, 54, 23}

# if the element doesn't exist, remove() gibes an error

# ---------------------------------------------------------------------------------------

# discard()
# Remove the specified item

number={10,23,45,66}
number.discard(66)
number.discard(76)  # no error even if 76 doesn't exist
print(number)

# output:
# {10, 45, 23}

# --------------------------------------------------------------------

# clear()
# Removes all the elements from the set

number={19,23,45,74}
number.clear()
print(number)

# output:
# set()

# ---------------------------------------------------------------------------------------

# pop()
# Removes an element from the set

number={21,34,54,78}
number.pop()
print(number)

# putput:
#{34, 21, 78}  
# 
# ----------------------------------------------------------------------------------------------

# difference() or -
# Returns a set containing the difference between two or more sets

a={1,2,3,4}
b={3,4,5,6}

print(a-b)
print(a)  #difference() methods doesn't update in the main set
# or you can write it using difference()
print(b.difference(a))

# output
# {1, 2}
# {1, 2, 3, 4}
# {5, 6}

# --------------------------------------------------------------------------------

# difference_update() or -=
# Removes the items in this set that are also included in another, specified set

a={1,2,3,4}
b={3,4,5,6}
a.difference_update(b) #update directly in the main set
print(a)

# output
# {1, 2}

# -----------------------------------------------------------------------------------------

# symmetric_difference() or ^
# return a sets of elements that are in either set but not both

a={1,2,3,4}
b={3,4,5,6}
print(a^b)
print(b.symmetric_difference(a))
print(a)         # doesn't update in the main set
print(b)

# output:
# {1, 2, 5, 6}
# {1, 2, 5, 6}
# {1, 2, 3, 4}
# {3, 4, 5, 6}

# symmetric_difference_update() or ^=
# Inserts the symmetric differences from this set and another

a={1,2,3,4}
b={3,4,5,6}
a.symmetric_difference_update(b) # directly update in the main set
print(a) 

# output:
# {1, 2, 5, 6}


# -----------------------------------------------------------------------------------------

# union() or |
# Return a set containing the union of sets

a={1,2,3,4}
b={3,4,5,6}
print(a|b)
print(b.union(a))


# output:
# {1, 2, 3, 4, 5, 6}
# {1, 2, 3, 4, 5, 6}

# ------------------------------------------------------------------------------------------

# intersection() or &
#  return the common elements of two or more sets.

a={1,2,3,4}
b={3,4,5,6}
print(a.intersection(b))
print(a&b)

# output:
# {3, 4}
# {3, 4}

# ---------------------------------------------------------------------------------------------------

# isdisjoint()
# 	Returns boolean value for whether two sets have a intersection or not

a={1,2,3,4}
b={3,4,5,6}
c={7,8}
print(a.isdisjoint(b))
print(a.isdisjoint(c)) 

# output:
# False
# True

# ----------------------------------------------------------------------------------------------

# issubset() or <=
# Returns True if all items of this set is present in another set

a={1,2,3,4}
b={3,4}
c={1,2,3,4}
print(b.issubset(a))
print(c<=a)

# output:
# True
# True


# ---------------------------------------------------------------------------------------------------------

# issuperset() or >=
# 	Returns True if all items of another set is present in this set

a={1,2,3,4}
b={3,4}
c={1,2,3,4}
print(a.issuperset(b))
print(a>=c)

# output:
# True
# True

# ------------------------------------------------------------------------------------------------------------------

                                                        # dictonary:

# ----------------------------------------------------------------------------------------------------------------------
#  a dictionary store data as key:value pair 
# it use key to acces a value

student={}
print(type(student))

#output:
#  <class 'dict'>

student={
    'name':'dolly',
    'age':20,
    'course':'python'
}
print(student)

# output:
# {'name': 'dolly', 'age': 20, 'course': 'python'}

# -----------------------------------------------------------------------------------------------

# accesing value using its key

student={
    'name':'dolly',
    'age':20,
    'course':'python'
}
print(student['name'])
print(student['age'])

# output:
# dolly
# 20

# ------------------------------------------------------------------------------------------------------

# add dictionary key:values pair

# adding key:values pair

student={
    'name':'dolly',
    'age':20,
    'course':'python'
}

student['city']='odisha'
print(student)

# output:
# {'name': 'dolly', 'age': 20, 'course': 'python', 'city': 'odisha'}

# --------------------------------------------------------------------------------------------

# updating value 

student={
    'name':'dolly',
    'age':20,
    'course':'python'
}
student['age']=21
print(student)

# output:
# {'name': 'dolly', 'age': 21, 'course': 'python'}


# ------------------------------------------------------------------------------------------------------

# deletting dictionary data

# pop()
# Removes the element with the specified key

student={
    'name':'dolly',
    'age':20,
    'course':'python',
    'city':'odisha'
}
student.pop("course")
print(student)

# output:
# {'name': 'dolly', 'age': 20, 'city': 'odisha'}

# popitem()
# Removes the last inserted key-value pair

student={
    'name':'dolly',
    'age':20,
    'course':'python',
    'city':'odisha'
}
student.popitem()
print(student)

# output:
# {'name': 'dolly', 'age': 20, 'course': 'python'}

# ------------------------------------------------------------------------------------------------------------------------

# del
# delete the specific pair 

student={
    'name':'dolly',
    'age':20,
    'course':'python',
    'city':'odisha'
}
del student['city']
print(student)

# output:
# {'name': 'dolly', 'age': 20, 'course': 'python'}

# ------------------------------------------------------------------------------------------------------------

# clear()
# Removes all the elements from the dictionary

student={
    'name':'dolly',
    'age':20,
    'course':'python',
    'city':'odisha'
}
student.clear()
print(student)

# output:
# {}

# --------------------------------------------------------------------------------------------------------------

# Dictionary Methods

# keys()
# Returns a list containing the dictionary's keys

student={
    'name':'dolly',
    'age':20,
    'course':'python',
    'city':'odisha'
}
print(student.keys())

# output:
# dict_keys(['name', 'age', 'course', 'city'])

# --------------------------------------------------------------------------------------------------------

# values()
# Returns a list of all the values in the dictionary

student={
    'name':'dolly',
    'age':20,
    'course':'python',
    'city':'odisha'
}
print(student.values())

# output:
# dict_values(['dolly', 20, 'python', 'odisha'])

# --------------------------------------------------------------------------------------------------------

# items()
# 	Returns a list containing a tuple for each key value pair

student={
    'name':'dolly',
    'age':20,
    'course':'python',
    'city':'odisha'
}
print(student.items())

# output:
# dict_items([('name', 'dolly'), ('age', 20), ('course', 'python'), ('city', 'odisha')])

# ----------------------------------------------------------------------------------------------------------------

# update()
# updates the dictionary with the specified key-value pairs

student={
    'name':'dolly',
    'age':20,
    'course':'python'
}
student.update({'city':'odisha'})
print(student)

# output:
# {'name': 'dolly', 'age': 20, 'course': 'python', 'city': 'odisha'}

# ----------------------------------------------------------------------------------------------------------------

# get()
# Returns the value of the specified key

student={
    'name':'dolly',
    'age':20,
    'course':'python',
    'city':'odisha'
}
print(student.get('city'))
print(student.get('collage'))  # return none if key doesn't exist or a default value.
print(student.get('collage','pes')) # return default value if key does't exist in the dictionary

# output:
# odisha
# None
# pes

#  difference between student['collage'] and student.get['collage] is that:
# [] raises an error if the key doesn't exist
# get( return none or default values)
# ---------------------------------------------------------------------------------------------------------------------------

# Loop Through Dictionary

# looping through key

student={
    'name':'dolly',
    'age':20,
    'course':'python',
    'city':'odisha'
}
for key in student:
    print(key)

# output:
# name
# age
# course
# city

# ---------------------------------------------------------------------------------------------------------

# looping through values

student={
    'name':'dolly',
    'age':20,
    'course':'python',
    'city':'odisha'
}
for value in student.values():
    print(value)

# output
# dolly
# 20
# python
# odisha

# -------------------------------------------------------------------------------------------------------------

# key:value pair

student={
    'name':'dolly',
    'age':20,
    'course':'python',
    'city':'odisha'
}
for key,value in student.items():
    print(key,":",value)

# output:
# name : dolly
# age : 20
# course : python
# city : odisha

# ----------------------------------------------------------------------------------------------------------------------------

# Dictionary Keys

# Dictionary keys must be hashable
# you can use tuple as key

student={
    'name':'dolly',
    'age':20,
    (1,2):'tuple'
}
print(student)

# output:
# {'name': 'dolly', 'age': 20, (1, 2): 'tuple'}

# you can use list as values but you cannot use a list as key

student={
    'name':'dolly',
    'age':20,
    [1,2]:'tuple'
}
print(student)

# output:
# TypeError: unhashable type: 'list'

# -----------------------------------------------------------------------------------------------------

# Dictionary + List

student_marks={
    'dolly':[98,95,89],
    'adiba':[88,91,90],
    'dipti':[56,39,59]
}
print(student_marks['dolly'])
print(student_marks['dolly'][0])

# output:
# [98, 95, 89]
# 98

# -----------------------------------------------------------------------------------------------------------------

# Nested Dictionary

students_detail={
    'dolly':{
        'age':20,
        'mark':97,
        'course':'python'
    },
    'anu':{
        'age':23,
        'mark':85,
        'course':'R'
    }
}

print(students_detail['anu'])
print(students_detail['dolly']['mark'])

# output:
# {'age': 23, 'mark': 85, 'course': 'R'}
# 97
# ---------------------------------------------------------------------------------------------------------------------

# create a tuple :
# Print:
# first element
# last element
# length

t=(10,20,30,40,50)
length=len(t)
print("first element:",t[0])
print("second element:",t[length-1])
print("length:",length)

# output:
# first element: 10
# second element: 50
# length: 5


# Given:
# number=[10, 20, 20, 30, 30, 40, 40, 50]
# Remove duplicates using a set.

number=[10,20,20,30,20,40,40,50]
number=set(number)
print(number)

# output:
# {40, 10, 50, 20, 30}



# Find common elements

a = {10, 20, 30, 40}
b = {30, 40, 50, 60}
print("common:",a&b)

# output:
# common: {40, 30}


#Frequency Counter
#  given:

a = {10, 20, 30, 40}
b = {30, 40, 50, 60}
print("common:",a&b)

numbers = [10, 20, 10, 30, 20, 10, 40]
frequency={}
for i in numbers:
    if i in frequency:
        frequency[i]+=1
    else:
        frequency[i]=1

for num in frequency:
    print(num,"->",frequency[num])

# output:
# 10 -> 3
# 20 -> 2
# 30 -> 1
# 40 -> 1

# Character Frequency
# given:
text = "programming"
frequency={}
for i in text:
    if i in frequency:
        frequency[i]+=1
    else:
        frequency[i]=1

for i in frequency:
    print(i,"->",frequency[i])

# output:
# p -> 1
# r -> 2
# o -> 1
# g -> 2
# a -> 1
# m -> 2
# i -> 1
# n -> 1


# find duplicate:
# given:
number=[10,20,30,20,20,10]
frequency={}
for i in number:
    if i in frequency:
        frequency[i]+=1
    else:
        frequency[i]=1

for i in frequency:
    if frequency[i]>=2:
        print(i)

# output:
# 10
# 20

# First Non-Repeating Character
text="aabbcdeeff"
frequency={}
for i in text:
    if i in frequency:
        frequency[i]+=1
    else:
        frequency[i]=1
for i in frequency:
    if frequency[i]==1:
        print(i)
        break

# output:
# c


# Student Marks Dictionary
# Find:
# Total marks
# Average
# Highest mark
# Lowest mark
# Student with highest marks
# Students scoring above 80
student= {
    "dolly": 99,
    "khushi": 92,
    "dipti": 78,
    "nandini": 95
}
total_mark=0
length=0
highest=student['dolly']
lowest=student['dolly']
student_above_80=[]
for i in student.values():
    total_mark+=i
    length+=1
    if i>highest:
        highest=i
    if i<lowest:
        lowest=i

for i in student:
    if student[i]==highest:
        student_highest=i
    if student[i]>=80:
        student_above_80.append(i)

print("total mark:",total_mark)
print("average:",total_mark/length)
print("highest mark:",highest)
print("lowest mark:",lowest)
print("student with highest mark:",student_highest)
print("student scoring above 80:",student_above_80)

# output:
# total mark: 364
# average: 91.0
# highest mark: 99
# lowest mark: 78
# student with highest mark: dolly
# student scoring above 80: ['dolly', 'khushi', 'nandini']