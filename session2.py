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
# It's python time, we are going to use notebooks
# * basic types
# * flow control

# %%
1+1

# %%
1/2

# %%
a=12

# %%
a

# %%
a*2.5

# %%
aString="hello, 'world'"

# %%
print(aString)

# %%
aMultiline="""
Hello world! 
It is unfortunately rainy today"""

# %%
print(aMultiline)

# %%
aString.capitalize()

# %%
aString.upper()

# %%
float(1)

# %%
a=1

# %%
b=1.2

# %%
a+b

# %%
str(a+b)

# %%
aString+aString

# %%
name = "Olivier"
age = 25

# %%
print ("{0} is {1} years old" .format(name,age))

# %%
print (f"{name} is {age} years old")

# %% [markdown]
# # Exercise 1 
# We want to print "The value of pi is 3.142"

# %%
pi=3.141592653589793

# %%
print ("the value of pi is {0}" .format(pi))

# %%
print (f"The value of pi is {pi:.3f}")

# %% [markdown]
# *in this case .3f is used to round it to the correct decimal pace*

# %%
aList = []

# %%
aList.append(10)

# %%
len(aList)

# %%
aList.append("hello")

# %%
aList.append(True)

# %%
aList[2] = "world"

# %%
aList

# %%
len(aList)

# %%
del aList[0]

# %%
aList

# %%
aList.remove("hello")

# %%
aTupe=(1, "Hello", "World")

# %%
aTupe[0] = "wibble"

# %%
numbers=[1,2,3,4,5,6]

# %%
number [-2]

# %%
numbers[-2]

# %%
numbers[1:]

# %%
# reversing a list
numbers[::-1]

# %%
aDict = {}

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

# %%
for i in range(10): 
    print(i)

# %%
aList = ["Moon", "Mars", "Jupiter"]

# %%
for x in aList:
    print(x, len(x))

# %%
for p in planets:
    print(p)

# %%
for p in planets:
    print(f"The mass of planet {p} is {planets[p]} earth masses")

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
