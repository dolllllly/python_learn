# python programming practice----
# Day 3
# ---------------------------------------------------------
# -String basics
# - String indexing
# - Positive and negative indexing
# - String slicing
# - String length using `len()`
# - String methods
# - `upper()`, `lower()`, `title()`
# - `strip()`, `lstrip()`, `rstrip()`
# - `replace()`
# - `find()`
# - `count()`
# - `startswith()` and `endswith()`
# - `split()` and `join()`
# - String traversal using loops
# - String immutability
# - String-based problem solving



# ------------------------------------------------------------------------------------------------------------------

# sting indexing both positive and negative indexing
#  0   1   2   3   4   5 positive indexing start with 0
#  P   Y   T   H   O   N
# -6  -5  -4  -3  -2   -1  negative indexing start from right side with -1


name="dolly behera"
print(name)
print("first letter:",name[0])
print("last letter:",name[-1])
print("second letter:",name[1])
print("third letter:",name[2])

# output
# dolly behera
# first letter: d
# last letter: a
# second letter: o
# third letter: l

# -------------------------------------------------------------------------------------------------------------------

# String slicing [starting index:stop index:step] it doesn't include stop index value
name="Dolly Behera"
print("original text:",name)
print("bydefault: ",name[:])
print("first name:"name[0:5])
print("last name",name[6:12])
print("step slicing:",name[0:12:2])
print("reverse slicing:",name[::-1])
print("negative slicing:",name[-12:-7])

# original text: Dolly Behera
# bydefault:  Dolly Behera
# first name: Dolly
# last name Behera
# step slicing: DlyBhr
# reverse slicing: areheB ylloD
# negative slicing: Dolly


# --------------------------------------------------------------------------------------------------
#  String methods
# --------------------------------------------------------------------------------------------------

# upper() and lower()
# Take a name from the user and print:
# Original name
# Uppercase
# Lowercase
# Title case

name=input("enter your name:")
print("original name:",name)
print("uppercase name",name.upper())
print("lowercase name:",name.lower())
print("propercase name:",name.title())

# output:
# enter your name:DollY beHERa
# original name: DollY beHERa
# uppercase name DOLLY BEHERA
# lowercase name: dolly behera
# propercase name: Dolly Behera

# --------------------------------------------------------------------------------

# len()
# Take a string and print:
# First character
# Last character
# Length

name=input("enter your name:")
length=len(name)
print("lemgth:",length)
print("first character:",name[0])
print("last character:",name[length-1])

# output:
# enter your name:dolly
# lemgth: 5
# first character: d
# last character: y


# -------------------------------------------------------------------------------------
# replace("old one","new one")
name="dolly behera"
print("original name:",name)
print("replaced name:",name.replace("dolly","devi"))

# output:
# original name: dolly behera
# replaced name: devi behera

# -----------------------------------------------------------------------------------------------------------------------------

# count()-count the occurrence of a letter of word

name="i am learning codding"
print("count of i",name.count("i"))

# output:
# count of i: 3

# -----------------------------------------------------------------------------------------------------------------------------

# strip()-remove space
name="    python by dolly    "
print("original:",name)
print("after removing space:",name.strip())

# output:
# original:     python by dolly    
# after removing space: python by dolly

# --------------------------------------------------------------------------------------------------------

# endwith("words") check if text end with something .it return True or False
# startwith("words") check if text starts with something .it return True or False
name="python by dolly"
print("start with python?:",name.startswith("python"))
print("end with python?:",name.startswith("dolly"))

# output
# start with python?: True
# end with python?: True

# --------------------------------------------------------------------------------------------------------
# isnumeric()
# isalpha()
# isalnum()

name="dolly"
age="20"
id="dolly83"
print("is numeris:",age.isnumeric())
print("is alphabate:",name.isalpha())
print("is numeris:",name.isnumeric())
print("is alphanumeric:",id.isalnum())

# output:
# is numeris: True
# is alphabate: True
# is numeris: False
# is alphanumeric: True

# ----------------------------------------------------------------------------------------------
#
# split() split string into list of words

name="hi my name is dolly"
print("word list:",name.split())

# output:
# word list: ['hi', 'my', 'name', 'is', 'dolly']

fruit="apple,orange,mango,bluebarry"
print("word list:",fruit.split(","))
print(fruit)

# output:
# word list: ['apple', 'orange', 'mango', 'bluebarry']
# apple,orange,mango,bluebarry

# ------------------------------------------------------------

# join() conbine string

name=["python","by","dolly"]
sentence=" ".join(name)
hypen="-".join(name)
print(sentence)
print(hypen)

# output:
# python by dolly
# python-by-dolly

# ---------------------------------------------------------------------------------------
# find() --it return the string index ..if the string isn't found it return -1

name="hi my name is dolly"
print(name.find("dolly"))
print(name.find("hi"))
print(name.find("python"))

# output:
# 14
# 0
# -1

# --------------------------------------------------------------------------------------------------

# character traversal--you can loop through every character in a string

name="dolly"
for ch in name:
    print(ch)

# output
# d
# o
# l
# l
# y

# --------------------------------------------------------------------------------------------------

# sting are immutable

name= "Python"
name[0] = "J"

# error
# TypeError: 'str' object does not support item assignment

# insted of these we can make a new string
name="python"
name1="j"+name[1:]
print(name1)

# output
# jython

# -------------------------------------------------------------------------------------------

# data cleaning example

price_text="price: $3500/-"
clean_price=price_text.replace("price: ","")\
                               .replace("$","") \
                            .replace("/-","")
print(clean_price)

# output:
# 3500

# ------------------------------------------------------------------------------------------------
# Take a word and print it in reverse.

name=input("enter your name:")
print(name[::-1])

# output:
# enter your name:Devi
# iveD

# ----------------------------------------------------------------------------------------------------

# Take a string and count the number of characters.
# Don't use len().

name=input("enter the name:")
count=0
for ch in name:
    count+=1
print(count)

# output:
# enter the name:devi
# 4

# --------------------------------------------------------------------------------------------

#Take input -- Count Vowels and Consonants

name=input("enter any name:")
vowels=consonants=0
for ch in name:
    if ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u":
         vowels+=1
    elif ch==" ":
         result=0
    else:
        consonants+=1
print("vowels:",vowels)
print("consonants:",consonants)

# output:
# enter any name:aeiou
# vowels: 5
# consonants: 0
# enter any name:dollly
# vowels: 1
# consonants: 5

# -----------------------------------------------------------------------------------

# Character Frequency without  .count()

name=input("enter any name:")
character=input("enter the character you want to check its total occurance:")
count=0
for ch in name:
    if ch==character:
        count+=1
print("total occurance:",count)

# output
# enter any name:elephant
# enter the character you want to check its total occurance:e
# total occurance: 2

# -------------------------------------------------------------

# Reverse Without Slicing
 
text=input("enter any text:")
reverse=""
i=len(text)-1
while i>=0:
    reverse=reverse+text[i]
    i-=1
print("original text:",text)
print("reversed text:",reverse)
        
# output
# enter any text:python
# original text: python
# reversed text: nohtyp

# -----------------------------------------------------------------------------------------------------------------------

# Palindrome String

text=input("enter any text to check wether its palindrome:")
reverse=""
i=len(text)-1
while i>=0:
    reverse=reverse+text[i]
    i-=1
if reverse==text:
    print("its a palindrome string")
else:
    print("not palindrome string")     

# output:
# enter any text to check wether its palindrome:dad
# its a palindrome string

# enter any text to check wether its palindrome:khask
# not palindrome string

# ---------------------------------------------------------------------------------------------------------------------------------------

# first character that occurs only once.

string=input("enter any string:")
i=0
while i<len(string):
    count=0
    j=0
    while j<len(string):
        if string[i]==string[j]:
            count+=1
        j+=1
    if count==1:
        print(string[i])
        break
    i+=1

# output
# enter any string:ddolly
# o

#----------------------------------------------------------------------------

# Find characters that occur more than once.
string=input("enter any string:")
i=0
result=""
while i<len(string):
    j=0
    count=0
    while j<len(string):
        if string[i]==string[j]:
            count+=1
        j+=1
    if count>=2 and string[i] not in result:
        result+=string[i]
        print(string[i])
    i+=1
# enter any string:dollyy
# l
# y

# --------------------------------------------------------------

# Produce a string containing each character only once

string=input("enter any string:")
i=0
result=""
while i<len(string):
    j=0
    count=0
    while j<len(string):
        if string[i]==string[j]:
            count+=1
        j+=1
    if count==1:
        result+=string[i]
    i+=1
print(result)

# ouput
# enter any string:dolly
# doy

# -----------------------------------------------------------------------------

# removing space

string=input("enter any string:")
i=0
result=""
while i<len(string):
    if string[i]!=" ":
        result+=string[i]

    i+=1
print(result)

# output
# enter any string:dolly behera
# dollybehera

# ---------------------------------------------------------------------------------------------------------------
#                                             Text Analyzer.

# Take a sentence from the user.

# Your program should calculate:

# Total characters
# Total characters excluding spaces
# Number of words
# Number of vowels
# Number of consonants
# Number of digits
# Number of spaces
# Number of uppercase letters
# Number of lowercase letters

text=input("enter any text:")
length=len(text)
total_character_excluding_space=""
words=0
vowel=0
consonants=0
digit=0
space=0
upcase=0
lowcase=0
i=0
while i<length:
    if text[i]!=" ":
        if text[i].isnumeric():
            digit+=1
        elif text[i].isalpha():
            words+=1
            if text[i].lower()=='a' or text[i].lower()=='e' or text[i].lower()=='i' or text[i].lower()=='o' or text[i].lower()=='u' :
                vowel+=1
            else:
                consonants+=1
            if text[i].isupper():
                upcase+=1
            else:
                lowcase+=1
        total_character_excluding_space+=text[i]
    else:
        space+=1
    i+=1
print("Total characters:",length)
print("Total characters excluding spaces:",len(total_character_excluding_space))
print("Number of words:",words)
print("Number of vowels:",vowel)
print("Number of consonants:",consonants)
print("Number of digits:",digit)
print("Number of spaces:",space)
print("Number of uppercase letters:",upcase)
print("Number of lowercase letters:",lowcase)

# output:
# enter any text:Dolly Behera 83238
# Total characters: 18
# Total characters excluding spaces: 16
# Number of words: 11
# Number of vowels: 4
# Number of consonants: 7
# Number of digits: 5
# Number of spaces: 2
# Number of uppercase letters: 2
# Number of lowercase letters: 9
