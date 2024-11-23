while True:
    try:
        operand = float(input("Number 1: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

while True:
    try:
        operand2 = float(input("Number 2: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

while True:
    sign = input("Sign (+, -, *, /): ")
    if sign in ["+", "-", "*", "/"]:
        break
    else:
        print("Invalid sign. Please choose one of +, -, *, /.")

# Perform the operation
if sign == "+":
    result = operand + operand2
elif sign == "-":
    result = operand - operand2
elif sign == "*":
    result = operand * operand2
elif sign == "/":
    if operand2 != 0:
        result = operand / operand2
    else:
        print("Error: Division by zero is not allowed.")
        result = None  

# Print the result
if result is not None:
    print(f"Result: {operand} {sign} {operand2} = {result}")
