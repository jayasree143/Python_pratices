# Task 4 : Write a Python program to calculate the area of a circle given its radius using the formula  area=π×r^2
# Take pie as 3.14
import math

radius = float(input("enter the value of radius:\n"))
pi_method1 = 3.14
pi_method2 = math.pi
area_circle1 = pi_method1 * radius ** 2
area_circle2 = pi_method2 * radius ** 2
print(f"the value of area circle: {area_circle1}")
print(f"The value of area of circle: {area_circle2}")
print(f"The value of area of circle: {area_circle2:.2f}")
