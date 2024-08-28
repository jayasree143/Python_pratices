# using for loop Fibonacci series
num = int(input("enter the number:\n"))
a = 0
b = 1
for i in range(num):
    print(a)
    a, b = b, a + b
print(f"The Fibonacci series of given number is {a}")

