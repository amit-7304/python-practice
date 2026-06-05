#print in python
print("Hello World")

#comments in python
"""
my name is Amit

"""

#assign multiple variables
fruit = ["apple", "banana", "cherry"]
x, y, z = fruit
print(x)
print(y)
print(z)

#print type
x = 5
y = "john"

print(type(x))

#random number
import random
print(random.randrange(1,10))

#sliceing Strings
a = "hello world"
print(a[2:5])
b = "hello amit"
print(b[-5:-2])

#modify string
a = "hello world"
print(a.upper())
b = "Hello World"
print(b.lower())
c = " Hello World "
print(c.strip())
d = "Hello World"
print(d.replace("H", "J"))
e = "Hello World"
print(e.split(" "))

#string formatting
age = 36
x = f"I am {age} years old"
print(x)

#python Boolean
def myFunction() :
    return True
if myFunction() :
    print("Yes")
else:
    print("No")    