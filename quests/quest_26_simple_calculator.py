def add(a, b):
    return a + b

def substract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: cannot divide by zero"
    return a / b

#Input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter second number: "))

operation = input("Choose an operation(add, subtract, multiply or divide): ")

#Decision making
if operation == "add":
    result = add(num1, num2)
elif operation == "subtract":
    result = substract(num1, num2)
elif operation == "multiply":
    result = multiply(num1, num2)
elif operation == "divide":
    result = divide(num1, num2)
else:
    result = "Invalid operation"

print(f"Result: {result}")