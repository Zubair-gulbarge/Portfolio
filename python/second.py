# Hello World:

# print("Hello, World!")

# Addition of Two Numbers:

# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# sum = num1 + num2
# print("Sum:", sum)

# Factorial Calculation:

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter a number: "))
print("Factorial:", factorial(num))
