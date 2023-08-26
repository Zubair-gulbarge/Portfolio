# Hello World:

# print("Hello, World!")

# Addition of Two Numbers:

# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# sum = num1 + num2
# print("Sum:", sum)

# Factorial Calculation:

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)

# num = int(input("Enter a number: "))
# print("Factorial:", factorial(num))


# Fibonacci Series:
# python
# Copy code
# def fibonacci(n):
#     if n <= 0:
#         return []
#     elif n == 1:
#         return [0]
#     elif n == 2:
#         return [0, 1]
#     else:
#         fib_series = [0, 1]
#         for i in range(2, n):
#             next_num = fib_series[-1] + fib_series[-2]
#             fib_series.append(next_num)
#         return fib_series

# count = int(input("Enter the number of terms in Fibonacci series: "))
# print("Fibonacci Series:", fibonacci(count))
# Check Prime Number:
# python
# Copy code
# def is_prime(num):
#     if num <= 1:
#         return False
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False
#     return True

# num = int(input("Enter a number: "))
# if is_prime(num):
#     print(num, "is a prime number.")
# else:
#     print(num, "is not a prime number.")
# Swap Two Variables:
# python
# Copy code
# a = int(input("Enter the value of a: "))
# b = int(input("Enter the value of b: "))
# a, b = b, a
# print("After swapping: a =", a, "b =", b)
# Generate Multiplication Table:
# python
# Copy code
# num = int(input("Enter a number: "))
# for i in range(1, 11):
#     print(num, "x", i, "=", num * i)
# Find Maximum of Three Numbers:
# python
# Copy code
# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# num3 = float(input("Enter the third number: "))
# max_num = max(num1, num2, num3)
# print("Maximum number:", max_num)
# Check Leap Year:
# python
# Copy code
# year = int(input("Enter a year: "))
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(year, "is a leap year.")
# else:
#     print(year, "is not a leap year.")
# Calculate Area of Triangle:
# python
# Copy code
# base = float(input("Enter the base of the triangle: "))
# height = float(input("Enter the height of the triangle: "))
# area = 0.5 * base * height
# print("Area of the triangle:", area)
# Feel free to run and modify these programs to practice your Python skills!
