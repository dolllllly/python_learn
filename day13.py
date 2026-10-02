# python programming practice----
# Day 13
# ------------------------------------------------------------------------------
# Inheritance and Polymorphism

## Topics
    # - Inheritance
    # - Single and multiple inheritance
    # - Method overriding
    # - super()
    # - Method Resolution Order (MRO)
    # - Polymorphism
    # - Duck typing
    # - isinstance() and issubclass()

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# What is inheritance?
# Inheritance is a mechanism in which one class acquires the properties and methods of another class.
# The class that inherits is called the child class or derived class.
# The class from which the child class inherits is called the parent class or base class.

class person:
    def __init__(self,name):
        self.name=name
    def introduce(self):
        print("my name is",self.name)

class student(person):
    def study(self):
        print(self.name,"is studying python ")
s1=student("dolly")
s1.introduce()
s1.study()

# output:
# my name is dolly
# dolly is studying python

# class student(person): this means that the student class inherits from person
# the student object can use intoduce(),even though that method is defined in person.


# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# type of inheritance
# 1. single inheritance:
# one child inherits from one parent class.

class person:
    def breathe(self):
        print("breaathing")

class student(person):
    def study(self):
        print("studying")
obj=student()
obj.breathe()
obj.study()

# output:
# breaathing
# studying


# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# # 2.multilevel inheritance
# a class inherits from a child class, forming a chain.
# person -> employee -> manager

class person:
    def introduce(self):
        print("i am a person")
class employee(person):
    def work(self):
        print("working")
class manager(employee):
    def manage(self):
        print("manage a team")
obj=manager()
obj.introduce()
obj.work()
obj.manage()

# output:
# i am a person
# working
# manage a team

# manager inherits from employee, ehich inherits from person


# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 3.multiple inheritance:
# a child inherits from more than one parents
# camera      person
#    \          /    
#     smartphone

class camera:
    def take_photo(self):
        print("taking photo")
class phone:
    def making_call(self):
        print("making a call")
class smartphone(camera,phone):
    pass
obj=smartphone()
obj.take_photo()
obj.making_call()

# output:
# taking photo
# making a call


# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 4. hiierarchical inheritance:
# multiple child classes inherit from a single parent class
#   animal
#   /    \
# dog    cat

class animal:
    def eat(self):
        print("eating")
class dog(animal):
    def bark(self):
        print("barking")
class cat(animal):
    def meow(self):
        print("meowing")
d=dog()
c=cat()
d.eat()
d.bark()

c.eat()
c.meow()    

# output:
# eating
# barking
# eating
# meowing

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Method overriding
# Method overriding happens when a child class defines a method with the same name as a method inherited from its parent

class animal:
    def sound(self):
        print("animal makes a sound")
class dog(animal):
    def sound(self):
        print("dog barks")
a=animal()
d=dog()
a.sound()
d.sound()

# output:
# animal makes a sound
# dog barks

# the dog class overrides sound()

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# the super() function
# super() function is used to call a method from the parent class inside a child class.
# it allows to extend or override inherited methods while still reusing the functionality of the parent class.

# reusing the parent's constructor in the child class:

class person:
    def __init__(self,name):
        self.name=name
class student(person):
    def __init__(self,name,age):
        super().__init__(name)
        self.age=age
s1=student("dolly",20)
print(s1.name)
print(s1.age)

# output:
# dolly
# 20

# Without super().__init__(name), the child's constructor would not automatically call the parent's __init__()

# extending a method from the parent class:

class person:
    def introduce(self):
        print("i am a person")
class student(person):
    def introduce(self):
        super().introduce()
        print("i am a student")
s1=student()
s1.introduce()

# output:
# i am a person
# i am a student

# thee child extend the parents methods instead of completely overriding it.


# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Method Resolution Order (MRO)
# when a class inherits from multiple classes, pthon needs a defined order for looking up methods .
# this is called method resolution order(MRO)
#python use the C3 ilinearization algorithm to determine the MRO.

class A:
    def show(self):
        print("A")
class B(A):
    def show(self):
             print("B")
class C(A):
    def show(self):
        print("C")
class D(B,C):
    pass
d=D()
d.show()
print(D.mro())

# output:
# B
# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]

# we can inspect the MRO of a class using the mro() method or the __mro__ attribute.

# why does D.show() print "B" instead of "C"??
# Dinherits from B first and C second, Python searches according to the MRO and finds show() in B before reaching C



# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# polymorphism:
# Polymorphism means “many forms.” In Python, different objects can provide the same method name while performing different actions

class dog:
    def sound(self):
        print("bark")
class cat:
    def sound(self):
        print("meow")
class cow:
    def sound(self):
        print("moo")
animals=[dog(),cat(),cow()]
for animal in animals:
    animal.sound()

# output:
# bark
# meow
# moo


# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Duck typing:
# python often focuses on what an object can do rather than its exact class.

class PDF:
    def open(self):
        print("Opening PDF")

class Image:
    def open(self):
        print("Opening image")

def open_file(file):
    file.open()

open_file(PDF())
open_file(Image())

# Output:
# Opening PDF
# Opening image

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# isinstance() and issubclass()
# These built-in functions help inspect class relationships

# isinstance(object, classinfo): 
# Returns True if the object is an instance of the class or one of its subclasses, otherwise False.

class animal:
    pass
class dog(animal):
    pass
d=dog()
print(isinstance(d,dog))      # True
print(isinstance(d,animal))   # True
a=animal()
print(isinstance(a,dog))      # False

# output:
# True
# True
# False

# issubclass():
# returns True if the first class is a subclass of the second class, otherwise False.


class animal:
    pass
class dog(animal):
    pass
print(issubclass(dog,animal))   
print(issubclass(animal,dog))

# output:
# True
# False

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                      practice:
# ---------------------------------------------------------------------------------------------------------------------------------------------------

# Create a parent class Vehicle with:
    #  brand
    # start()

#  Create a child class Car with:
    # model
    # display_details()

# Requirements:
    # Use super() to initialize the brand.
    # Create two car objects.
    # Display their details.

class vehicle:
    def __init__(self,brand):
        self.brand=brand
    def start(self):
            print("vehicle started")
class car(vehicle):
    def __init__(self,brand,model):
        super().__init__(brand)
        self.model=model
    def display_details(self):
        super().start()
        print("brand:",self.brand)
        print("model:",self.model)
obj1=car("BMW","X5")
obj2=car("audi","A4")
obj1.display_details()
print("---------------------")
obj2.display_details() 

# output:
# vehicle started
# brand: BMW
# model: X5
# ---------------------
# vehicle started
# brand: audi
# model: A4

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Create a parent class Shape with an area() method.

# Create child classes:
    # Rectangle
    # Circle
    # Square

# Each class should override area() to calculate its own area.

# Use a loop to print the area of each object.

import math as m
class shape:
    def area(self):
        pass
class rectangle(shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return f"area of rectangle : {self.length*self.width}"
class circle(shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return f"area of circle : {round(m.pi*self.radius**2,2 )}"

class square(shape):
    def __init__(self,side):
        self.side=side
    def area(self):
        return f"area of square : {self.side**2}"

object=[rectangle(5,10),circle(5),square(4)]

for obj in object:
    print(obj.area())

# output:
# area of rectangle : 50
# area of circle : 78.54
# area of square : 16


# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Create these classes:

        # Writer with write()
        # Speaker with speak()
        # Presenter inheriting from both

# Create an object of Presenter and call both methods
# Then add a method named introduce() to both parent classes. 
# Define it in neither Presenter nor its parents' child level. 
# Predict which implementation is selected, then verify using Presenter.mro()

class writer:
    def write(self):
        print("write")
    def introduce(self):
        print("writer class")
class speaker:
    def speak(self):
        print("speak")
    def introduce(self):
            print("speaker class")
class preasenter(speaker,writer):
    pass

obj1=preasenter()
obj1.write()
obj1.speak()
obj1.introduce()
print(preasenter.mro())

# output:
# write
# speak
# speaker class
# [<class '__main__.preasenter'>, <class '__main__.speaker'>, <class '__main__.writer'>, <class 'object'>]



# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Build a notification system with:
    # A base class Notification.
    # Child classes EmailNotification, SMSNotification, and PushNotification.
    # A method send(message) in each class.
    # A function send_all(notifications, message) that sends the message through every object.

# Requirements:
    # Use method overriding.
    # Demonstrate polymorphism.
    # Do not use if/elif to check each notification's type inside send_all().
    # Add a new notification type without modifying send_all().
    # Write tests that verify the output or behavior.
    
        
class notification:
    def __init__(self,receiver):
        self.receiver=receiver
    
        
class EmailNotification(notification):
   
    def send(self,message):
        self.message=message
        print(f"sending email notification")
        print(f"to: {self.receiver}")
        print(self.message)
        print(f"email send successfully")

class SMSNotofication(notification):
   
    def send(self,message):
            self.message=message
            print(f"sending sms notification")
            print(f"to: {self.receiver}")
            print(self.message)
            print(f"sms send successfully")

class PushNotification(notification):
    
    def send(self,message):
                self.message=message
                print(f"sending push notification")
                print(f"to: {self.receiver}")
                print(self.message)
                print(f"push notification send successfully")

class WhatsAppNotification(notification):
     def send(self,message):
          self.message=message
          print(f"sending WhatsApp notification")
          print(f"to: {self.receiver}")
          print(self.message)
          print(f"WhatsApp notification send successfully")
                
def send_all(notifications,message):
    for notification in notifications:
          notification.send(message)
          print("---------------------------\n")

notification=[EmailNotification("dollybehera@example.com"),SMSNotofication(12399480809),PushNotification("dolly's phone"),WhatsAppNotification("97987989070")]
send_all(notification,"message: your order have been shipped")

# # output:
# sending email notification
# to: dollybehera@example.com
# message: your order have been shipped
# email send successfully
# ---------------------------

# sending sms notification
# to: 12399480809
# message: your order have been shipped
# sms send successfully
# ---------------------------

# sending push notification
# to: dolly's phone
# message: your order have been shipped
# push notification send successfully
# ---------------------------

# sending WhatsApp notification
# to: 97987989070
# message: your order have been shipped
# WhatsApp notification send successfully
# ---------------------------

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------