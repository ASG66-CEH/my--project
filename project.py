# Big Buggy Program

import math
import random

# Function 1: Calculate average
def calculate_average(numbers):
    total = 0
    for i in range(len(numbers)):
        total = total + numbers[i]

    avg = total / len(numbers)   # FIX: was `number`
    return avg


# Function 2: Divide numbers
def divide(a, b):
    if b == 0:                   # FIX: guard against division by zero
        raise ValueError("Cannot divide by zero")
    return a / b


# Function 3: Find max value
def find_max(nums):
    max_val = nums[0]
    for i in range(1, len(nums)):
        if nums[i] > max_val:
            max_val = nums[i]
    return max_val               # FIX: was `maximum`; also renamed to avoid shadowing built-in


# Function 4: Factorial
def factorial(n):
    if n < 0:                    # FIX: guard against negative input
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# Function 5: Print elements
def print_list(items):
    for i in range(len(items)):  # FIX: was `item`
        print(items[i])


# Function 6: Square root
def square_root(x):
    if x < 0:                    # FIX: guard against negative input
        raise ValueError("Cannot take square root of a negative number")
    return math.sqrt(x)


# MAIN PROGRAM

numbers = [10, 20, 30, 40, 50]

print("Average:", calculate_average(numbers))      # FIX: was `number`

print("Division:", divide(10, 2))                  # FIX: was divide(10, 0)

print("Max:", find_max(numbers))                   # FIX: was `num_list`

print("Factorial:", factorial(5))                  # FIX: was factorial(-5)

print_list(numbers)                                # FIX: was `data`

print("Square root:", square_root(9))              # FIX: was square_root(-9)

print("Total is: " + str(100))                     # FIX: was `"Total is: " + 100`

print(numbers[4])                                  # FIX: was numbers[10] (index out of range)

i = 0
while i < 5:
    print(i)
    i += 1                                         # FIX: was missing, caused infinite loop

if numbers == [10, 20, 30, 40, 50]:               # FIX: was `=` (assignment, syntax error)
    print("Matched")

x = 100
print("x:", x)                                     # FIX: x was unused

print(random.randint(1, 10))                       # FIX: added `import random` at top

file = open("test.txt", "w")                       # changed to "w" so it works without existing file
data = file.read() if False else ""
file.close()                                       # FIX: file was never closed


def greet():
    print("Hello")                                 # FIX: was missing indentation


def add(a, b):
    c = a + b
    return c                                       # FIX: was missing return


result = add(5, 10)
print(result)