# Certainly! Here are some Python interview questions along with practice sets for each:

# **1. What is Python? What are its key features?**
#    - Python is a high-level, interpreted programming language known for its simplicity and readability.
#    - Key features include dynamic typing, automatic memory management, extensive standard libraries, and support for multiple programming paradigms (procedural, object-oriented, functional).

# **2. What is the difference between a list and a tuple in Python?**
#    - Lists are mutable (can be modified), while tuples are immutable (cannot be modified after creation).
#    - Lists are defined with square brackets `[ ]`, and tuples with parentheses `( )`.

# **3. How do you handle exceptions in Python?**
#    - Python uses try-except blocks to handle exceptions.
   
#    ```python
#    try:
#        # Code that might raise an exception
#    except ExceptionType:
#        # Code to handle the exception
#    ```

# **4. Explain the difference between `range` and `xrange` in Python 2.7.**
#    - In Python 2.7, `range` generates a list, while `xrange` generates an xrange object, which is more memory-efficient for large ranges.

# **5. What is a lambda function?**
#    - A lambda function is an anonymous, small, and inline function that can have any number of arguments, but can only have one expression.

# **6. Explain list comprehension in Python.**
#    - List comprehension is a concise way to create lists by applying an expression to each element in a sequence.
   
#    ```python
#    squares = [x**2 for x in range(10)]
#    ```

# **7. What is the purpose of the `__init__` method in Python classes?**
#    - The `__init__` method is a constructor that gets called when an object is created from a class. It initializes the object's attributes.

# **8. Explain the Global Interpreter Lock (GIL) in Python.**
#    - GIL is a mutex that protects access to Python objects, preventing multiple threads from executing Python bytecodes at once. This can limit the concurrency of Python programs.

# **9. How can you open and read a file in Python?**
#    - You can use the `open()` function to open a file and the `.read()` method to read its contents.
   
#    ```python
#    with open('file.txt', 'r') as file:
#        content = file.read()
#    ```

# **10. Write a Python program to reverse a string.**
   
#    ```python
#    def reverse_string(input_str):
#        return input_str[::-1]
#    ```

# **Practice Sets:**

# 1. **FizzBuzz Problem:**
#    Write a Python program that prints numbers from 1 to 100. For multiples of 3, print "Fizz" instead of the number, and for multiples of 5, print "Buzz". For numbers that are multiples of both 3 and 5, print "FizzBuzz".

# 2. **Palindrome Checker:**
#    Write a Python program to check if a given string is a palindrome (reads the same backward as forward).

# 3. **Factorial Calculation:**
#    Write a Python program to calculate the factorial of a given number using both iterative and recursive methods.

# 4. **Prime Number Generator:**
#    Write a Python program to generate a list of prime numbers up to a given limit.

# 5. **Dictionary Manipulation:**
#    Given a dictionary with student names and their scores, write a Python program to find and print the student with the highest score.

# 6. **Anagram Checker:**
#    Write a Python function to check if two given strings are anagrams of each other (contain the same characters in a different order).

# Remember to practice these questions to improve your Python programming skills and be well-prepared for your interview.

# solution for fizzbuzz problem
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

# Solution for palindrome problem

def is_palindrome(s):
    s = s.lower()  # Convert the string to lowercase
    s = s.replace(" ", "")  # Remove spaces from the string
    return s == s[::-1]  # Compare the string with its reverse

input_string = input("Enter a string: ")

if is_palindrome(input_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
# the above code is not working properly getting stuck in the terminal;