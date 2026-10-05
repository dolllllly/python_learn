# python programming practice----
# Day 16
# ------------------------------------------------------------------------------------------------------------------------------------------

# Advanced OOP: Composition, Aggregation, Association, __str__, __repr__ & Dunder Methods

# # topic learned:
        # Association
        # Aggregation
        # Composition
        # IS-A vs HAS-A
        # Dunder methods
        # __init__
        # __str__
        # __repr__
        # __len__
        # __eq__
        # __add__
        # Comparison dunder methods
        # Operator overloading
        # OOP design relationships 

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Association
# asscociation means thatt two classes are related or interact with eachother ,but neither necessarily owns the other.

class teacher:
    def teach(self):
       print("teacher is teaching")
class student:
    def learn(self):
        print("student is learning")
teacher1=teacher()
student1=student()

teacher1.teach()
student1.learn()

# output:
# teacher is teaching
# student is learning

# They are separate objects.
# A teacher can exist without a particular student, and a student can exist without a particular teacher.
# Teacher ←→ Student
# They have a relationship, but neither one necessarily controls the lifetime of the other.

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Composition:
# Composition Represents a stronger  has-a relationship in which one object is made up of another object as one of its components.

class Engine:
    def start(self):
        print("engine startes")
class Car:
    def __init__(self):
        self.engine=Engine()
    def start_car(self):
        self.engine.start()
        print("car started")
car=Car()
car.start_car()

# output:
# engine startes
# car started

# here self.engine=Engine() means the car contains Engine.
# Car creaates the Engine object in its constructor.
# Engine object stored in self.engine


# why is this called "has-a"?

#  in inheritance its a  Is-A relationship : Dog Is-A Animal
# in composition its a HAS-A relationship:  Car HAS-A Engine
# so:
    #   inheritance---IS-A
    #   composition---HAS-A

class Battery:
    def charge(self):
        print("batery charging")
class Phone:
    def __init__(self):
        self.battery=Battery()
    def charge_phone(self):
        print("phone conected")
        self.battery.charge()
samsung=Phone()
samsung.charge_phone()

# output:
# phone conected
# batery charging


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Aggregation:
# aggregation is also a has-a relationship, but weaker than composition.
# here one object contains a reference to an object of another class, while the contained object can also exist independently.

# example:
# a collage can have student. a student object can exist even when the department object is not present.

class Student:
    def __init__(self,name):
        self.name=name
class Collage:
    def __init__(self,student):
        self.student=student
student=Student("dolly")
c=Collage(student)
print(c.student.name)


# output:
# dolly


# the student can still exixt independently:
print(student.name)

# output:
# dolly

# So the College uses the Student, but doesn't necessarily own its existenc

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Composition vs Aggregation

#  | Composition                                  | Aggregation                    |
# | -------------------------------------------- | ------------------------------ |
# | Strong relationship                          | Weaker relationship            |
# | Object is usually created/owned by container | Object can exist independently |
# | Strong "has-a"                               | Loose "has-a"                  |
# | Example: Car → Engine                        | Example: College → Student     |



# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# What are Dunder Methods?
# Dunder means Double UNDERscore because they start and end with double underscores.
# dunder methods are special methods with double underscores __ that enable operator overloading and custom object behavior.
# example:
# __init__

# The below code displays the magic methods inherited by int class
print(dir(int))

['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__',
 '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__index__',
 '__init__','__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', 
'__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', 
'__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__',
'__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes',
 'imag', 'is_integer', 'numerator', 'real', 'to_bytes']



# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#__init__
# this method is automatically called when a new object of a class is created.

class student:
    def __init__(self,name):
        self.name=name
s=student("dolly")

# conceptually:
# Create object
#      ↓
# __init__()
#      ↓
# Initialize object


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# __str__
# __str__ defines the human-readable string representation of an object

# suppose:
class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
s=student("dolly",20)
print(s)

# output:
# <__main__.student object at 0x00000269FF359FA0>

# print(s) return a location which is not vey useful:

# so we define __str__

class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"student: {self.name}, age: {self.age}"
s=student("dolly",20)
print(s)

# output:
# student: dolly, age: 20

# print(object)
#        ↓
#    __str__()


# __str__ Must Return a String

# this is wrong:
def __str__(self):
    return self.age
# because self.age is an integer and it should return string.

# so:
def __str__(self):
    return str(self.age)
# or:
def __str__(self):
    return f"age: {self.age}"


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# __repr__
# __repr__ is another representation method.
# it is intended to provide a more developer-oriented / unambiguous representation of an object.

class student:
    def __init__(self,name,mark):
        self.name=name
        self.mark=mark
    def __repr__(self):
        return f'student({self.name!r}, {self.mark!r})'
s=student("dolly",90)
print(repr(s))

# output:
# student('dolly', 90)


# Why !r?
# return f"Student({self.name!r})"
# !r asks Python to use repr() formatting

name = "Dolly"
print(f"{name}")
print(f"{name!r}")

# output:
# Dolly
# 'Dolly'

# This makes strings visibly distinguishable in representation


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# str() vs repr()

class Student:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Student name: {self.name}"

    def __repr__(self):
        return f"Student({self.name!r})"
    
s = Student("Dolly")
print(str(s))
print(repr(s))

# output:
# Student name: Dolly
# Student('Dolly')

# __str__  -> user-friendly
# __repr__  -> developer/debug=frienfly

# what happen with print(object)?

print(s)

# output:
# Student name: Dolly

# python generally uses the object's string representation.
# is __str__ is defines, it is used.
# if it isn't defined, python can fall back to __repr__


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# __len__
#this method tells python what len(object) should return.

class team:
    def __init__(self,members):
        self.members=members
    def __len__(self):
        return len(self.members)
team1=team(["dolly","anu","adiba"])
print(len(team1))

# output:
# 3

# or you can call it :
print(team1.__len__())


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# __eq__
# __eq__ controls equality using: ==

class student:
    def __init__(self,name):
        self.name=name
    def __eq__(self,other):
        return self.name==other.name
s1=student("dolly")
s2=student("dolly")
print(s1==s2)

# output:
# True

# Without defining appropriate equality behavior, two separate objects are generally not considered equal merely because their attributes contain the same values


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# __add__
# __add__ method defines how objects of a class are added together using the '+' operator

class number:
    def __init__(self,value):
        self.value=value
    def __add__(self,other):
        return self.value + other.value
a=number(10)
b=number(20)
print(a+b)
print(a.__add__(b))
# output:
# 30
# 30

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Operator overloading
# Operator overloading means giving a normal Python operator like +, -, ==, < a special meaning for your own objects

# Common operator overloading methods
# | Operator | Dunder method    |
# | -------- | ---------------- |
# | `+`      | `__add__()`      |
# | `-`      | `__sub__()`      |
# | `*`      | `__mul__()`      |
# | `/`      | `__truediv__()`  |
# | `//`     | `__floordiv__()` |
# | `%`      | `__mod__()`      |
# | `==`     | `__eq__()`       |
# | `!=`     | `__ne__()`       |
# | `<`      | `__lt__()`       |
# | `>`      | `__gt__()`       |
# | `<=`     | `__le__()`       |
# | `>=`     | `__ge__()`       |


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# custom product:

class product:
    def __init__(self,name,price):
        self.name=name
        self.price=price

    def __str__(self):
        return f'{self.name} : ₹ {self.price}'
    def __add__(self,other):
        return f'₹ {self.price + other.price}'
p1=product("keyboard",1000)
p2=product("mouse",500)
print(p1)
print(p2)
print("total:",p1+p2)

# output:
# keyboard : ₹ 1000
# mouse : ₹ 500
# total: ₹ 1500

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# __lt__ and __gt__
# We can customize comparisons

class Student:

    def __init__(self, marks):
        self.marks = marks

    def __gt__(self, other):
        return self.marks > other.marks
s1 = Student(90)
s2 = Student(80)

print(s1 > s2)

# Output:
# True

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Mini Project

# Shopping Cart

# Build:
    # Product
    #     ↓
    # ShoppingCart

# Product should have:
    # name
    # price

# ShoppingCart should:
    # contain products
    # add products
    # calculate total
    # show products
    # use __len__
    # use __str__


class Product:

    def __init__(self,name,price):
        self.name=name
        self.price=price

    def __str__(self):
        return f'{self.name}: ₹ {self.price}'
    
class ShoppingCart:

    def __init__(self):
        self.products=[]

    def add_products(self,product):
        self.products.append(product)

    def total(self):
        return sum(product.price for product in self.products)

    def __len__(self):
        return len(self.products)

    def __str__(self):
        return "\n".join(str(product) for product in self.products)
p1=Product("keyboard",1000)
p2=Product("mouse",500)

cart=ShoppingCart()

cart.add_products(p1)
cart.add_products(p2)

print(cart)

print("total:",cart.total())
print("itens:", len(cart))




# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------




# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



