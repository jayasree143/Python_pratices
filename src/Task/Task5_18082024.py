"""
Task 5
Create a program that takes two numbers as input and prints whether the first number is greater than, less than, or equal to the second number
"""
first_number = float(input("Enter the First number:\n"))
second_number = float(input("Enter the second number:\n"))
if first_number > second_number:
    print(f"The first number {first_number} is greater than to second number {second_number} ")
elif first_number < second_number:
    print(f"The first number {first_number} is less than to second number {second_number} ")
else:
    print(f"The first number {first_number} is equal to second number {second_number} ")
