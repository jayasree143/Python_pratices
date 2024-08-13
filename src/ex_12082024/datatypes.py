"""
1.Numbers:Python supports three types of numbers - int (integer), float
(floating point), and complex (complex numbers).
"""
num = 44 # integer
num1 = 44545.454 # float
# Creating a complex number using complex()
z1 = complex(2, 3)
print(z1)  # Output: (2+3j)
print(num,num1)
print(type(num1))
print(type(num))
"""
2. Strings:
Strings in Python are sequences of characters, used to store textual information. For example:
In this example, spaceship_name is a string representing the name of the spaceship.
"""
name = "Apollo"  # a string
print(name)
"""
3.List
List is ordered collection that can be modified it a mutable object and it enclosed by [] square bracket
we can create the duplicate value also.
"""
a = [1, 2, 3, 4]
print(a)  # it will print the list of a
print(a[0])  # it will print the index of 0 value
print(a[-1])  # it will print tha last index value
for i in a:
    print(i)  # it will print the value one by one
b = [4, 5, 6, 7]
c = [8, 9, 0, 1]
d = b + c
for i in d:
    print(i)
print(len(d)) # it will print the length of d
print(b * 3)
# nested list
c1 = [[1, 2, 3, 4], [6, 7, 7, 8], [5, 7, 8, 9]]
print(c1)
print(c1[0])  # it will print the index of 0 value.
print(c1[0][0])  # it will print the value of nested list of index
c1.append([6,8,9,4])
print(c1)
"""
4.Dictionaries

"""