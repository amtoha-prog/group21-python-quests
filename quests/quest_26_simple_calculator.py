# Quest 26: The Simple Calculator
# Author: amtoha-prog | a.mtoha@alustudent.com
# African Leadership University (ALU) — BSE Year 1

# Each arithmetic operation is its own function.
# This keeps logic separated and makes it easy to add new operations later
# without rewriting the decision-making code at the bottom.

def add(a, b):
    # Return the sum of two numbers
    return a + b

def substract(a, b):
    # Return the difference of two numbers (a minus b)
    return a - b

def multiply(a, b):
    # Return the product of two numbers
    return a * b

def divide(a, b):
    # Division by zero is mathematically undefined and would crash the program.
    # We check for it first and return a friendly error message instead.
    if b == 0:
        return "Error: cannot divide by zero"
    return a / b

# Input — ask the user for two numbers.
# float() is used instead of int() so the calculator handles decimals too.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter second number: "))

# Ask which operation to perform.
# The user types a word so it's readable, not a confusing symbol like '+'.
operation = input("Choose an operation(add, subtract, multiply or divide): ")

# Decision making — route to the correct function based on what the user typed.
# Each branch calls the matching function and stores the result.
if operation == "add":
    result = add(num1, num2)
elif operation == "subtract":
    result = substract(num1, num2)
elif operation == "multiply":
    result = multiply(num1, num2)
elif operation == "divide":
    result = divide(num1, num2)
else:
    # If the user typed something unrecognised, set result to an error string
    # rather than crashing or printing nothing.
    result = "Invalid operation"

# Display the final answer using an f-string for clean, readable formatting.
print(f"Result: {result}")
