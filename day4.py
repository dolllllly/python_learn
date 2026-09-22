#  python programming practice----
# Day 4
# ----------------------------------------------------------
# - Creating lists
# - List indexing
# - Positive and negative indexing
# - List slicing
# - Updating list elements
# - `append()`
# - `insert()`
# - `extend()`
# - `remove()`
# - `pop()`
# - `clear()`
# - `del`
# - `in` and `not in`
# - `len()`
# - `sort()` vs `sorted()`
# - `reverse()`
# - Looping through lists
# - Lists with conditions
# - Nested lists 
# - List copying

# ------------------------------------------------------------------------------------------------------------------

# creating list
fruit=["appple","banana","orange"]
print(fruit)

# output:
# ['appple', 'banana', 'orange']


# empty list

items=[]
print(items)

# output
# []

# --------------------------------------------------------------------------------
#
# indexing

#    0       1        2
# apple   banana   orange

fruit=["apple","banana","orange"]
print(fruit[0])
print(fruit[1])
print(fruit[2])

# output:
# appple
# banana
# orange

# ----------------------------------------------------------------------------
# Negative Indexing

# apple   banana   orange
#   -3       -2        -1

fruits = ["apple", "banana", "orange"]
print(fruits[-1])
print(fruits[-2])
print(fruits[-3])

# output
# orange
# banana
# apple

# ---------------------------------------------------------------------------------------------------------

# Slicing

numbers = [10, 20, 30, 40, 50]
print(numbers[1:4])


# output
# [20, 30, 40]

print(numbers[::-1])

# output
# [50, 40, 30, 20, 10]

print(numbers[-1:-6:-1])

# [50, 40, 30, 20, 10]

print(numbers[0:5:2])

# [10, 30, 50]

print(numbers[-2:0:-1])

# [40, 30, 20]

# --------------------------------------------------------------------------------------------------

# Updating Elements : Lists are mutable.

numbers = [10, 20, 30]
numbers[1] = 200
print(numbers)

# output:
# [10, 200, 30]

fruits = ["apple", "banana", "orange"]
fruits[1]="guava"
print(fruits)

# output
# ['apple', 'guava', 'orange']

# ---------------------------------------------------------------------------------------------

# append()
# Adds an element at the end

numbers = [10, 20, 30]
numbers.append(40)
print(numbers)

# output:
# [10, 20, 30, 40]

numbers.append([50,60])
print(numbers)

# output
# # output:
# [10, 20, 30, 40, [50,60]]

# ---------------------------------------------------------------------------------

# insert()
# Adds an element at a specific position

number=[10,20,30,50]
number.insert(3,40)
print(number)

# output
# [10, 20, 30, 40, 50]


# ---------------------------------------------------------------------------------

# extend()
# Adds multiple elements

a = [1, 2, 3]
a.extend([4, 5, 6])
print(a)

# output:
# [1, 2, 3, 4, 5, 6]

# ---------------------------------------------------------------------------------

# remove()
# Removes the first matching value

numbers = [10, 20, 30, 20]
numbers.remove(20)
print(numbers)

# output:
# [10, 30, 20] 
# remove the first occurance only

# ---------------------------------------------------------------------------------

# pop()
# Removes an element using its index
# wothout index remove the last element

number= [10, 20, 30,40,50]
number.pop()
print(number)

# output:
# [10, 20, 30, 40]

number.pop(2)
print(number)

# output:
# [10, 20, 40]

# ---------------------------------------------------------------------------------

# clear()
# Removes everything

numbers = [10, 20, 30]
numbers.clear()
print(numbers)

#output
#  []

# ---------------------------------------------------------------------------------

# del
# Delete using an index

numbers = [10, 20, 30,40,50]
del numbers[1]
print(numbers)

# Output:
# [10, 30,  40, 50]

# You can also delete a slice

numbers = [10, 20, 30,40,50]
del numbers[0:2]
print(numbers)

# output:
# [30, 40, 50]

# ---------------------------------------------------------------------------------


# in and not in: return True or False

name=["dolly","anu","adiba","khushi"]
print("dolly" in name)

# True

print("sasmi" in name)

# False

print("adiba" not in name)

# False

print("sasmi"not in name)

# True

# ---------------------------------------------------------------------------------

# len()

number=[10, 20, 30, 40]
print(len(number))

# Output:
# 4

# ---------------------------------------------------------------------------------

#sort() & sorted() 
# sort()
# Changes the original list

number=[50, 10, 40, 20]
number.sort()

print(number)

# Output:
# [10, 20, 40, 50]

# sorted()
# Returns a new sorted list

number=[50, 10, 40, 20]
new_number= sorted(number)
print(new_number)
print(number)

# output:
# [10, 20, 40, 50]
# [50, 10, 40, 20]

# ---------------------------------------------------------------------------------

# reverse()

number=[10, 20, 30]
number.reverse()
print(number)

# Output:
# [30, 20, 10]

# ---------------------------------------------------------------------------------

# Looping Through a List


number=[10, 20, 30, 40]
for num in number:
    print(num)

# output:
# 10
# 20
# 30
# 40
# ---------------------------------------------------------------------------------

# List + Conditions

num=[1,2,3,4,5,6,7,8,9]
for i in num:
    if i%2==0:
        print(i) #even number

# output:
# 2
# 4
# 6
# 8


# ---------------------------------------------------------------------------------

# Nested Lists
# A list can contain other lists

matrix=[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[0])
print(matrix[0][2])
print(matrix[2][1])

# output:
# [1, 2, 3]
# 3
# 8

# ---------------------------------------------------------------------------------
# Create a list of 5 fruits and print:
# -First fruit
# -Last fruit
# -Number of fruits

fruits=[]
fruits.append("banana")
fruits.append("orange")
fruits.append("apple")
fruits.append("mango")
fruits.append("guava")
print(fruits)
print("first fruit:",fruits[0])
print("last fruit:",fruits[4])
print("total fruits:",len(fruits))

# output:
# ['banana', 'orange', 'apple', 'mango', 'guava']
# first fruit: banana
# last fruit: guava
# total fruits: 5

# ---------------------------------------------------------------------------------

# Create a list of 10 numbers and print all elements using a loop

list=[1,2,3,4,5,6,7,8,9,10]
for i in list:
    print(i)

# output
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10

# ---------------------------------------------------------------------------------

# Find the sum of all numbers in a list.

list=[1,2,3,4,5,6,7,8,9,10]
sum=0
i=0
while i<len(list):
     sum+=list[i]
     i+=1
print("sum:",sum)

# output
# sum: 55


list=[1,2,3,4,5,6,7,8,9,10]
sum=0
for i in list:
     sum+=i
print("sum:",sum)


# output
# sum: 55

# ---------------------------------------------------------------------------------

# Find the largest number in a list.
list=[39,10,68,39,35]
max=0
for i in list:
    if i>max:
        max=i
print(max)

# output"
# 68

# ---------------------------------------------------------------------------------

# Find the smallest number.

list=[39,10,68,39,35]
small=list[0]
for i in list:
    if i<small:
        small=i
print("smallest:",small)

# output
# 10

# ---------------------------------------------------------------------------------
# Count Even and Odd

list=[39,10,68,39,35]
even=0
odd=0
for i in list:
    if i%2==0:
        even+=1
    else:
        odd+=1
print("even count:",even)
print("odd count:",odd)

# output
# even count: 2
# odd count: 3

# ---------------------------------------------------------------------------------
# Take a list and ask the user for a number.
# Check whether the number exists.
list=[39,10,68,39,35]
num=int(input("enter any number:"))
exist=False
for i in list:
    if i==num:
        exist=True
        break
if exist:
    print(f'{num} exist')
else:
    print(f'{num} doesn\'t exist')

# output:
# enter any number:67
# 67 doesnt exist

# enter any number:10
# 10 exist

# ---------------------------------------------------------------------------------
# Reverse Without reverse()
list=[39,10,68,39,35]
new_list=[]
for i in range(len(list)-1,-1,-1):
    new_list.append(list[i])
print(new_list)

# output:
# [35, 39, 68, 10, 39]

# ---------------------------------------------------------------------------------
# Remove Duplicates

ist=[39,10,68,10,35,10]
new_list=[]

for i in list:
    found=False
    for j in new_list:
        if i==j:
            found=True
        

    if found==False:
        new_list.append(i)
print(new_list)

# output:
# [39, 10, 68, 35]
# ---------------------------------------------------------------------------------

# Frequency
list=[39,10,68,10,35,10,35]
result=[]
for i in list:
    count=0
    for j in list:
        if i==j:
            count+=1
    
    if count>=1 and i not in result:
        result.append(i)
        print(i,"=",count)

# output:
# 39 = 1
# 10 = 3
# 68 = 1
# 35 = 2


# ---------------------------------------------------------------------------------
# Second Largest
list=[39,10,68,39,35]
max=0
second_max=0

for i in list:
    if i>max:
        second_max=max
        max=i
print("largest:",max)
print("second largest:",second_max)

# output:
# largest: 68
# second largest: 39

# ---------------------------------------------------------------------------------
# Second Smallest
numbers = [39, 10, 68, 35, 20]

smallest = numbers[0]
second = numbers[0]

for i in numbers:
    if i < smallest:
        second = smallest
        smallest = i

    elif i < second and i != smallest:
        second = i

print("Smallest:", smallest)
print("Second smallest:", second)

# output:
# Smallest: 10
# Second smallest: 20

# ---------------------------------------------------------------------------------

# Find Duplicates
list=[39,10,68,10,35,10,35]
result=[]
for i in list:
    count=0
    for j in list:
        if i==j:
            count+=1
    if count>=2 and i not in result:
        result.append(i)
        print(i)

# output:
# 10
# 35

# ---------------------------------------------------------------------------------
# Move Zeros

list=[1,0,2,0,4,5,0,6]
result=[]
zero=[]
for i in list:
    if i==0:
        zero.append(i)
    else:
        result.append(i)
result.extend(zero)
print(result)

# output:
# [1, 2, 4, 5, 6, 0, 0, 0]

# ---------------------------------------------------------------------------------
# Separate Even and Odd

list=[1,9,2,3,4,5,8,6]
even=[]
odd=[]
for i in list:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)

print("even list",even)
print("odd list",odd)

# output:
# even list [2, 4, 8, 6]
# odd list [1, 9, 3, 5]

# ---------------------------------------------------------------------------------

# Two Sum: Find the two numbers whose sum is n

list=[1,9,2,3,4,5,8,6]
result=[]
n= int(input("enter the sum total you want: "))
for i in list:
    for j in list:
        if i+j==n and list.index(i)!=list.index(j) and j not in result and j not in result:
            result.append(i)
            result.append(j)
            print(i,j )

# output:
# enter the sum total you want: 10
# 1 9
# 2 8
# 4 6

    

# ---------------------------------------------------------------------------------
# Student Marks Analyzer
# Calculate:
# Total marks
# Average
# Highest mark
# Lowest mark
# Number of students/subjects above 75
# Number below 40
# Number of even marks
# Number of odd marks
# Second highest mark

student_mark=[]
total_subj=int(input("enter total subj:"))
i=1
while i<=total_subj:
    sub=int(input("enter subject mark:"))
    student_mark.append(sub)
    i+=1

lowest_mark=student_mark[0]
highest_mark=0
second_highest=0
even=[]
odd=[]
below_40=[]
total_mark=0
for i in student_mark:
    total_mark+=i
    if i<lowest_mark:
        lowest_mark=i
    if i>highest_mark:
        second_highest=highest_mark
        highest_mark=i 
    elif i>second_highest and i!=highest_mark:
        second_highest=i
    if i<40:
        below_40.append(i)
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
    


print(student_mark)
print("total mark:",total_mark)
print("average:",total_mark/len(student_mark))
print("highest mark:",highest_mark)
print("lowest mark:",lowest_mark)
print("second highest mark:",second_highest)
print("list of mark below 40:",below_40)
print("even mark:",even)
print("number of even mark",len(even))
print("odd mark:",odd)
print("number of odd mark",len(odd))

# output:
# enter total subj:7
# enter subject mark:39
# enter subject mark:89
# enter subject mark:99
# enter subject mark:88
# enter subject mark:92
# enter subject mark:98
# enter subject mark:57
# [39, 89, 99, 88, 92, 98, 57]
# total mark: 562
# average: 80.28571428571429
# highest mark: 99
# lowest mark: 39
# second highest mark: 89
# list of mark below 40: [39]
# even mark: [88, 92, 98]
# number of even mark 3
# odd mark: [39, 89, 99, 57]
# number of odd mark 4
# ---------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------