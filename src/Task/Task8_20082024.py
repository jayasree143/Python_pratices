"""
 Triangle Classifier:
 Write a program that classifies a triangle based on its side lengths. Given
  three input values representing the lengths of the sides, determine if the
  triangle is equilateral (all sides are equal), isosceles (exactly two sides are equal),
  or scalene (no sides are equal). Use an if-else statement to classify the triangle.

"""
len_1 = int(input("Enter the side of the length:\n"))
len_2 = int(input("Enter the side of the length:\n"))
len_3 = int(input("Enter the side of the length:\n"))
if len_1 == len_2 == len_3:
    print("All sides are equal, its equilateral triangle")
elif (len_1 == len_2) or (len_2 == len_3) or (len_3 == len_1):
    print("Two side are equal its isosceles triangle")
else:
    print("no sides are equal its scalene triangle ")
