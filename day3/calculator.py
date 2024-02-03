while True:
    for _ in range(2):  
        expression = input("Enter a mathematical expression (or 'exit' to quit): ")

        if expression.lower() == 'exit':
            print("Calculator exiting. Goodbye!")
            break  # Exit the for loop

        parts = expression.split()
        if len(parts) != 3:
            print("Error: Invalid expression format. Please enter a valid expression.")
            continue

        operand1, operator, operand2 = parts

        if not operand1.isdigit() or not operand2.isdigit():
            print("Error: Invalid operands. Please enter valid numbers.")
            continue

        if operator == '+':
            result = int(operand1) + int(operand2)
        elif operator == '-':
            result = int(operand1) - int(operand2)
        elif operator == '*':
            result = int(operand1) * int(operand2)
        elif operator == '/':
            if int(operand2) != 0:
                result = int(operand1) / int(operand2)
            else:
                print("Error: Division by zero. Please enter a valid expression.")
                continue
        else:
            print("Error: Invalid operator. Please enter a valid operator (+, -, *, /).")
            continue

        print("Result:", result)

    user_input = input("Do you want to continue? (yes/no): ")
    if user_input.lower() != 'yes':
        print("Calculator exiting. Goodbye!")
        break  
