# Big Buggy Program

import math

# Function 1: Calculate average
def calculate_average(numbers):
    total = 0
    for i in range(len(numbers)):
        total = total + numbers[i]
    
    avg = total / len(number)   # BUG: wrong variable name
    return avg


# Function 2: Divide numbers
def divide(a, b):
    return a / b   # BUG: no zero check


# Function 3: Find max value
def find_max(nums):
    max = nums[0]
    for i in range(1, len(nums)):
        if nums[i] > max:
            max = nums[i]
    return maximum   # BUG: wrong variable name


# Function 4: Factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# BUG: no check for negative numbers


# Function 5: Print elements
def print_list(items):
    for i in range(len(item)):   # BUG: wrong variable
        print(items[i])


# Function 6: Square root
def square_root(x):
    return math.sqrt(x)

# BUG: no check for negative input


# MAIN PROGRAM

numbers = [10, 20, 30, 40, 50]

# BUG: wrong function call
print("Average:", calculate_average(number))

# BUG: division by zero
print("Division:", divide(10, 0))

# BUG: undefined variable
print("Max:", find_max(num_list))

# BUG: negative factorial
print("Factorial:", factorial(-5))

# BUG: wrong variable passed
print_list(data)

# BUG: invalid sqrt
print("Square root:", square_root(-9))

# BUG: type error
print("Total is: " + 100)

# BUG: index error
print(numbers[10])

# BUG: infinite loop
i = 0
while i < 5:
    print(i)
# missing increment → infinite loop

# BUG: wrong condition
if numbers = [10, 20, 30]:   # syntax error
    print("Matched")

# BUG: unused variable
x = 100

# BUG: wrong import usage
print(random.randint(1, 10))

# BUG: file not closed
file = open("test.txt", "r")
data = file.read()

# BUG: indentation error
def greet():
print("Hello")

# BUG: missing return
def add(a, b):
    c = a + b

result = add(5, 10)
print(result)
