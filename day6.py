#  python programming practice----
# Day 6
# ---------------------------------------------------------------------------------------------------------------------

# - What are functions?
# - Creating functions
# - Calling functions
# - Parameters
# - Arguments
# - Multiple parameters
# - return
# - print() vs return
# - Returning multiple values
# - Default parameters
# - Positional arguments
# - Keyword arguments
# - Local variables
# - Global variables
# - None
# - Functions with conditions
# - Functions with loops
# - Functions with lists
# - Functions with dictionaries
# - Calling one function from another


# ---------------------------------------------------------------------------------------------------------------------------------------------

#                                                                function

# what is function?
# a function is block of resuable code that performs a specific task
# defining a function: a function can be drfined using def keyword. 
# def function_name(parameters):
         #statements          
#        return expression

# calling a function : after creating a function, call it using the name of the functions followed by parenthesis 
# def function_name(parameters):
         #statements          
#        return expression
# function_name()

def hello():
    print("hello")
hello()

# output:
# hello

# we can call it as many time as we want


def hello():
    print("hello")
hello()
hello()
hello()
hello()
hello()

# output:
# hello
# hello
# hello
# hello
# hello

# ---------------------------------------------------------------------------------------------------------------------------------------------

# function without parameters
def welcome():
    print("welcome to my python learning course")
welcome()

# output:
# welcome to my python learning course

# ---------------------------------------------------------------------------------------------------------------------------------------------

# function with parameters
# parameters allow us to give data to a funcyion

def hello(name):  #name-> parameter
    print("hello",name)
hello("dolly")    #dolly -> argument
hello("anu")      #anu -> argument
hello("adiba")    #adiba -> argument

# output:
# hello dolly
# hello anu
# hello adiba


# ---------------------------------------------------------------------------------------------------------------------------------------------

# multiple parameters

def add(a,b):
    print(a+b)
add(10,15)

# output:
# 25

def student(name,age):
    print("name:",name)
    print("age:",age)
student('dolly',20)

# output:
# name: dolly
# age: 20
# ---------------------------------------------------------------------------------------------------------------------------------------------

#                                        type of functional argument:

#1. default  parameters:
# you can give parameter a default value, which can be used when no value is passed during function call

def greet(name="user"):
    print("hello",name)
greet("dolly")
greet()  # no value is passed so the default value will be used

# output:
# hello dolly
# hello user

def add(a,b=10):
    print(a+b)
add(87)

# output:
# 97

# ---------------------------------------------------------------------------------------------------------------------------------------------

# 2.keyword argument:
# pass values using parameter names, so argument order does not metter

def student(name,age):
    print("name",name)
    print("age:",age)
student(age=20,name="dolly")

# output:
# name dolly
# age: 20

# ---------------------------------------------------------------------------------------------------------------------------------------------
# 3.positional argument:
# values are assigned to parametes based on their order in the function call
def student(name,age):
    print("name",name)
    print("age",age)
student("dolly",20)

# output:
# name dolly
# age: 20

# ---------------------------------------------------------------------------------------------------------------------------------------------

# Return 
# return is used to end a function and send a value back to the caller

def add(a,b):
    return a+b
result=add(76,64)
print(result) 
print(add(20,10))

# output:
# 140
# 30

# difference between print() and return:
# print()display result
# return : return the value so we can use it later

def add(a, b):
    print(a + b)  # it will display the value 30

x = add(10, 20)

print(x) # give None because x has nothing

# 30
# None

def add(a, b):
    return a+b

x = add(10, 20)

print(x)

# output:
# 30

# ---------------------------------------------------------------------------------------------------------------------------------------------

# Function Returning Multiple Values
# python can return multiple values

def arithmetic(a,b):
    total=a+b
    difference=a-b
    multiplication=a*b
    division=a/b
    return total,difference,multiplication,division

def arithmetic(a,b):
    total=a+b
    difference=a-b
    multiplication=a*b
    division=a//b
    return total,difference,multiplication,division
sum,subt,mult,div=arithmetic(87,56)
print("sum:",sum)
print("substraction:",subt)
print("multiplication:",mult)
print("division:",div)

# output:
# sum: 143
# substraction: 31
# multiplication: 4872
# division: 1


# ---------------------------------------------------------------------------------------------------------------------------------------------
#                                            type of variable:
# local variable:
# local variable are defined inside a function and exist only during its execution.
# they cannot be accessed from outside the function.

def hello():
    a="hi"
    print(a)
hello()

# output:
# hi

def hello():
    a="hi"
    print("local:",a)
hello()
print("outside local",a)

# print("outside local",a)
                        #   ^
# NameError: name 'a' is not defined



# ---------------------------------------------------------------------------------------------------------------------------------------------

# global variable:
# global variable are declared outside all function and can be accessed anywhere in the program, including inside function

a="hi"
def hello():
    print("inside function:",a)
hello()
print("outside function:",a)

# output:
# inside function: hi
# outside function: hi

# ---------------------------------------------------------------------------------------------------------------------------------------------
# use of both global and local variable:
# if variable is defined both globaly and locally with same name ,local variable shadows the global variable inside the function.
# changes to local variable do not affect the global variable unless explicitly declare variable as global

def hello():
    a="hi" #local
    print("inside function:",a)

a="hello" #global
hello()
print("outside function:",a)

# output:
# inside function: hi
# outside function: hello


# ---------------------------------------------------------------------------------------------------------------------------------------------

# modifying global variable inside a function:
# bydefault ,one cannot modify a global variable inside a function without declaring it as global

# without global key: error

def hello():
    a+="namaste"
    print(a)

a="hello ji,"
hello()

# a+="namaste"
    # ^
# UnboundLocalError: cannot access local variable 'a' where it is not associated with a value

# with global key

def hello():
    global a
    a+=" namaste"   #global value modifided
    print(a)
a="hello ji,"
print(a)  # global value print 
hello()

# output:
# hello ji,
# hello ji, namaste


a = 1  # Global variable

def f():
    print("f():", a)  # Uses global a

def g():
    a = 2  # Local shadows global
    print("g():", a)

def h():
    global a
    a = 3  # Modifies global a
    print("h():", a)

print("global:", a)
f()
print("global:", a)
g()
print("global:", a)
h()
print("global:", a)

# output:
# global: 1
# f(): 1
# global: 1
# g(): 2
# global: 1
# h(): 3
# global:3

# ---------------------------------------------------------------------------------------------------------------------------------------------

# function +condition:
 
def even_odd(num):
    if num%2==0:
        return "even"
    else:
        return "odd"

print(even_odd(12))
print(even_odd(37))

# output:
# even
# odd


# ---------------------------------------------------------------------------------------------------------------------------------------------

# function with loop:

def print_even(num):
    for i in num:
        if i%2==0:
             print("even",i)

list=[20,23,24,42,67]
print_even(list)

# output:
# even: 20
# even: 24
# even: 42

# ---------------------------------------------------------------------------------------------------------------------------------------------

# function +list:

def largest_number(num):
    highest=num[0]
    for i in num:
        if i>highest:
            highest=i
    return highest

list=[10, 50, 20, 90, 30]
print(largest_number(list))

# output:
# 90

# ---------------------------------------------------------------------------------------------------------------------------------------------

# function+dictionary:

def details(d):
    for key,value in d.items():
        print(key,":",value)

dict={
    "name":"dolly",
    "age":20,
    "course":"python"
}
details(dict)

# output:
# name : dolly
# age : 20
# course : python

# ---------------------------------------------------------------------------------------------------------------------------------------------


# Function Calling Another Function

def square(n):  #line 1
    return n*n   #line2
def cube(n):     #line3
    return square(n)*n   #line 4
print(cube(3))            #line 5

# output:
# 27
# line of execution is  5-3-4-1-2-4-5


# ---------------------------------------------------------------------------------------------------------------------------------------------

# none
# if a function doesn't return anything explicitly

def hello():
    print("hello")
x=hello()
print(x)

# output:
# hello
# None

# ---------------------------------------------------------------------------------------------------------------------------------------------

#                                                     practice

# ---------------------------------------------------------------------------------------------------------------------------------------------
# Greeting Function
# Create:
# greet("Dolly")

# Expected:
# Hello Dolly
# Welcome to Python

def greet(a):
    print("Hello",a)
    print("welcome to python")
greet("Dolly")

# output:
# Hello Dolly
# welcome to python

# ---------------------------------------------------------------------------------------------------------------------------------------------
# Addition
# Create:
# add(10, 20)

# Expected:
# 30
# Use return.

def add(a,b):
    return a+b
print(add(10,20))

# output:
# 30

# ---------------------------------------------------------------------------------------------------------------------------------------------
# Create and check even odd:

def check_even_odd(n):
    if n%2==0:
        return "even" 
    else:
        return "odd"

print(check_even_odd(15))

print(check_even_odd(22))

print(check_even_odd(48))

# output:
# odd
# even
# even


# ---------------------------------------------------------------------------------------------------------------------------------------------
# Square

# Create a function that accepts a number and returns its square

def square(n):
    return n*n
print("square:",square(9))

# output:
# square: 81
 

# ---------------------------------------------------------------------------------------------------------------------------------------------

# Largest
# Create and find the largest 

def largest(a,b,c):
    if a>b:
        if a>c:
            return a
        else:
            return b
    else:
        if b>c:
            return b
        else:
            return c
print(largest(10,50,30))

# output:
# 50

# ---------------------------------------------------------------------------------------------------------------------------------------------

# Count Even and Odd

def  count_even_odd(num):
    even=0
    odd=0
    for i in num:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd

number=[10,15,20,25,30,25,29]
even,odd=count_even_odd(number)
print("even:",even)
print("odd:",odd)

# output:
# even: 3
# odd: 4


# ---------------------------------------------------------------------------------------------------------------------------------------------

# Sum of List

def sum(list):
    count=0
    for i in list:
        count+=i
    print("total sum=",count)
        
list=[10,20,30,40,50]
sum(list)

# output:
# total sum= 150


# ---------------------------------------------------------------------------------------------------------------------------------------------

# Find Largest and Smallest

def largest_smallest(list):
    smallest=list[0]
    largest=list[0]
    for i in list:
        if i>largest:
            largest=i
        if i<smallest:
            smallest=i
    return largest,smallest
list=[89,34,83,45,98,73]
large,small=largest_smallest(list)
print("largest:",large)
print("smallest:",small)

# output:
# largest: 98
# smallest: 34


# ---------------------------------------------------------------------------------------------------------------------------------------------

# Count Positive and Negative

def count_positive_negative(list):
    positive=0
    negative=0
    zero=0
    for i in list:
        if i>0:
            positive+=1
        elif i<0:
            negative+=1
        else:
            zero+=1

    print("positive:",positive)
    print("negative:",negative)
    print("zeros:",zero)
list=[10,-5,-20,8,0,58,-40,0]
count_positive_negative(list)

# output:
# positive: 3
# negative: 3
# zeros: 2
            
# ---------------------------------------------------------------------------------------------------------------------------------------------

# Prime Function

def is_prime(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    if count>2:
        print("False")
    else:
        print("True")
is_prime(10)
is_prime(17)

# output:
# False
# True

# ---------------------------------------------------------------------------------------------------------------------------------------------

# Factorial Function
def factorial(n):
    factorials=1
    for i in range(1,n+1):
        if i>=1:
            factorials*=i
    print("factorial:",factorials)
factorial(5)

# output:
# 120


# ---------------------------------------------------------------------------------------------------------------------------------------------

# Reverse Number
def reverse(n):
    reverse=0
    while n>0:
         reverse=reverse*10+n%10 
         n=n//10
    print("reverse:",reverse)
reverse(123)

# output:
# reverse: 321


# ---------------------------------------------------------------------------------------------------------------------------------------------

# Armstrong Function

def amstrong(n):
    a=0
    num=n
    while n>0:
        a=a+(n%10)**3
        n=n//10
    if num==a:
        print(num,"is an amstrong number")
    else:
        print(num,"is not an amstrong number")

amstrong(153)
amstrong(875)

# output:
# 153 is an amstrong number
# 875 is not an amstrong number


# ---------------------------------------------------------------------------------------------------------------------------------------------

# Frequency Counter Function

def frequency(num):
    frequency={}
    for i in num:
        if i in frequency:
            frequency[i]+=1
        else:
            frequency[i]=1
    for i in frequency:
        print(i,"->",frequency[i])
list=[10,20,10,30,20,10]
frequency(list)  

# output:
# 10 -> 3
# 20 -> 2
# 30 -> 1

# ---------------------------------------------------------------------------------------------------------------------------------------------

# Calculator Using Functions

def add(a,b):
    return a+b
def substract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
num1=int(input("enter first number: "))
num2=int(input("enter second number: "))
operation=input("enter operation: ")
if operation=="+":
    print("addition:",add(num1,num2))
elif operation=="-":
    print("substraction:",substract(num1,num2))
elif operation=="*":
    print("multiplication:",multiply(num1,num2))
elif operation=="/":
    print("divide:",divide(num1,num2))
else:
    print("please enter valid operation!!") 

# output:
# enter first number: 30
# enter second number: 10
# enter operation: *
# multiplication: 300




# ---------------------------------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------------------------------