# python programming practice----
# Day 15
# ------------------------------------------------------------------------------------------------------------------------------------------
# Class Variables, Instance Variables, Class Methods, Static Methods & Method Types

# # topic learned
    #  Instance variables
    #  Class variables
    #  Attribute lookup
    #  __dict__
    #  Instance methods
    #  self
    #  Class methods
    #  cls
    #  @classmethod
    #  Alternative constructors
    #  Static methods
    #  @staticmethod
    #  Instance vs class vs static methods

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Instance Variables:
# An instance variable belongs to a particular object.
# Usually created inside __init__() using self

class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
# create two objets:
s1=student("dolly",90)
s2=student("devi",80)

# now each object has its own name and marks:
# s1.name-> dolly
# s1.marks->90

# s2.name->devi
# s2.marks->80

# so : instance variable= separate copy of each object.

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# class variables
# a class variable belongs to class itself and is shared by objects

class student:
    school="pes university"
    def __init__(self,name):
        self.name=name
s1=student("dolly")
s2=student("devi")
print(s1.school)
print(s2.school)
print(student.school)

# output:
# pes university
# pes university
# pes university


# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# instance vs class variable

class student:
    school="pes university"  #class variable
    def __init__(self,name):
        self.name=name        #instance variable

s1=student("dolly")
s2=student("devi")
print(s1.name)
print(s2.name)
print(s1.school)
print(s2.school)

# otput:
# dolly
# devi
# pes university
# pes university

# name is different for each employee.
# school is shared 


# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Changing a Class Variable

class student:
    school="kalinga university"
s1=student()
s2=student()

student.school="pes university"
print(s1.school)
print(s2.school)

# output:
# pes university
# pes university

# we can change the class variable through the class
student.school="pes university"
# therefore both objects see the new value.


# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Important: Changing Through an Object

class student:
    school="kalinga university"
s1=student()
s2=student()

s1.school="pes university"
print(s1.school)
print(s2.school)
print(student.school)

# output:
# pes university
# kalinga university
# kalinga university

# when we try to change the class attribute with object..
# instead of updating the class attribute for all it create an instance attribute called school for s1.

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Attribute Lookup
# it mean when you call a variable using object , it first check whether there is any instance variable of that name ,if yes than return the value
# if no then chech if the class have that variable.

# example:
s1.school

# 1. Does s1 have school?
#         ↓
#       YES → use it

#       NO
#         ↓
# 2. Does Student have school?
#         ↓
#       YES → use it


# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# __dict__
# __dict__ is a special attribute that shows the attributes/data stored inside an object or class as a dictionary


class student:
    school="pes university"
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

s=student("dolly",90)
print(s.__dict__)

# output:
# {'name': 'dolly', 'marks': 90}

# notice that school isn't there.
# because school belongs to the class.

print(student.__dict__)
# output:
# {'__module__': '__main__', 'school': 'pes university', '__init__': <function student.__init__ at 0x00000299236AD260>,
#  '__dict__': <attribute '__dict__' of 'student' objects>, '__weakref__': <attribute '__weakref__' of 'student' objects>, '__doc__': None}


# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Method Types in Python
# inside calss you'll commonly encounter:

# 1 instance method
    # def show(self):

# 2. class method

    # @classmethod
    # def show(cls):

# 3. static method

    # @staticmethod
    # def show():


# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# instance method:
# this is the method you've already been using most ofthe.

class student:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(self.name)
s=student("dolly")
s.show()

# output:
# dolly

# the first parameter is:
# self
# self refers to current object


# why self?
# suppose:
s1=student("dolly")
s2=student("devi")
s1.show()
s2.show()

# when you call:
s1.show()
# python effectively passes s1.
# conceptually: student.show(s1)

# and when you call:
s2.show()
# conceptually : student.show(s2)

# therefore self.name means:  "name belonging to the current object"

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# class object:
# a class method work with class itself
# it uses:
@classmethod
# and coventionally receives: cls

class student:
    school="kalinga university"
    @classmethod
    def change_school(cls,new_school):
        cls.school=new_school

print("before change:",student.school)
student.change_school("pes university")
print("after change:",student.school)

# output"
# before change: kalinga university
# after change: pes university

# here cls refers to (student) current class


# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# self vs cls
# | Parameter | Refers to      |
# | --------- | -------------- |
# | `self`    | Current object |
# | `cls`     | Current class  |


# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Class Method Can Be Called Through Object

class student:
    school="kalinga"
    @classmethod
    def show_school(cls):
        print(cls.school)
s=student()
s.show_school()

# output:
# kalinga


class student:
    school="kalinga university"
    @classmethod
    def change_school(cls,new_school):
        cls.school=new_school
s=student()
print("before change:",s.school)
s.change_school("pes university")
print("after change:",s.school)

# ouput:
# before change: kalinga university
# after change: pes university

# it still receives the class as cls

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Class Method as Alternative Constructor

class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls,data):
        name,age=data.split(",")
        return cls(name,int(age))

s=student.from_string("dolly,20")
print(s.name)
print(s.age)

# output:
# dolly
# 20

# this class method act as an alternative constructer


# Why cls(...) Instead of Student(...)?
# we write:  return cls(name,int(age))
# instead of : return student(name,int(age))
# because cls allows the method to work properly with subclasses too, this become useful in inheritance.

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# static method
# a static method doesn't automatically receive self or cls

class calculator:
    @staticmethod
    def add(a,b):
        return a+b
print(calculator.add(10,20))

# output:
# 30

# no object is required


# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# why use static methods?

# suppose a function is logically related to a class but doesn't need any object or class data.
class calculator:
    @staticmethod
    def is_even(number):
        return number%2==0
print(calculator.is_even(10))

# output:
# True
# the method doesn't need: self or cls
# therefore static method is suitable.


# Calling Static Method Through Object
c=calculator()
print(c.is_even(7))

# output:
# False

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Calling Static Method Through Object

# | Method   | Decorator       | First parameter | Mainly works with |
# | -------- | --------------- | --------------- | ----------------- |
# | Instance | None            | `self`          | Object            |
# | Class    | `@classmethod`  | `cls`           | Class             |
# | Static   | `@staticmethod` | None            | Independent logic |


# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

                                                    #practice
# ---------------------------------------------------------------------------------------------------------------------------------------------------


# Create a class variable:
#     employee_count = 0
#     Every time an employee is created, increase it.

# Expected:
#     Total Employees: 3

class employee:
    employee_count=0
    def __init__(self,name):
        self.name=name
        employee.employee_count+=1
e1=employee("dolly")
e2=employee("anu")
e3=employee("adiba")
print("total employee:",employee.employee_count)

# output:
# total employee: 3


# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Create a class method:
    # get_employee_count()
    # that returns the number of employees

class employee:
    employee_count=0
    def __init__(self,name):
            self.name=name
            employee.employee_count+=1
    @classmethod
    def get_employee_count(cls):
        return employee.employee_count
e1=employee("dolly")
e2=employee("anu")
e3=employee("adiba")
print("total employee:",employee.get_employee_count())


# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Create a static method:

    # is_valid_name(name)
    # Return True if the name isn't empty.

class employee:
    @staticmethod
    def is_valid_name(name):
        return len(name.strip())>0
print(employee.is_valid_name("dolly"))
print(employee.is_valid_name("    "))
print(employee.is_valid_name(" "))

# output:
# True
# False
# False

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Create an alternative constructor:
    # Employee.from_string("Dolly,100000")

# It should create:
    # Employee("Dolly", 50000)

class employee:

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    @classmethod
    def from_string(cls,string):
        name,salary= string.split(",")
        return cls(name,int(salary))
e=employee.from_string("Dolly,100000")
print(e.name)
print(e.salary)

# output:
# Dolly
# 100000


# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Mini Project
# Employee Management System

class employee:

    company="microsoft"
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def show_details(self):
        print("name:",self.name)
        print("salary:",self.salary)
        print("company:",self.company)
    @classmethod
    def change_company(cls,new_company):
        cls.company=new_company
    @staticmethod
    def is_valid_salary(salary):
        return salary>0

e1=employee("dolly",100000)
e1.show_details()
employee.change_company("google")
print("after company change:",employee.company)
print(employee.is_valid_salary(200000))


# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------




# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------




# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------