# python programming practice----
# Day 10
# ------------------------------------------------------------------------------

# File Handling, CSV & JSON
#  Topics Learned
#  -   File Handling
#  -   open()
#  -   Read files
#  -   Write files
#  -   Append files
#  -   with open()
#  -   read()
#  -   readline()
#  -   readlines()

#  -   CSV files
#  -   csv.reader()
#  -   csv.DictReader()
#  -   Writing CSV files

#  -   JSON
#  -   json.dumps()
#  -   json.loads()
#  -   json.dump()
#  -  json.load()
#  -   File exception handling

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# File Handling Fundamentals
# What is file handling?
# File handling means using Python to store, retrieve, and manage information in files
# Without files, data stored in variables normally disappears when the program ends. Files allow us to save data for future use

# Where is file handling used?
        # Saving user information
        # Reading datasets
        # Storing application settings
        # Saving logs and errors
        # Loading ML model configurations
        # Reading CSV datasets for machine learning
        # Sending and receiving JSON through REST APIs
        # Loading documents for RAG applications

# syntax:
file = open("filename.txt", "mode")
#    perform file operations
file.close()

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# What is a file path?
# A file path tells Python where a file is located
# There are two main types:
# relative path: a relative path is based on the program's current working directory
# absolute path: an absolute path specifies the complete location

# to chexk current working directry:

import os 
print(os.getcwd())

# C:\Users\dolly\OneDrive\Desktop\career preparation

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# What is a file object?

# when you open a file , python gives you a file object. you use this object to read or write data

file=open("data.txt","r")
print(file)
print(type(file))
file.close()

# the file object provides methods such as:
# read()
# readline()
# readlines()
# write()
# writelines()
# seek()
# tell()
# close()

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# file modes
# the mode tells python what you want t do with the file
#  "r"  : read : raises FileNotFindFoundError if file doesn't exist
#  "w"  : write, replaces existing content : create file if file doesn't exist
#  "a"  : append at the end :  create file if file doesn't exist
#  "x"  : create a new file : creates file and gives error if it already exists
#  "rd" : read binary data  : raise error if file doesn't exist
#  "wb" : write binary data : create file if file doesn't exist
#  "r+" : read and write :  raise error if file doesn't exist
#  "w+" : read and write truncates file : create file if file doesn't exist
#  "a+" : read and append : creates file if file doesn't exist



# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# read mode-"r"
# reads a files but if file does not exist, python raise FileNotFoundError
file=open("data.txt","r")
content=file.read()
print(content) 

# output:
# hi my name is dolly
# how are you?

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# write mode- "w"
# writes to a file but if the file already contains information, "w" erases the old content before writing (we call it overwrites)
# create a file if the file doesn't exist

file=open("data.txt","w")
file.write("hello python")   # content changed
file.close() 

# before:
# hi my name is dolly
# how are you?

# after execution
# hello python

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# append-"a"
# append adds content at the end insted of replacing the existing content
# create a file if file doesn't exist

file=open("data.txt","a")
file.write("\nhello myself dolly")
file.close()

# before:
# hello python

# after:
# hello python
# hello myself dolly

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# exclusive creation-"x"
# create a file ,if the file already exist python raise FileExistError
# this is useful when you want to avoid accidently overwriting an existing file

file=open("new_file.txt","x")
file.write("new file created")
file
file.close()

# new_file.txt created

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# understanding + in file modes

# the + symbol allows both reading and writing

file=open("data.txt","r+")
content=file.read()
print(content)
file.write("\nupdated")
file.close()

# read:
# hello python
# hello myself dolly

# after write:
# hello python
# hello myself dolly
# updated

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# reading fies
# read()--read the entire file
# create a file name data.txt or with any othe name in the current working directory
# supose my data.txt file contains :
# hello 
# myself dolly behera
# we are learning python

file=open("data.txt","r")
content=file.read()
print(content) 
file.close()

# output:
# hello          
# myself dolly behera
# we are learning python

# Reading consumes the content from the current file position
# Calling read() again at the end normally returns an empty string

file=open("data.txt", "r")
print(repr(file.read()))
print(repr(file.read()))
file.close()

# output:
# 'hello\nmyself dolly behera\nwe are learning python '
# ''


# you can specify the number of character to read:

file=open("data.txt","r")
content=file.read(12)
print(content)
file.close()

# output:
# hello
# myself


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# readline() — Read one line

file=open("data.txt","r")
line1=file.readline()
line2=file.readline()
print(line1)
print(line2)
file.close()

# output:
# hello

# myself dolly behera


# Each call reads the next line
# A newline character (\n) may be included in the returned string
# To remove surrounding whitespace:

file=open("data.txt","r")
line1=file.readline()
line2=file.readline()
print(line1.strip())
print(line2.strip())
file.close()

# output:
# hello
# myself dolly behera

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# readlines() — Read all lines into a list

file=open("data.txt","r")
lines=file.readlines()
print(lines)
file.close()

# output:
# ['hello\n', 'myself dolly behera\n', 'we are learning python ']

# You can process the lines:

file=open("data.txt","r")
lines=file.readlines()
for i in lines:
    print(i.strip())
file.close()

# output:
# hello
# myself dolly behera
# we are learning python

# readlines() is convenient for small files
#  for very large files, iterating over the file is usually more memory efficient

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# reading a file using loop

file=open("data.txt","r")
for line in file:
    print(line.strip())
file.close()

# hello
# myself dolly behera
# we are learning python


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Writing and Appending

# write()
# the write() method writes a string to a file
# write() methods under "w" mode write new content after earesing old content (overwrites)

file=open("notes.txt","w")         #create a file notes.txt if it don't have any file named notes.txt
file.write("i am learning python")  # write this in the text file
file.close()

# new file create named notes.txt
# it content text that is:
# i am learning python

# write() does not automatically add a new line

# to add new line:

file=open("notes.txt","w")   #file exist with some content in it
file.write("python\n")
file.write("machine learning\n")
file.write("AI engineering\n") 
file.close()

# before:
# i am learning python

# after: (replace the old content wih new one)
# python
# machine learning
# AI engineering


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# writelines()
# writelines() writes multiple string from an iterable
# writelines() does not automatically add newline characters

language=["sql\n","react\n","R"]
file=open("notes.txt","w")
file.writelines(language)
file.close()

# before:
# python
# machine learning
# AI engineering

# after:
# sql
# react
# R

# without newline characters output will be like: 
# sqlreactR
# so inclue \n when you want separate lines

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Append without losing existing content
# Use "a" when you want to add new information to an existing file

file=open("notes.txt","a")
file.write(" "+"Language")
file.write("\n rag")
file.close()

# before
# sql
# react
# R


#after appending:
# sql
# react
# R Language   #Language is added after space
# rag           # rag is added after newline character


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# with open() and Context Managers

# you may write
file=open("data.txt","r")
try:
    content=file.read()
finally:
    file.close()

# but python offer a simple approach:

with open("data.txt","r") as file:
    content=file.read()
print(content)

# when the with block finish, python close the file automatically,even if an exception occurs inside the block
# this pattern is called a context manager
        # Prevents files from being left open
        # Makes code shorter
        # Helps manage resources safely
        # Is the standard style for file handling in Python

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# File Pointer: tell() and seek()

# file pointer:
# when python read or write a files, it keeps track of the current position.
# this is often called file pointer or file position

# tell()
# get the current position

with open("data.txt","r") as file:
    print("current position before reading:",file.tell())    #current position 0
    file.read(3)          #read three character pointer is at 3
    print("current position after reading:",file.tell())     #current position 3

# output:
# current position before reading: 0
# current position after reading: 3


# seek()
# change the position

with open("data.txt","r") as file:
    print(file.read(3))    # current position after reading:3
    file.seek(0)           #change position to 0 again
    print(file.read(3))    #again read from 0 position to 3

# output:
# hel
# hel


with open("data.txt","r") as file:
    print("read first 3 character:",file.read(3))
    print("current position after reading first three character:",file.tell())
    file.seek(0)
    print("current position after changing position to 0 using seek:",file.tell())
    print("again read the firdt 3 character because the current position is at 0 : ",file.read(3))

# output:
# read first 3 character: hel
# current position after reading first three character: 3
# current position after changing position to 0 using seek: 0
# again read the firdt 3 character because the current position is at 0 :  hel

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Encoding and Newlines

# what is encoding?
# encoding is the process of converting text into bytes when saving it to a file 
# and converting those bytes back into readable text when reading the file
# for general text files, explicitly using UTF-8 is a good habbit
# this is useful when your file cointain different language or special characters.

with open("data.txt","w",encoding="utf-8") as file:
    file.write("Hello, Guys! नमस्ते")

with open("data.txt","r",encoding="utf-8") as file:
    print(file.read())

# output:
# Hello, Guys! नमस्ते

# Why does newline="" appear in CSV code?
# The newline="" argument lets Python's CSV module manage newline handling
# It helps avoid unwanted blank lines in CSV files, particularly on Windows

with open("student.csv","w",newline="",encoding="utf-8"):
    ...

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Exception Handling with Files
# handle a missing file
try:
    with open("data.txt","r",encoding="utf-8")as f:
        content=file.read()
        print(content)
except FileNotFoundError:
    print("the file does not exist")

# if file exist ,read the file
# if file doesn't exist ..print the except part


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Handle permission errors

try:
    with open("secret.txt","r",encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("you do not have the permission to read this file")

# if file exist and have permission to read the file then read it
# if the file doesn't exist print file not found
# if file exist but don't have the permission to  read it. it will print(you don't have the permission to read this file)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------\

# Handle invalid JSON later in the pipeline

import json
try:
    with open("student.json","r",encoding="utf-8") as f:
        data=json.load(f)
except FileNotFoundError:
    print("JSON file not found")
except json.JSONDecodeError:
    print("the JSON file contain invalid JSON")



# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# CSV Files
#  CSV stand for Comma-Separated Values
# a CSV stores tabular data in row and columns

# example
# Name,Age,Marks
# Dolly,20,89
# Adiba,22,93
# Anu,23,96

# csv file are widely used for datasets,spreadsheeets,and data analysis.
# python have a built-in csv module.
import csv

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# read CSV using csv.reader()

import csv
with open("students.csv","r",newline="",encoding="utf-8") as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)

# ['Name', 'Age', 'Marks']
# ['Dolly', '20', '89']
# ['Adiba', '22', '93']
# ['Anu', '23', '96']
# Each row is a list of strings

# Skip the header
# next(reader) consumes the first row,which is the header.

import csv
with open("students.csv","r",newline="",encoding="utf-8") as file:
    reader=csv.reader(file)
    header=next(reader)
    for row in reader:
        print(row)

# output:
# ['Dolly', '20', '89']
# ['Adiba', '22', '93']
# ['Anu', '23', '96']


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Read CSV using csv.DictReader()
#  DictReader reads each row as a dictionary, using the header names as keys

import csv
with open("students.csv","r",newline="",encoding='utf-8') as file:
    reader=csv.DictReader(file)
    for row in reader:
        print(row)

# # output:
# {'Name': 'Dolly', 'Age': '20', 'Marks': '89'}
# {'Name': 'Adiba', 'Age': '22', 'Marks': '93'}
# {'Name': 'Anu', 'Age': '23', 'Marks': '96'}


import csv
with open("students.csv","r",newline="",encoding='utf-8') as file:
    reader=csv.DictReader(file)
    for row in reader:
        print(row['Name'],row['Age'])

# Dolly 20
# Adiba 22
# Anu 23

# the values are still strings, so convert them when you need numeric calculation

marks=int(row["marks"])


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Calculate average marks from CSV

import csv
total=0
count=0

with open("students.csv","r",newline="",encoding="utf-8") as file:
    reader=csv.DictReader(file)

    for row in reader:
        total+=int(row["Marks"])
        count+=1
if count>0:
    average=total/count
    print("average :",average)
else:
    print("no student record found")

# average : 92.66666666666667


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Write a CSV file

import csv
students=[
    ["dolly",20,90],
    ['khushi',21,89],
    ['agrima',23,67]
]
with open("student.csv","w",newline="",encoding="utf-8")as file:
    writer=csv.writer(file)

    writer.writerow(["Name","Age","Marks"])
    writer.writerows(students)

# before:
# Name,Age,Marks
# Dolly,20,89
# Adiba,22,93
# Anu,23,96

# after
# # Name,Age,Marks
# dolly,20,90
# khushi,21,89
# agrima,23,67


# writerow() writes one row
# writerows() writes multiple rows


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Append to a CSV file
import csv
with open("students.csv","a",newline="",encoding="utf-8") as file:
    writer=csv.writer(file)
    writer.writerow(["saniya",22,32])

# before:
# Name,Age,Marks
# dolly,20,90
# khushi,21,89
# agrima,23,67

# after:
# Name,Age,Marks
# dolly,20,90
# khushi,21,89
# agrima,23,67
# saniya,22,32



# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# JSON:
# Json stands for javaScriot Onject Notation
# it is a text based format used to store and exchange structured data

# example:
#         {
#            "name":"dolly",
#            "age": 20,
#            "course":["python","machine Learning","AI"],
#             "is_student": true
#          }

# JSON stores data  using key-value pairs,arrays,strings,numbers,boolean value and null

# Where is JSON used?

# REST APIs — sending and receiving data
# FastAPI — accepting requests and returning responses
# RAG applications — storing metadata about documents and chunks
# Configuration files — storing application settings
# AI/ML applications — exchanging prediction results

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# JSON vs Python dictionary
# they look similar, but they are not the same

# python dictionary:
student = {
    "name": "Dolly",
    "age": 20,
    "is_student": True,
    "nickname": None
}

# JSON representation:
{
    "name": "Dolly",
    "age": 20,
    "is_student": true,
    "nickname": null
}

# differences: 
#      python                          JSON
#      ---------------------------------------
#       True                            true
#       False                           false
#       None                            null
#   " "or ' ' for string           " " only for string
#       dictionary                      object


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# import the JSON module
# python includes a built-in json module

import json

# the four main methodes are
# json.dumps()          -python object---->JSON string
# json.loads()          -JSON string------> python object
# json.dump()           -write python object to JSON file
# json.load()           -read JSON from file


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# json.dumps()----python to ISON string

import json
student={
    "name":"dolly",
    "age": 20,
    "marks":90
}

data=json.dumps(student)
print(data)
print(type(data))

# {"name": "dolly", "age": 20, "marks": 90}
# <class 'str'>

# pretty -print using indent
# intent=4 makes the JSON easier for humans to read

import json
student={
    "name":"dolly",
    "age": 20,
    "course":["python","machine Learning","AI"]
}

data=json.dumps(student,indent=4)
print(data)
print(type(data))

# output:
#  {
#     "name": "dolly",
#     "age": 20,
#     "course": [
#         "python",
#         "machine Learning",
#         "AI"
#     ]
# }
# <class 'str'>


# sort keys
# sort_keyd=True sorts the dictionary keys in the output

import json

data = {
    "zebra": 1,
    "apple": 2,
    "mango": 3
}

print(json.dumps(data, sort_keys=True))

# output:
# {"apple": 2, "mango": 3, "zebra": 1}


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# json.loads()----JSON string to python
# loads() converts a JSON-formatted string into a python object
# 
import json
data='{"name":"dolly", "age":20, "mark":90}'
student=json.loads(data)
print(student)
print(type(student))
print(student["name"]) 

# output:
# {'name': 'dolly', 'age': 20, 'mark': 90}
# <class 'dict'>
# dolly

# after conversion to dictionary you can acces using dictionary keys

# example with JSON array 
import json
data='["python", "machine learning", "AI"]'  #JSON array
skills=json.loads(data)
print(skills)
print(type(skills))
print(skills[1])

# output:
# ['python', 'machine learning', 'AI']          ##python list
# <class 'list'>
# machine learning

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# json.dump() ------save data to file
# use dump() when you want to save a python object directly into a JSON file

import json
student={
    "name":"dolly",
    "age": 20,
    "course":["python","machine Learning","AI"]
}

with open("student.json","w",encoding="utf-8") as file:
    json.dump(student,file,indent=4)

# the file student now contain:
# {
#     "name": "dolly",
#     "age": 20,
#     "course": [
#         "python",
#         "machine Learning",
#         "AI"
#     ]
# }


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# json.load()---read data from a file
# use load() to read from a file, convert it into a python object

import json
with open("student.json","r",encoding="utf-8") as file:
    student=json.load(file)
print(student)
print(student["name"])
print(student["course"])

# output:
# {'name': 'dolly', 'age': 20, 'course': ['python', 'machine Learning', 'AI']}
# dolly
# ['python', 'machine Learning', 'AI']

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#                                           practice:
# ------------------------------------------------------------

# Create student.txt and write:

# Name: Dolly
# Course: Python
# Goal: AI/ML Engineer

# Then read and print it

data=["Name: Dolly\n","Course: Python\n","Goal: AI/ML Engineer"]
with open("student.txt","w") as f:
    file.writelines(data)
with open("student.txt","r") as f:
    content=file.read()
    print(content)

# i don't have any file name student.txt so it automatically create student.txt and write content that was given
# then read it

# output:
# Name: Dolly
# Course: Python
# Goal: AI/ML Engineer



# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Create a file containing:

# Python
# Java
# C++
# SQL

# Read it line by line.

with open("course.txt","w") as f:
    f.write("Python\n")
    f.write("Java\n")
    f.write("C++\n")
    f.write("SQL")
with open("course.txt","r") as f:
    for i in f:
        print(i.strip())

# output:
# Python
# Java
# C++
# SQL


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Append:

# Machine Learning
# Deep Learning

# without deleting the existing content.

with open("course.txt","a") as file:
    file.write("\nMachine Learning")
    file.write("\nDeep Learning")

# now course.txt contain:
# Python
# Java
# C++
# SQL
# Machine Learning
# Deep Learning

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Create:
# students.csv

# with:
# Name,Marks
# Dolly,90
# Khushi,85
# Dipti,88
# Nandini,95

# Read the file and print:

# Dolly → 90
# Khushi → 85
# ...

import csv
data=[
    ["Dolly",98],
    ["Khushi",86],
    ["Dipti",33],
    ["namdini",55]
]
with open("students.csv","w",newline="",encoding="utf-8") as file:
    write=csv.writer(file)
    write.writerow(["Name","Marks"])
    write.writerows(data)

with open("students.csv","r",newline="",encoding="utf-8") as file:
    content=csv.DictReader(file)
    for i in content:
        print(i["Name"],"->",i["Marks"])

# output:
# Dolly -> 98
# Khushi -> 86
# Dipti -> 33
# namdini -> 55

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Create:

# student = {
#     "name": "Dolly",
#     "age": 20,
#     "skills": ["Python", "Git", "AI"]
# }

# Save it to:

# student.json

# Then read it back

import json
student={
    "name":"dolly",
    "age":20,
    "skills":["python","git","AI"]
}
with open("student.json","w",encoding="utf-8") as file:
    write=json.dump(student,file,indent=4)
with open("student.json","r",encoding="utf-8") as file:
    read=json.load(file)
    print(read)

# output:
# {'name': 'dolly', 'age': 20, 'skills': ['python', 'git', 'AI']}
    
    


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Create a program that stores student information in a JSON file.

# Menu:

# 1. Add student
# 2. View students
# 3. Search student
# 4. Exit

# Example JSON:

# [
#     {
#         "name": "Dolly",
#         "marks": 90
#     },
#     {
#         "name": "Khushi",
#         "marks": 85
#     }
# ]

# This is a good small project because it combines:

# Functions + Lists + Dictionaries + JSON + Exception Handling

import json
def add_student():
    name=input("enter name: ")
    marks=float(input("enter marks: "))
    try:
       with open("students.json","r",encoding="utf-8") as file:
           students=json.load(file)
    except (FileNotFoundError,json.JSONDecodeError):
        students=[]
    students.append({"Name":name,"Marks":marks})

    with open("students.json","w",encoding="utf-8") as file:
        json.dump(students,file,indent=4)
    print("student data added successfuly")


     
def view_students():
        try:
            with open("students.json","r",encoding="utf-8") as file:
                students=json.load(file)
                for student in students:
                    print(student["Name"],",",student["Marks"])
        except FileNotFoundError:
            print("no student found")

def search_student():
    try:
        name=input("enter the name: ")
        with open("students.json","r",encoding="utf-8") as file:
            students=json.load(file)
        for student in students:
            if student["Name"].lower()==name.lower():
                print(student)
                return
        print("student not found")
    except FileNotFoundError:
        print("no student found")
        

while True:
    print("\n 1. add student")
    print(" 2. view students")
    print(" 3. search student")
    print(" 4. exit")
    try:
            choice=int(input("enter your choice:"))

            if choice==1:
                add_student()
            elif choice==2:
                view_students()
            elif choice==3:
                search_student()
            elif choice==4:
                break

    except ValueError:
                print("invalid choice")
                continue


    

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------