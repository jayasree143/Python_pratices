"""
# Write a program that calculates and displays the letter grade

# for a given numerical score (e.g., A, B, C, D, or F)

# based on the following grading scale:

#

# A: 90-100

# B: 80-89

# C: 70-79

# D: 60-69

# F: 0-59
logic:
step1: input is score or mark
       output return string
"""
score = int(input("enter the score:\n"))
grade = 'F'
if 90 <= score <= 100:  # score >= 90 and score <=100
    grade = 'A'
    print(f"The grade is {grade}")
elif 80 <= score <= 89:
    grade = 'B'
    print(f"The grade is {grade}")
elif 70 <= score <= 79:
    grade = 'C'
    print(f"The grade is {grade}")
elif 60 <= score <= 69:
    grade = 'D'
    print(f"The grade is {grade}")
elif 0 <= score <= 59:
    grade = 'F'
    print(f"The grade is {grade}")
else:
    print("The Score is not applicable")


