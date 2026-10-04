# python programming practice----
# Day 14
# ------------------------------------------------------------------------------------------------------------------------------------------
# Encapsulation, Abstraction, Properties & Access Control

# #topic learned:
    # Encapsulation
    # Public members
    # Protected _variable
    # Private __variable
    # Name mangling
    # Getter
    # Setter
    # @property
    # Property setter
    # Read-only property
    # Abstraction
    # Abstract class
    # ABC
    # @abstractmethod
    # Encapsulation vs abstraction
    # Combining OOP concepts

# ------------------------------------------------------------------------------------------------------------------------------------------------------

# What is Encapsulation?
# Encapsulation is about protecting data inside a class.
# bundling data (properties) and methods together in a class, while controlling how the data can be accessed from outside the class.
# This prevents accidental changes to your data and hides the internal details of how your class works.

# ------------------------------------------------------------------------------------------------------------------------------------------------------

# why do we need encapsulation?

# supose:
class bank:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance

customer1=bank("dolly",50000)
customer1.balance=-200000
print(customer1.balance)

# output:
# -200000

# you see -200000 is undesirable in bank. so we need to control balance
# for example:
# balance must be greater than 0
# this is where encapsulation become useful.

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------


# access modifiers in python
# python commonly uses three levels of access:

# | Type      | Syntax   | Meaning                                         |
# | --------- | -------- | ----------------------------------------------- |
# | Public    | `name`   | Can be accessed normally                        |
# | Protected | `_name`  | Intended for class/subclass use                 |
# | Private   | `__name` | Name-mangled; intended to prevent direct access |

# python does not enforce access modifiers as strictly as java/c++
# the _ and __ conventions communicate intendded access.


# ------------------------------------------------------------------------------------------------------------------------------------------------------

# public member:
# Public members are variables or methods that can be accessed from anywhere inside the class, outside the class or from other modules
# By default, all members in Python are public

class student:
    def __init__(self,name):
        self.name=name
s=student("dolly")
print(s.name)

# output:
# dolly

# we can also change it:

s.name="devi"
print(s.name)

# output:
# devi

# ------------------------------------------------------------------------------------------------------------------------------------------------------

# protect memberss:
# Protected members are variables or methods that are intended to be accessed only within the class and its subclasses
# They are not strictly private but should be treated as internal.
# a single underscore prefix indicate a protectes-by-convention attribute or methods

class student:
    def __init__(self,name):
        self._name=name
    def show(self):
        print(self._name)

s=student("dolly")
print(s._name)

# output:
# dolly

# we can technically access it ,so why call it protected?
# this is intended for internal use or subclasses. Don't access it directly unless you know what you're doing


# ------------------------------------------------------------------------------------------------------------------------------------------------------

# private members:
# Private members are variables or methods that cannot be accessed directly from outside the class
#  They are used to restrict access and protect internal data
# two underscores as prefix are used:

class employee:
    def __init__(self,salary):
        self.__salary=salary
e=employee(50000)
print(e.__salary)

# output:
# AttributeError: 'employee' object has no attribute '__salary'

# error because __salary is name-mangled

class employee:
    def __init__(self,salary):
        self.__salary=salary
    def show_salary(self):
        print(self.__salary)
e=employee(50000)
# print(e.__salary)     # error
e.show_salary()

# output:
# 50000


# user coulsn't directly manipulate the salary:
class employee:
    def __init__(self,salary):
        self.__salary=salary
    def show_salary(self):
        print(self.__salary)
e=employee(50000)
e.__salary=78999
e.show_salary()

# output:
# 50000

# salary is still same as before
# insted we provide controlled methods:

class employee:
    def __init__(self,salary):
        self.__salary=salary
    def update_salary(self,NewSalary):
        if NewSalary>0:
            self.__salary=NewSalary

    def show_salary(self):
        print(self.__salary)
e=employee(50000)
e.update_salary(70000)
e.show_salary()

# output:
# 70000

# ------------------------------------------------------------------------------------------------------------------------------------------------------

# name mangling:
# Python uses name mangling, where the interpreter internally renames the variable 
#  __salary becomes _employee__salary
# This discourages direct access from outside the class . so private variables aren't truly inaccessible.

class employee:
    def __init__(self,salary):
        self.__salary=salary
e=employee(50000)
print(e._employee__salary)

# output:
# 50000

# ------------------------------------------------------------------------------------------------------------------------------------------------------

# Getter and Setter
# Getter:
# Used to read a private value.

# Setter:
# Used to modify a private value safely.

# Instead of accessing private data directly, these methods provide controlled access, allowing you to:
    # Read data using a getter method.
    # Update data using a setter method with optional validation or restrictions.

class employee:
    def __init__(self,salary):
        self.__salary=salary
    def get_salary(self):
        return self.__salary
    def set_salary(self, salary):
        if salary>0:
            self.__salary=salary
        else:
            print("invalid salary")
e=employee(80000)
print(e.get_salary())
e.set_salary(100000)
print(e.get_salary())

# output:
# 80000
# 100000

# Why Getter/Setter?

# Without encapsulation:
e.salary = -5000  

# With controlled access:
e.set_salary(-5000)

# The setter can validate the value.

# So:

    # Data
    #  ↓
    # Private attribute
    #  ↓
    # Getter / Setter
    #  ↓
    # Controlled access
# ------------------------------------------------------------------------------------------------------------------------------------------------------

# Python @property
# python provide a cleaner way to implement gretters ans setters

# instead of:
e.set_salary()

# we can write:
e.salary
# using @property

class employee:
    def __init__(self,salary):
        self.__salary=salary
    @property
    def salary(self):
        return self.__salary
    
e=employee(80000)
print(e.salary)

# output:
# 80000

# notice: e.salary not e.salary()



# ------------------------------------------------------------------------------------------------------------------------------------------------------

# property setter

# we can use:
# @salary.setter

class employee:
    def __init__(self,salary):
        self.__salary=salary
    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self,value):
        if value>0:
            self.__salary=value
        else:
            print("invalid salary")
e=employee(80000)
print(e.salary)
e.salary=100000
print(e.salary)

# output:
# 80000
# 100000

e.salary=-100

# output:
# invalid salary


# Execution Flow:
# e.salary = 100000
#      ↓
# salary setter
#      ↓
# validation
#      ↓
# self.__salary = 100000


# ---------------------------------------------------------------------------------------------------------------------------------------------
# Important: @property vs Normal Method:

# Normal getter
def get_salary(self):
    return self.__salary

# Call:
e.get_salary()

# --------------

# Property
@property
def salary(self):
    return self.__salary

# Call:
e.salary

# The property makes an attribute look like a normal attribute while executing method logic behind the scenes.

# ------------------------------------------------------------------------------------------------------------------------------------------------------

# Read-Only Property

# A property without a setter can be effectively read-only through the normal interface.

class Student:
    def __init__(self, marks):
        self.__marks = marks

    @property
    def marks(self):
        return self.__marks
s = Student(90)
print(s.marks) 

# output:
# 90

s.marks = 100
# raise an AttributeError because there is no setter

# ------------------------------------------------------------------------------------------------------------------------------------------------------

# Abstraction:
# Abstraction is the process of hiding implementation details and exposing only the essential functionality to the user

# real-world example:
# when you use a ATM
# Insert card
#      ↓
#Enter PIN
#      ↓
#Choose withdrawal
#      ↓
#Enter amount
#      ↓
#Receive money

# you don't need to know exactly how the bank's internal transaction system works.
# that's abstraction

# ------------------------------------------------------------------------------------------------------------------------------------------------------

# Abstraction in python
# python provides the abc module

from abc import ABC, abstractmethod

# we can create an abstract class:

from abc import ABC, abstractmethod

class animal(ABC):
    @abstractmethod
    def sound(self):
        pass
a=animal()

# raise TypeError: Can't instantiate abstract class animal without an implementation for abstract method 'sound'


# ------------------------------------------------------------------------------------------------------------------------------------------------------

# Implementing the Abstract Method

from abc import ABC, abstractmethod
class animal(ABC):
    @abstractmethod
    def sound(self):
        pass
class dog(animal):
    def sound(self):
        print("dog bark")

d=dog()
d.sound()

# output:
# dog bark

# the subclass provides the actual implementation.


# ------------------------------------------------------------------------------------------------------------------------------------------------------

# why Abstraction?
# Imagine you have:

# Animal
#  ├── Dog
#  ├── Cat
#  └── Cow

# You want to guarantee:
    # Dog → must have sound()
    # Cat → must have sound()
    # Cow → must have sound()

# But each one can implement it differently:

# Dog.sound() → "Bark"
# Cat.sound() → "Meow"
# Cow.sound() → "Moo"

# That's the real purpose of abstraction:
# The parent defines what the child MUST provide; the child decides HOW to implement it.

# ------------------------------------------------------------------------------------------------------------------------------------------------------

# Abstraction vs Encapsulation

# | Encapsulation                                           | Abstraction                                    |
# | ------------------------------------------------------- | ---------------------------------------------- |
# | Controls access to data                                 | Hides implementation details                   |
# | Focuses on data protection/control                      | Focuses on what an object does                 |
# | Uses private/protected conventions, properties, methods | Uses abstract classes/methods                  |
# | Example: validating salary                              | Example: every animal must implement `sound()` |



# Encapsulation = HOW data is accessed

# Abstraction = WHAT functionality is exposed


# ------------------------------------------------------------------------------------------------------------------------------------------------------

# Complete Example: Encapsulation + Abstraction

from abc import ABC , abstractmethod

class bankaccount(ABC):
    def __init__(self,balance):
        self.__balance=balance
    @abstractmethod
    def account_type(self):
        pass
    @property
    def balance(self):
        return self.__balance
    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount

class savingaccount(bankaccount):
    def account_type(self):
        print("saving account")

account=savingaccount(100000)
account.account_type()
print(account.balance)
account.deposit(100000)
print(account.balance)

# output:
# saving account
# 100000
# 200000

Here:

# Abstraction
@abstractmethod
def account_type(self):

# Encapsulation
self.__balance

# Property
@property
def balance(self):

# Inheritance
savingsaccount(bankaccount)

# This is how OOP concepts start working together.


# ------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                # practice
# --------------------------------------------------------------------------------------------------------------------------------

# Create a BankAccount class with:

        # private __balance
        # deposit()
        # withdraw()
        # show_balance()
# Don't allow withdrawal if the amount is greater than the balance.


class BankAccount:
    def __init__(self,balance):
        self.__balance=balance

    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
        else:
            print("deposite amount must be grater than zero")

    def withdraw(self,amount):
        if amount<self.__balance:
            self.__balance-=amount
        else:
            print("withdraw amount exceed balance")

    def show_balance(self):
        return f'Balance: {self.__balance}'

account=BankAccount(100000)
print(account.show_balance())
account.deposit(100000)
print("after deposit",account.show_balance())
account.withdraw(50000)
print("after withdraw",account.show_balance())

# output:
# Balance: 100000
# after deposit Balance: 200000
# after withdraw Balance: 150000

# ------------------------------------------------------------------------------------------------------------------------------------------------------

# Create:
    # class Student
    # with a private:__marks

# Use @property to:
    # get marks
    # set marks
    # allow only 0–100

class student:
    def __init__(self,name,marks):
        self.name=name
        self.__marks=marks
    @property
    def marks(self):
        return self.__marks
    @marks.setter
    def marks(self,marks):
        if marks>=0 and marks<=100:
            self.__marks=marks
        else:
            print("marks only allow 0-100")
s1=student("dolly",80)
print(s1.name, s1.marks)
s1.marks=95
print("after marks modifications:",s1.name, s1.marks)
s1.marks=-97

# output:
# dolly 80
# after marks modifications: dolly 95
# marks only allow 0-100
        

# ------------------------------------------------------------------------------------------------------------------------------------------------------

# Create an abstract class:
    # Shape
    # with: area() as an abstract method.

# Create:
    # Circle
    # Rectangle
# and implement area() in both

from abc import ABC , abstractmethod
import math as m

class shape(ABC):
    @abstractmethod
    def area(self):
        pass
class circle(shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return f'area of circle with radius {self.radius} is {round(m.pi*self.radius**2,2)}'

class rectangle(shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return f'area of rectangle with length {self.length} and width {self.width} is {self.length*self.width}'

c=circle(4)
r=rectangle(3,6)
print(c.area())
print(r.area())

# output:
# area of circle with radius 4 is 50.27
# area of rectangle with length 3 and width 6 is 18 
        

# ------------------------------------------------------------------------------------------------------------------------------------------------------

# Create:
    # class Employee
    # with:
        # name
        # private salary

# Requirements:
    # salary > 0
    # salary property
    # salary setter
    # show_details()

# Then create:
    # Manager(Employee)
    # Developer(Employee)

# and demonstrate inheritance + encapsulation + polymorphism.

class employee:
    def __init__(self,name,salary):
        self.name=name
        self.__salary=salary
    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self,salary):
        if salary>0:
            self.__salary=salary
        else:
            print("invalid salary")
    def show_details(self):
        print("name:",self.name)
        print("salary:",self.salary)

class manager(employee):
    def show_details(self):
        print("manager:",self.name)
        print("salary:",self.salary)
    
class developer(employee):
    def show_details(self):
        print("developer:",self.name)
        print("salary:",self.salary)

employee1=manager("devi",200000)
employee1.show_details()
employee2=developer("dolly",200000)
employee2.show_details()

# output:
# manager: devi
# salary: 200000
# developer: dolly
# salary: 200000


# ------------------------------------------------------------------------------------------------------------------------------------------------------

# mini project: Employee Salary Management System:

from abc import ABC, abstractmethod

class employee(ABC):
    def __init__(self,name,salary):
        self.name=name
        self.__salary=salary
    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self,salary):
        if salary>0:
            self.__salary=salary
        else:
            print("invalid salary")
    @abstractmethod
    def work(self):
        pass
    def show_details(self):
        print("name:",self.name)
        print("salary:",self.salary)

class manager(employee):
    def work(self):
        print("manager manage the team")
    def show_details(self):
        print("manager:",self.name)
        print("salary:",self.salary)

class developer(employee):
    def work(self):
        print("developer write code")
    def show_details(self):
        print("developer:",self.name)
        print("salary:",self.salary)

d=developer("dolly",100000)
m=manager("devi",120000)
d.show_details()
d.work()
d.salary=200000
print("salary modified")
d.show_details()
print()
m.show_details()
m.work()
m.salary=220000
print("salary modified")
m.show_details()

# output:
# developer: dolly
# salary: 100000
# developer write code

# salary modified:
# developer: dolly
# salary: 200000

# manager: devi
# salary: 120000
# manager manage the team

# salary modified:
# manager: devi
# salary: 220000

# ------------------------------------------------------------------------------------------------------------------------------------------------------