# python programming practice----
# Day 2
# topic:loop and iterative problem solving
# --------------
# topic coverd:
# --for loop
#--while loop
# --range()
# --break
# --continue
# --pass
# --counter and accumulators
# --conditional logic inside loops
# --iterative problem solving
# -------------------------------------------
# -------------------------------------------

# using a for loop, print number from 1 o 20
for i in range(1,21):
    print(i)

# output:
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
# 11
# 12
# 13
# 14
# 15
# 16
# 17
# 18
# 19
# 20

# ---------------------------------------------------------

# using a while loop, print number from 1 o 20
i=1
while i<21:
    print(i)
    i=i+1

# output:
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
# 11
# 12
# 13
# 14
# 15
# 16
# 17
# 18
# 19
# 20

# ---------------------------------------------------------

# using while loop ,print all even numbers from 2 to 20.

i=1
while i<21:
    if i%2==0:
        print(i)
    i+=1
# output:
# 2
# 4
# 6
# 8
# 10
# 12
# 14
# 16
# 18
# 20

# ------------------------------------------------------------------

# using for loop ,print all even numbers from 2 to 20.
for i in range(1,21):
    if i%2==0:
        print(i)

#output:
#  2
# 4
# 6
# 8
# 10
# 12
# 14
# 16
# 18
# 20

# ------------------------------------------------------------

# skip numbers from 1 to 20,but skip numbers divisible by 3.

for i in range(1,21):
    if i%3==0:
       continue
    print(i)

# output
# 1
# 2
# 4
# 5
# 7
# 8
# 10
# 11
# 13
# 14
# 16
# 17
# 19
# 20

# --------------------------------------------------------------------------

# print all the number and break the loop when it reach 10
i=1
while i>=1:
    if i==10:
        break
    print(i)
    i+=1

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

# -------------------------------------------------------------------------------------

# Palindrome Number

num=int(input("enter any number:"))
n=num
result=0
while num>0:
    y=num%10
    result=result*10+y
    num=num//10
print(result)
if result==n:
    print("palindrome" ) 
else:
    print("not palindrome")

# output:
# enter any number:1234
# 4321
# not palindrome

# enter any number:12321
# 12321
# palindrome

# ------------------------------------------------------------------------------------------------
# Largest Digit among the number user input
num=int(input("enter any number:" ))
result=0
while num>0:
    digit=num%10
    if digit>result:
        result=digit
    num=num//10
print(result)

# output:
# enter any number:7659
# 9

# ------------------------------------------------------------------------------------------------

# ask user for number continiously in a loop...and print positive for positive number ,break if the number is 0 and print negative for negative number
while True:
    num=int(input("enter a number:"))
    if num>0:
        print("positive")
    elif num==0:
        break
    else:
        print("negative")

# output
# enter a number:9
# positive
# enter a number:-2
# negative
# enter a number:0  

# --------------------------------------------------------------------------

num=int(input("enter any number:"))
result=count=result2=count2=0
for i in range(1,num+1):
    if i%2==0:
        result+=i
        count+=1
    elif i%2!=0:
        result2+=i
        count2+=1
print("odd count",count2)
print("odd sum:",result2)
print("even sum:",result)
print("even count",count)

# output:
# enter any number:10
# odd count 5
# odd sum: 25
# even sum: 30
# even count 5


# -----------------------------------------------------------------------
#  * print 

for i in range(5):
    for j in range(5):
        print("*",end=" ")
    print()

# output:
# * * * * * 
# * * * * * 
# * * * * * 
# * * * * * 
# * * * * * 

for i in range(1,6):
    for j in range(i):
        print("*",end=" ")
    print()

# output
# * 
# * * 
# * * * 
# * * * * 
# * * * * *

for i in range(5,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()

# output:
# * * * * * 
# * * * * 
# * * * 
# * * 
# * 

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

# output:
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5 

for i in range(6):
    for j in range(6):
        if i==0 or i==5 or j==0 or j==5:
          print("*",end=" ")
        else:
           print(" ",end=" ")
    print()

# output:
# * * * * * * 
# *         * 
# *         * 
# *         * 
# *         * 
# * * * * * * 
        

