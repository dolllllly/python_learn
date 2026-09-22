# python programming practice-
# DAY-01
# topic:python fundamentals & conditional logic
# .............
# topics covered:
# --variable and data types
# --user input and output
# --arithmetic operators
# --comparison and logical operator
# --conditional statement
# --basic problem solving
# --practical application




#print your name and your course
print("Hello, my name is dolly.")
print("I am an MCA student.")
#output:
# Hello, my name is dolly.
# I am an MCA student.

# .......................................................................................

#text data type
# string-used to represent textual data
# type-str
name="dolly"
print(name)
print(type(name))

#output
#  dolly
# <class 'str'>

# -----------------------------------------------------------------------------------------------------------

# number data type-integer,float,complex 
# integer-store whole number
# type-int
age=20
print(age)
print(type(age))

# output
# 20
# <class 'int'>

# ---------------------------------------------------------------------------------------------------------------

# float-store decimal number
# type-float
amount=10.02
print(amount)
print(type(amount))

# output
# 10.02
# <class 'float'>

# ---------------------------------------------------------------------------------------------------------------

# complex number-number with real and imagenary part
# type-complex

a=5+6j
print(a)
print(type(a))

# output
# (5+6j)
# <class 'complex'>

# --------------------------------------------------------------------------------------------------------------

# sequence data type: order collection of item
# list- ordered and changeable character enclosed within square bracket[]
# type-int

list1=[11,12,13,24]
print(list1)
print(type(list1))

# output
# [11, 12, 13, 24]
# <class 'list'>

# -----------------------------------------------------------------------------------------------------------------

# Tuple- ordered and unchangeable character enclosed within parenthesis()
# type-tuple

tuple1=(1,2,3,4,5)
print(tuple1)
print(type(tuple1))

# output
# (1, 2, 3, 4, 5)
# <class 'tuple'>

# -----------------------------------------------------------------------------------------------------------------

# range-sequence of number
# type-range

a=range(1,6)
print(type(a))
print(list(a))

# output
# <class 'range'>
# [1, 2, 3, 4, 5]

# --------------------------------------------------------------------------------------------------------------------

# mapping type
# dictionary-store data in key- value pair where key is unique and value can be any data type and enclosed within curly bracket{}
# type-dict

info={
    "name":"Dolly",
    "age":20,
    "course":"python",
    "passed":True
}
print(info)
print(type(info))

# output
# {'name': 'Dolly', 'age': 20, 'course': 'python', 'passed': True}
# <class 'dict'>

# -----------------------------------------------------------------------------------------------------------------------

# set type
# set-unorder collection of unique item enclosed wihin curly bracket {}
# type-set

fruit={"mango","apple","banana"}
print(fruit)
print(type(fruit))

# output:
# {'banana', 'mango', 'apple'}
# <class 'set'>

# -----------------------------------------------------------------------------------------------------------------

#  boolen type:represent True and False value
# type-bool

a=True
print(a)
print(type(a))

# output:
# True
# <class 'bool'>

# ----------------------------------------------------------------------------------------------------------------------

#  None Type: represent ni value or empty state
# type-NoneType

a=None
print(a)
print(type(a))

# output:
# None
# <class 'NoneType'>

# ---------------------------------------------------------------------------------------------------------------------------
#create variables and and print them
#print your name,age,collage,city
name="Dolly"
age=20
collage="PES University"
city="Bangalore"
print("my name is",name)
print("my age is",age)
print("i am studying in",collage)
print("i am living in",city)
#output:
# my name is Dolly
# my age is 20
# i am studying in PES University
# i am living in  Bangalore

# ..................................................................................

# operators
#Basic arithmetic operations on two variables
a=25
b=10
print("addition of two given number is",a+b)
print("substraction of two number is",a-b)
print("multiplication of two number is",a*b)
print("division of two number is",a/b)
#output:
# addition of two given number is 35
# substraction of two number is 15
# multiplication of two number is 250
# division of two number is 2.5

# .................................................................................


#user input ...asking user for their name and age and print them
name=input("enter your name: ")
age=int(input("enter your age: "))
print("your name is",name)
print("your age is",age)
#output:
# enter your name: dolly
# enter your age: 20
# your name is dolly
# your age is 20

# ..............................................................

#take two number from user and perform arithmetic operations
a=int(input("enter first number:"))
b=int(input("enter your second number:"))
print(f'additio of two number is {a+b}')
print("substraction of two number is",a-b)
print("multiplication of two number is",a*b)
print(f'division of two number is {a/b}')
# output:
# enter first number:80
# enter your second number:40
# additio of two number is 120
# substraction of two number is 40
# multiplication of two number is 3200
# division of two number is 2.0

# ...................................................

#rectangle area,ask user for length and breadth and print the area of the rectangle
length=int(input("enter the length of the rectangle:"))
breadth=int(input("enter the breadth of the rectangle:"))
area=length*breadth
print("area of the rectangle is",area)
# outhput:
# enter the length of the rectangle:7
# enter the breadth of the rectangle:8
# area of the rectangle is 56

#......................................................... 

#age..ask user for their birth year andcalculate and  print their approximate age using current year
birth_year=int(input("enter your birth year:"))
current_year=2026
age=current_year-birth_year
print("ypur approximate age is",age)
# output:
# enter your birth year:2006
# ypur approximate age is 20

# ...............................................

# mark sheet...ask user for their marks in 5 subject and calculate and print their total marks,average marks and percentage
subject1=int(input("enter your marks in first subject:"))
subject2=int(input("enter your marks in second subject:"))
subject3=int(input("enter your marks in thiird subject:"))
subject4=int(input("enter ypour marks in fourth subject:"))
subject5=int(input("enter your marks in fifth subject:"))
total_marks=subject1+subject2+subject3+subject4+subject5
average_marks=total_marks/5
percentage=(total_marks/500)*100
print("your total marks is",total_marks)
print("your average marks is",average_marks)
print("your percentage is",percentage)

# output:
# enter your marks in first subject:89
# enter your marks in second subject:80
# enter your marks in thiird subject:90
# enter ypour marks in fourth subject:95
# enter your marks in fifth subject:98
# your total marks is 452
# your average marks is 90.4
# your percentage is 90.4

# .................................................

#temprature conversion...ask user for temprature in celsius and convert it into fahrenheits and print it
# f=(c*9/5)+32
celcius=int(input("enter temprature in celcius: "))
fahrenheits=(celcius*9/5)+32
print("temprature in fehrenheits is",fahrenheits)

# output:
# enter temprature in celcius: 876
# temprature in fehrenheits is 1608.8

# .............................................................

# mini introductionprogram...ask user for their name,age,city,course and print them as one introductions
age=int(input("enter your age : "))
city=input("enter your city :")
course=input("enter your course : ")
print(f'hello my name is {name} . and i am {age} years old . i am currenttly living in {city} and i am pursuing {course} course')

# output:
# enter your name : dolly
# enter your age : 20
# enter your city :bangalore
# enter your course : MCA
# hello my name is dolly . and i am 20 years old . i am currenttly living in bangalore and i am pursuing MCA course

# .............................................................................................

#salary calculator...ask user for their basic salary ,HRA,DA and tax percentage and calulate gross salary, tax
#  and net salary and peint them
name=input("enter your name : ")
basic_salary=int(input("enter your basic salary:"))
HRA=int(input("enter your HRA:"))
DA=int(input("enter your DA:"))
tax_percentage=int(input("enter your tax percentage:"))
gross_salary=basic_salary+HRA+DA
tax=(gross_salary*tax_percentage)/100
net_salary=gross_salary-tax
print("employee name:",name)
print("gross salary:",gross_salary)
print("tax:",tax)
print("net salary:",net_salary)

# output:
# enter your name : dolly behera
# enter your basic salary:50000
# enter your HRA:20000
# enter your DA:5000 
# enter your tax percentage:5
# employee name: dolly behera
# gross salary: 75000
# tax: 3750.0
# net salary: 71250.0

# .......................................................................

# shopping bill...ask user for their name,phone number, price of each item and claculate their subtotal,add 18%gst and final bill and print them
name=input("enter the customer name:")
phone_number=int(input("enter the customer phone number:"))
laptop_price=int(input('enter the price of the laptop:'))
mouse_price=int(input("enter the price of the mouse:"))
keyboard_price=int(input("enter the price of the leyboard:"))
gst_percentage=int(input("enter the gst percentage:"))
subtotal=laptop_price+mouse_price+keyboard_price
gst=(subtotal*gst_percentage/100)
final_bill=subtotal+gst
print("dk electronics store")
print("customer name:",name)
print("phone number:",phone_number)
print("subtotal:",subtotal)
print("gst added:",gst)
print("fnal bill:",final_bill)
print("thank you for shopping with us!")

# output:
# enter the customer name:dolly behera
# enter the customer phone number:87875634769
# enter the price of the laptop:60000
# enter the price of the mouse:2000
# enter the price of the leyboard:3000 
# enter the gst percentage:18
# dk electronics store
# customer name: dolly behera
# phone number: 87875634769
# subtotal: 65000
# gst added: 11700.0
# fnal bill: 76700.0
# thank you for shopping with us!

# ............................................................

# time converter..ask user for the second and then convert it to hours+minutes+seconds
total_seconds=int(input("enter the seconds:"))
hours=total_seconds//3600
reminder1=total_seconds%3600
minutes=reminder1//60
seconds=reminder1%60
print("total seconds:",total_seconds)
print(hours,"hours")
print(minutes,"min")
print(seconds,"seconds")

# output:
# enter the seconds:797989
# total seconds: 797989
# 221 hours
# 39 min
# 49 seconds

# ......................................................

#electricity bill...ask user for their electricity units as input and calculate the bill using :
# first 100 units-> rs 2/unit
# next 100 units-> rs3/units
# above 200 units-> rs5/units
units=int(input("enter your electriciy bill:"))
if units<=100:
    print("rs.",units*2)
elif 100<units<=200:
    print(200+(units-100)*3)
else:
    print(500+(units-200)*5)

# output:
# enter your electriciy bill:200
# 500

# .....................................................................


# ATM withdrawal..ask user for their account balance and the withdrawal amount..withdrawal must be multiple of 100 ,cannot exceed balance,and maintain a minimum balance of 500 and calculate the ramaining balance and ptint them
account_balance=int(input("enter your totaal account balance:"))
withdrawal_amount=int(input("enter the ampount you want to withdrawal:"))
if withdrawal_amount%100==0 and account_balance-withdrawal_amount>=500:
    print("your remaining balance is",account_balance-withdrawal_amount)
else:
    print("please follow the rule of withdrawal")

# output:
# enter your totaal account balance:6000
# enter the ampount you want to withdrawal:5500
# your remaining balance is 500

# enter your totaal account balance:600
# enter the ampount you want to withdrawal:300
# please follow the rule of withdrawal

# enter your totaal account balance:60000
# enter the ampount you want to withdrawal:55500
# your remaining balance is 4500

# .........................................................................

# student grade system ...take marks of 5 subject from the user and calculate percentage and assign grade-
# 90+->A+
# 80-89 ->A 
# 70-79 ->B 
# 60-69 ->C 
# 50-59 ->D 
# Below 50 ->F
# and also check whether the student has passed every subject
name=input("enter student name:")
subj1=int(input("enter the marks of first subject:"))
subj2=int(input("enter the marks of second subject:"))
subj3=int(input("enter the marks of third subject:"))
subj4=int(input("enter the marks of fourth subject:"))
subj5=int(input("enter the marks of fifth subject:"))
total_mark=subj1+subj2+subj3+subj4+subj5
print("Name:",name)
print("Total mark:",total_mark)
percentage=total_mark/500*100
print("Percentage:",percentage)
if percentage>=90:
    print("Grade:A+")
elif 80<=percentage<=89:
    print("Grade:A")
elif 70<=percentage<=79:
    print("Grade:B")
elif 60<=percentage<=69:
    print("Grade:C")
elif 50<=percentage<=59:
    print("Grade:D")
else:
    print("Grade:F")

if subj1>30 and subj2>30 and subj3>30 and subj4>30 and subj5>30:
    result="passed"
else:
    result="failed"
print("Result:",result)

# # output:
# enter student name:dolly
# enter the marks of first subject:23
# enter the marks of second subject:87
# enter the marks of third subject:90  
# enter the marks of fourth subject:99
# enter the marks of fifth subject:89
# Name: dolly
# Total mark: 388
# Percentage: 77.60000000000001
# Grade:B
# Result: failed

# enter student name:dolly
# enter the marks of first subject:89
# enter the marks of second subject:99
# enter the marks of third subject:89
# enter the marks of fourth subject:79
# enter the marks of fifth subject:89
# Name: dolly
# Total mark: 445
# Percentage: 89.0
# Grade:A
# Result: passed

# Number Analysis ...take three numbers from the user without using python's max() or min():
num1=int(input("enter the first number:"))
num2=int(input("enter your second number:"))
num3=int(input("enter your third number:"))
if num1>num2:
    if num1>num3:
        print(num1,"is the largest number")
    else:
        print(num3,"is the largest")
else:
    if num2>num3:
        print(num2,"is the largest")
    else:
        print(num3,"is the largest")


num1=int(input("enter the first number:"))
num2=int(input("enter your second number:"))
num3=int(input("enter your third number:"))
if num1>num2:
    if num1>num3:
        print(num1,"is the largest number")
    else:
        print(num3,"is the largest")
else:
    if num2>num3:
        print(num2,"is the largest")
    else:
        print(num3,"is the largest")

# output:
# enter the first number:87
# enter your second number:879
# enter your third number:77
# 879 is the largest


# simple calculator

num1=float(input("enter the first number:"))
num2=float(input("enter your second number:"))
print("operation avaailable are addition,substraction,division,multiplicatonabd reminder..")
operation=input("enter the operation you want to perforn:")
if operation=="addition":
    result=num1+num2
elif operation=="substraction":
    result=num1-num2
elif operation=="division":
    result=num1/num2
elif operation=="multiplication":
    result=num1*num2
elif operation=="reminder":
    result=num1%num2
else:
    print("please enter the correct operation")
print(num1,operation,num2,"=",result)

# output:
# enter the first number:90
# enter your second number:30
# operation avaailable are addition,substraction,division,multiplicatonabd reminder..
# enter the operation you want to perforn:addition
# 90.0 addition 30.0 = 120.0

#...........................................................................
  
# ATM withdrawal system
account_balance=int(input("enter your account balance:"))
withdrawal_amount=int(input("enter the amount you want to withdraw:"))
pin=int(input("enter your account pin:"))
actual_pin=1234
if pin==actual_pin:
    if account_balance-withdrawal_amount>=500 and withdrawal_amount%100==0:
        print("Withdrawal succeessfull !")
        print("Amount withdrawal:",withdrawal_amount)
        print("Remaining balance:",account_balance-withdrawal_amount)
    else:
        print("Withdrawal denied !")
        print("Minimum balanced of 500 must be maintained.")
else:
    print("Incorrect PIN")

# output:
# enter your account balance:3000
# enter the amount you want to withdraw:2590
# enter your account pin:1234
# Withdrawal denied !
# Minimum balanced of 500 must be maintained.

# enter your account balance:3000
# enter the amount you want to withdraw:2000
# enter your account pin:1111
# Incorrect PIN

# enter your account balance:3000
# enter the amount you want to withdraw:1000
# enter your account pin:1234
# Withdrawal succeessfull !
# Amount withdrawal: 1000
# Remaining balance: 2000

# ---------------------------------------------------------------------------------------------

# employee promotions or bonous or warnning based on rating,total project done by them,
# their attendence and customer feedback score
 
employee_name=input("enter employee name:")
rating=int(input("enter the rating of the employee:"))
total_project=int(input("enter the number of project done by the employee:"))
attendance=int(input("enter the attendence out of 100:"))
customer_feedback=int(input("enter the customer feedback score from scale 1-10:"))

if rating>=4 and total_project>=8 and attendance>=90:
    print(f'{employee_name} is eligible for promotion:')
else:
    print(f'{employee_name} is not eligible for promotion')

if rating>=4 and customer_feedback>=8:
# if rating>=4 and customer_feedback>=8 or (total_project>=10 or attendance>=95):
    if total_project>=10 or attendance>=95:
        print(employee_name,"will receive a bonous.")
else:
    print(employee_name,"will not receive any bonous.")

if rating<3:
    if attendance<80 or total_project<5:
        print(employee_name,"will receive a warning letter.")
    else:
        print(employee_name,"will be fired.")
else:
    print(employee_name,"has no warning.")

# ---------------------------------------------------------------------------------------------