num1 = int,float(input("Enter first number: "))
num2 = int,float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

def calculator(operator, num1, num2):
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operator"

    return result

# Example usage:
result = calculator(operator, num1, num2)
print("Result:", result)
