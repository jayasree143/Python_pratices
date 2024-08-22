"""
Task #7
Leap Year Checker:
Create a program that determines whether a given year is a leap year. A leap year is divisible by 4, but not by 100 unless
it is also divisible by 400. Use an if-else statement to make this determination.
"""
num = int(input("Enter the number for checking the leap year:\n"))
if num == 0:
    print(f"The Given number is not leap year")
elif (num % 4 == 0) and (num % 100 != 0):
    print(f"The Given number is leap year")
elif (num % 100 == 0) and (num % 400 == 0):
    print(f"The Given number is leap year")
else:
    print(f"The Given number is not leap year")
