# Factorial number
num = int(input("enter the number :\n"))
result = 1
if num == 0 or num == 1:
    print(1)
else:
    for i in range(1, num+1):
        result = result*i
print("Factorial of", num, "is", result)

