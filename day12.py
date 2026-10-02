# python programming practice----
# Day 12
# ------------------------------------------------------------------------------
# Object-Oriented Programming (OOP) Basics

## Topics Covered
    # - Classes and objects
    # - __init__()
    # - self
    # - Instance attributes
    # - Instance methods
    # - Class attributes
    # - Class methods
    # - Static methods

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# What is OOP?
# Object-Oriented Programming (OOP) is a programming approach in which code is organized using class and objecs.
# an object can have:
    # attributes: data or variable associated with the object
    # methods: functions associated with object
# for example:a Student object could contain a name, marks,  as attributes and a method to calculate the percentage



# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# What is a class?
# a class is a bluprint for creating objects.
# think of a class as a design for a house.the design describes the house,but it is not an actual house

class student:
    pass

# here :
        # class is the keyword used to defined a class
        # student is the class name
        # pass mean do nthing for now .it allo us ti create an empty class.


# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# what is an object?
# an object is an instance of a class.
# object is created by calling the class 
class student:
    pass
s1=student()
s2=student()
print(s1)
print(s2)

# both variables s1 and s2 refers to onjects created from the student class.
# s1 refers to one object and s2 refers to another object
# even though they come from the same class, they are separate instances

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# what is __init__() method?
# __init__() is a special methods that python call automatically to initialize an object attributes when a new object is created.

class student:
    def __init__(self):
        print("a student object was created")
s1=student()
s2=student()

# output:
# a student object was created
# a student object was created

# 1.python define the student class.
# 2. s1=student() create an object
# 3.python automatically call __init__() for that object.
# the message is printed
# the same process happen when s2 is created.

# we do no need to call __init() ourselves.


# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# what is self?
# self refers to current object.
# it allow each object to store and access its own attributes.

class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
s1=student("anu",23)
s2=student("adiba",22)
print(s1.name)
print(s2.name)

# output:
# anu
# adiba

# what does self.name=name mean?
# self.name is an attribute belonging to the current object
# name is the value receives by the parameter.
# when we write s1=student("anu",23)
# python initilize the object s1 with "anu" and 23
# for the second object s2 ,value are stired separately

# is self a keyword?
# no. self is not a keyword . it is a naming convention that python programmers follow.
# we can use any other name such as 
class student:
    def __init__(this,name):
        this.name=name
# but we should use self because it makes your code redeable and follow standard python practice


# why do we need self?
# without self, a methods would not have a direct referance to the instance whose data needs to access


# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# instance atttributes
# attributes create using self are usually called instance Attribute
# each objects can have its own values.

class student:
    def __init__(self,name,mark):
        self.name=name
        self.mark=mark
s1=student("anu",96)
s2=student("adiba",92)

print(s1.name, s1.mark)
print(s2.name, s2.mark)

# anu 96
# adiba 92

# each object stores its own name and mark

# changing one object's attribute does not automatically change the other object's attribute
    
s2.mark=99
print(s1.name,s1.mark)
print(s2.name,s2.mark)

# anu 96
# adiba 99


# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# instance methods:
# an instance method is a function defined inside a class that works with an individual object.
# it takes self as its first parameter

class studenr:
    def __init__(self,name,mark):
        self.name=name
        self.mark=mark
    def percentage(self):
        return self.mark
    def display(self):
        print(f"{self.name}: {self.percentage()}%")
s1=student("dolly",99)
s1.display()

# output:
# dolly: 99%

# percentage() return the stored mark
# display() use the object's name and call another instance methode.



# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# class attributes:
# class attributes is declared directly inside the class ,but outsidee its methods
# it belong to class and is generally shared by all its objects

class student:
    school="kalinga university"   #class attribute
    def __init__(self,name):
        self.name=name             #instance attribute
s1=student("anu")
s2=student("adiba")

print(s1.name,":",s1.school)
print(s2.name,":",s2.school)
print(student.school)

# you can access it through the class or an object

# instance attributes vs class attributes:
# instance attribute belong to individual object while class attribute belong to class
# instance attribute defined using self inside __init__() while class attribute defined directly inside the class
# in instance attribute ,each object can have its own value while class attribute is shared by all

# s1.name and s2.name are different
# but both object access the same class attribute school

# what happent when you change a class varible?

class student:
    school="kalinga university"   
    def __init__(self,name):
        self.name=name             
s1=student("anu")
s2=student("adiba")

student.school="iit nagpur"

print(s1.name,":",s1.school)
print(s2.name,":",s2.school)
print(student.school)

# output:
# anu : iit nagpur
# adiba : iit nagpur
# iit nagpur

# we changed the class attribute through student.school, both object now access the updaated value


# changing it through an object is different:

class student:
    school="kalinga university"   
    def __init__(self,name):
        self.name=name             
s1=student("anu")
s2=student("adiba")

s1.school="iit nagpur"

print(s1.name,":",s1.school)
print(s2.name,":",s2.school)
print(student.school)

# output:
# anu : iit nagpur
# adiba : kalinga university
# kalinga university

# s1.school="iit nakpur"  python create an instance attribute named school on s1. 
# but it does not change the class attribute.
# now s1 has its own company value, while s2 still access the class value
# this is calles attribute shadowing



# mutable class attribute:
# be careful when using list or dictionaries as class attributes
class Student:
    subjects = []

    def __init__(self, name):
        self.name = name

s1 = Student("anu")
s2 = Student("adiba")
s1.subjects.append("Python")
print(s1.subjects)
print(s2.subjects)

# output:
['Python']
['Python']

# a mutable class attribute is shared by all objects of a class
#  If one object modifies it, the change can be seen by the other objects too

# to overcome this issue:
class Student:
    def __init__(self, name):
        self.name = name
        self.subjects = []


s1 = Student("anu")
s2 = Student("adiba")
s1.subjects.append("Python")
print(s1.subjects)
print(s2.subjects)

# output:
# ['Python']
# []


# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# class method and static methods

# class methods--@classmethod
# a class method works with the class rather than a particular object's data
# it use cls as its first parameter
        # cls refers to the class
        # @classmethod is a decorators that makes a method a class method

class student:
    school="kalinga university"
    @classmethod
    def change_school(cls,new_name):
        cls.school=new_name
s1=student()
s2=student()
print(student.school)
student.change_school("pes university")
print(s1.school)
print(s2.school)

# kalinga university
# pes university
# pes university

# school is a class atribute
# @classmethod makes change_school() a class method
# cls refers to Student
# cls.school = new_school changes the class attribute
# Both objects now access the updated school name
# You can call a class method using either the class or an object, but calling it through the class is clearer when changing class-wide data

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# static method--@staticmethod
# a static method is a method inside a class tht doesnot need access to the object's attributes or the class'attributes
# it does not automatically receive self or clas.

class calculator:
    @staticmethod
    def add(a,b):
        return a+b
    
    @staticmethod
    def multiply(a,b):
        return a*b
print(calculator.add(10,20))
print(calculator.multiply(10,5))

# output:
# 30
# 50

# class method vs static method

class Student:
    school = "Kalinga University"

    @classmethod
    def show_school(cls):
        return cls.school

    @staticmethod
    def welcome():
        return "Welcome to the student portal"


print(Student.show_school())
print(Student.welcome())

# output:
# Kalinga University
# Welcome to the student portal

# The difference is:

# show_school() uses cls to access the class attribute.
# welcome() doesn't need any class or instance data.
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

                                                            # practice
# -----------------------------------------------------------------------------------------------------------------------------------------------

# Student class

# Create a Student class with:
        # name
        # marks (a list of marks)
        # calculate_average()
        # display_result()

# Requirements:
        # Create two students
        # Calculate each student's average
        # Display each student's name and average
        # Handle an empty marks list without a division-by-zero error
class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def calculate_average(self):
        if not self.marks:
            return 0
        return sum(self.marks)/len(self.marks)
    def display_result(self):
        print("name :",self.name)
        print("average :",round(self.calculate_average(),2))
s1=student("anu",[98,85,89])
s2=student("adiba",[96,89,87])
s1.display_result()
s2.display_result()

# output:
# name : anu
# average : 90.67
# name : adiba
# average : 90.67

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# bank account:
# Create a BankAccount class with:

        # account_holder
        # balance
        # deposit(amount)
        # withdraw(amount)
        # display_balance()

# Rules:

        # Reject deposits that are zero or negative
        # Reject withdrawals that are zero or negative
        # Reject withdrawals greater than the available balance
        # Do not allow a negative starting balance
        # Try to keep the balance unchanged when a transaction fails

class bankaccount:
    def __init__(self,account_holder,balance):
        self.account_holder=account_holder
        if balance<0:
            print("starting balance cannot be zero")
            self.balance=0
        else:
            self.balance=balance
    def deposit(self,amount):
        if amount<=0:
            print("deposit amount must be greater than zero")
        else:
            self.balance+=amount

    def withdraw(self,amount):
        if amount<=0:
            print("withdraw amount must be greater than zero")
        elif amount>self.balance:
            print("withdraw amount must be less than balance")
        else:
            self.balance-=amount
    def display_balance(self):
        print("account holder:",self.account_holder)
        print("current balance:",self.balance)
a1=bankaccount("dolly",500000)
a1.display_balance()
print("---------------------")
a1.deposit(50000)
a1.display_balance()
print("---------------------")
a1.deposit(-979)
a1.display_balance()
print("---------------------")
a1.withdraw(70000)
a1.display_balance()
print("---------------------")
a1.withdraw(600000)
a1.display_balance()
print("---------------------")
a1.withdraw(-93)
a1.display_balance()

# output:
# account holder: dolly
# current balance: 500000
# ---------------------
# account holder: dolly
# current balance: 550000
# ---------------------
# deposit amount must be greater than zero
# account holder: dolly
# current balance: 550000
# ---------------------
# account holder: dolly
# current balance: 480000
# ---------------------
# withdraw amount must be less than balance
# account holder: dolly
# current balance: 480000
# ---------------------
# withdraw amount must be greater than zero
# account holder: dolly
# current balance: 480000





# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# library book
# Create a Book class with:

    # title
    # author
    # is_available

# Methods:

    # borrow_book()
    # return_book()
    # display_info()

# Rules:

    # A book can only be borrowed when available
    # Returning an already available book should not mark it as newly returned twice
    # Display a clear message for each operation
class book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
        self.is_available=True
    def borrow_book(self):
        if self.is_available:
            self.is_available=False
            print("book borrowed successfully")
        else:
            print("sorry this book is already borrowed")
    def return_book(self):
        if not self.is_available:
            self.is_available=True
            print("book return successfully")
        else:
            print("this book is already available")
    def display_info(self):
        print("title:",self.title)
        print("author:",self.author)
        if self.is_available:
            print("status : Available")
        else:
            print("status : borrowed")

b1=book("python practice","dolly behera")
b1.display_info()
print("---------------------")
b1.borrow_book()
b1.display_info()
print("---------------------")
b1.borrow_book()
b1.display_info()
print("---------------------")
b1.return_book()
b1.display_info()
print("---------------------")
b1.return_book()
b1.display_info()

# output:
# title: python practice
# author: dolly behera
# status : Available
# ---------------------
# book borrowed successfully
# title: python practice
# author: dolly behera
# status : borrowed
# ---------------------
# sorry this book is already borrowed
# title: python practice
# author: dolly behera
# status : borrowed
# ---------------------
# book return successfully
# title: python practice
# author: dolly behera
# status : Available
# ---------------------
# this book is already available
# title: python practice
# author: dolly behera
# status : Available


# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Design a Rectangle class.

# Requirements:

    # Store length and width.
    # Implement area() and perimeter().
    # Implement is_square().
    # Reject non-positive dimensions.
    # Implement __str__() to return a readable description.
    # Create at least three test cases.
    # Explain why area() is an instance method rather than a class method.
class rectangle:
    def __init__(self,length,width):
        if length>0 and width>0:                
            self.length=length
            self.width=width
       
        else:
              raise ValueError("length and width must be greater than zero")
         
    def area(self):
        return self.length*self.width
    def perimeter(self):
        return 2*(self.length+self.width)
    def is_square(self):
        return self.length==self.width and self.length>0 and self.width>0
    def __str__(self):
        return f"Rectangle(length={self.length}, width={self.width})"
    def display_info(self):
        print(self)
        print("area:",self.area())
        print("perimeter:",self.perimeter())
        if self.is_square():
            print("this is a square")
        else:
            print("this is not a square")
r1=rectangle(5,10)
r1.display_info()
print("---------------------")

r2=rectangle(7,7)
r2.display_info()
print("---------------------")
try:
    r3=rectangle(0,10)
    r3.display_info()
except ValueError as e:
    print("Error:",e)

# output:
# Rectangle(length=5, width=10)
# area: 50
# perimeter: 30
# this is not a square
# ---------------------
# Rectangle(length=7, width=7)
# area: 49
# perimeter: 28
# this is a square
# ---------------------
# Error: length and width must be greater than zero


# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Mini-project — Student Result Manager

# Build a small program using classes and objects.

# Requirements
    # Create a Student class.
    # Store each student's name and marks.
    # Calculate the average.
    # Assign a grade.
    # Display a result report.
    # Create at least three student objects.
    # Handle an empty marks list.


class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def average(self):
        if not self.marks:
            return 0
        return sum(self.marks)/len(self.marks)
    def grade(self):
        avg=self.average()
        if avg>=90:
            return "A"
        elif avg>=80 and avg<90:
            return "B"
        elif avg>=70 and avg<80:
            return "C"
        elif avg>=60 and avg<70:
            return "D"
        elif avg>=50 and avg<60:
            return "E"
        else:
            return "fail"
    def __str__(self):
        return f"Name : {self.name} \nmark : {self.marks}"
    def display_result(self):
        print(self)
        print("average:",round(self.average(),2))
        print("grade:",self.grade())

s1=student("anu",[98,89,83])
s2=student("adiba",[93,90,86])
s3=student("dolly",[])
s1.display_result()
print("--------------------------------")
s2.display_result()
print("--------------------------------")
s3.display_result()

# output:
# Name : anu 
# mark : [98, 89, 83]
# average: 90.0
# grade: A
# --------------------------------
# Name : adiba 
# mark : [93, 90, 86]
# average: 89.67
# grade: B
# --------------------------------
# Name : dolly 
# mark : []
# average: 0
# grade: fail
