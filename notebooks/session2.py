# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.1
#   kernelspec:
#     display_name: Python [conda env:conda_envs-computelab-2025-2]
#     language: python
#     name: conda-env-conda_envs-computelab-2025-2-py
# ---

# %% [markdown]
# # Session 2
# It's python time hehe
#
# **Why** python though ? 🐍
# - free
# - cross–platform
# - easy to learn
# - it’s a general purpose programming language
# - it’s a nice language
# - lots of support for scientific computation/data visualisation
#
# It's time to clean this notebook up
#
# > "Let's get crack-a-lackin" - Marty from Madagscar

# %% [markdown]
# ## Basic Python 1
# *with examples woah*

# %% [markdown]
# ### 1. Scalars
# - **int** an integer, eg a=1
# - **float** a floating point, eg b=1.2 or c=1e-1
# - **bool** can be True or False
# - **NoneType** special object indicating nulls

# %% [markdown]
# ### 2. Operators

# %%
1+1 # Addition

# %%
4-1 # Substraction

# %%
6*7 # Multiplication

# %%
1/2 # Division

# %%
4**5 # Power

# %%
89 % 5 # Modulo (remainder of a division)

# %%
89 // 5 # Floor division (divide and round down to nearest integer)

# %% [markdown]
# ### 3. Variables
# - are dynamic — they spring into existance when you assigna value to them, eg myObject = 1000
# - are weakly typed — the type is inferred from the type of
# the value
# - can change their value during the lifetime of the program
# - can change their type during the lifetime of the program

# %%
a=12

# %%
a

# %%
a*2.5

# %% [markdown]
# ### 4. Introspection
#
# **What** objects do we have and what can they **do** ?

# %%
type(a)

# %%
print(a.__doc__)

# %%
# ?a

# %%
dir(a)

# %% [markdown]
# ## Basic Python 2 
# *(wait there's 2 of them now ? J.K Rowling didn't warn me about this)*

# %% [markdown]
# ### 1.Strings
# A string is an immutable sequence object used to hold textual
# data. They can be written using
# - single quotes 'allows embedded "double quotes"'
# - double quotes "allows embedded 'single quotes'"
# - triple quoted '''three single quotes''' or
# """three double quotes"""
# Triple quoted strings may span multiple lines.

# %%
aString="hello, 'world'" # Double quote with embedded single quotes

# %%
print(aString)

# %%
aString.upper()

# %%
aString.capitalize()

# %%
aString.replace('world','floridians')

# %%
aString.count('hello')

# %%
aString.split()

# %%
aMultiline="""
Hello world! 
It is unfortunately rainy today"""

# %%
print(aMultiline)

# %% [markdown]
# ### 2. Converting Types

# %%
float(1)

# %%
a=1

# %%
b=1.2

# %%
a+b

# %%
c=str(a+b)

# %% [markdown]
# ### 3. String Formats

# %%
aString+aString

# %%
name = "Olivier"
age = 25

# %%
print ("{0} is {1} years old" .format(name,age)) # newer style .format

# %%
print (f"{name} is {age} years old") # very convenient f-strings

# %% [markdown] jp-MarkdownHeadingCollapsed=true
# #### String Templates
# - https://docs.python.org/3/library/string.html
# - Jinja2 templates (very powerful **beware**)

# %% [markdown]
# ### 4. Exercise 1 
# We want to print "The value of pi is 3.142"

# %%
pi=3.141592653589793

# %%
print ("the value of pi is {0:.3f}" .format(pi)) # .format - not sure how to modify decimal paces in this format - solved now

# %%
print (f"The value of pi is {pi:.3f}") # f-string

# %% [markdown]
# *in this case .3f is used to round it to the correct decimal pace*

# %% [markdown] editable=true slideshow={"slide_type": ""}
# ### 5. Containers
#
# Containers are objects that collect a number of objects. There
# are
# - tuples fixed size, immutable
# - lists variable size, mutable
# - dictionaries a mapping from an immutable object to a mutable object
# Other containers are available from the [collections](https://docs.python.org/3/library/collections.html)
# module. You can also write your own.

# %%
aList = [] # Creating list

# %%
aList.append(10) # Append to a list

# %%
len(aList) # Number of items

# %%
aList.append("hello")

# %%
aList.append(True)

# %%
aList[2] = "world" # Retrieve item from list (similar to R, except we start couting from 0 here)

# %%
aList

# %%
len(aList)

# %%
del aList[0] # Deleting elements from a list (not sure how to do it for multiple elements at a time (tried a few stuff didn't work)

# %%
aList

# %%
aList.remove("hello")

# %%
aTupe=(1, "Hello", "World")

# %%
aTupe[0] = "wibble" # won"t work since a tuple has a fixed size, immutable

# %%
numbers=[1,2,3,4,5,6] 

# %%
numbers[-2] # starts counting from the 'end'

# %%
numbers[2:4] # acces range of items

# %%
numbers[1:] # get all starting items starting at index 1

# %%
numbers[:5]# get all items up to index 5 excluding it

# %%
numbers[::-1] # reversing a list

# %%
numbers[0:5:2] # specifying a step count (here it is 2)

# %%
aDict = {} # Creating a dictionary --> mapping from an immutable object to a mutable one

# %% [markdown]
# We can make up our own indices in this case

# %%
aDict['first'] = "world"

# %%
aDict["first"]

# %%
planets = {"earth":1, "jupiter": 317.8, "mars": 0.107}

# %%
planets

# %%
p="jupiter"

# %%
print(f"The mass of planet {p} is {planets[p]} earth masses")

# %% [markdown]
# ## Flow Control

# %% [markdown]
# ### 1. Loops

# %%
for i in range(10): # Sequence of numbers
    print(i)

# %%
for i in range(10): # Hello World ten times woah
    print('Hello, World!')

# %%
aList = ["Moon", "Mars", "Jupiter"] 

# %%
for x in aList: # Visiting each item of a container in turn
    print(x, len(x))

# %%
for x in aList[:2]: # Combining looping with slicing
    print(x, len(x))

# %%
for p in planets: #Testing out different retrievals in dictionaries, here combining planet name and earth masses
    print(p,planets[p])

# %%
for p in planets:
    print(f"The mass of planet {p} is {planets[p]} earth masses")

# %% [markdown]
# ### 2. If-then-else

# %%
p="earth"

# %%
if planets[p] > 1:
    print(f"{p} has a larger mass than the Earth")
elif planets[p] < 1:
    print(f"{p} has a smaller mass than the Earth")
else:
    print(f"{p} has the same mass as the Earth")

# %%
for p in planets:
    if planets[p] > 1:
        print(f"{p} has a larger mass than the Earth")
    elif planets[p] < 1:
        print(f"{p} has a smaller mass than the Earth")
    else:
        print(f"{p} has the same mass as the Earth")

# %% [markdown]
# ### 3. Logical Expressions
# - evalutates to either True or False
# - comparison operators: ==, <, <=, >, >=, !=
# - logical operators: and, or, not
# - membership operators: in, not in
# - identidy opertors: is, is not

# %% [markdown]
# ### 4. While Loops

# %%
for p in planets:  # May have discovered what infinity means in this case
    while planets[p]<1: 
        print(f"{p} has a smaller mass than the Earth")
    break

# %%
i=0 # While loop to write "Hello, World!" ten times
while i<10:
    print(f"Hello, World!")
    i = i+1

# %%
lower = -1
upper = 11 # Creating the range for the exercise
 
while lower <= upper: # Will keep going until lower reaches upper
    if lower % 2 == 0: # This is how to find even numbers
        print(lower)
    lower += 1
