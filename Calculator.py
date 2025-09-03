def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b

num1 = int(input("Enter a num: "))
num2 = int(input("Enter another num: "))
operation = input("Enter your operation: ")

if operation == "add":
    print(add(num1, num2))
elif operation == "subtract":
    print(subtract(num1, num2))
elif operation == "multiply":
    print(multiply(num1, num2))
elif operation == "divide":
    print(divide(num1, num2))
else:
    print("INVALID INPUT")