import math

def log_history(first_operand, operator, second_operand, result):
    with open('./lab_calculator/source/history_log.txt', 'a') as file:
        file.write(f"{first_operand} {operator} {second_operand} = {result}\n")

def show_history():
    try:
        with open('./lab_calculator/source/history_log.txt', 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "History is empty."

def input_number(prompt, memory_value):
    while True:
        user_input = input(prompt).upper()
        if user_input == 'MR':
            print(memory_value)
            return memory_value
        try:
            return float(user_input)
        except ValueError:
            print("Incorrect input! Please enter a valid number or 'MR'.")

def calculator(decimal_places, memory_value):
    first_number = input_number('Input first operand (or MR for memory recall): ', memory_value)

    operator = input("Enter the operator (+, -, *, /, ^, sq, %): ")
    
    while operator not in ['+', '-', '*', '/', '^', 'sq', '%']:
        print("Invalid operator. Available operators: +, -, *, /, ^, sq, %.")
        operator = input("Enter operator (+, -, *, /, ^, sq, %): ")

    second_number = input_number('Input second operand (or MR for memory recall): ', memory_value)

    result = None

    if operator == '+':
        result = round(first_number + second_number, decimal_places)
    elif operator == '-':
        result = round(first_number - second_number, decimal_places)
    elif operator == '*':
        result = round(first_number * second_number, decimal_places)
    elif operator == '/':
        if second_number != 0:
            result = round(first_number / second_number, decimal_places)
        else:
            print("Error: division by zero!")
    elif operator == '^':
        result = round(first_number ** second_number, decimal_places)
    elif operator == 'sq':
        result = round(first_number ** (1 / second_number), decimal_places)
    elif operator == '%':
        if second_number != 0:
            result = round(first_number % second_number, decimal_places)
        else:
            print("Error: division by zero!")

    print(f"{first_number} {operator} {second_number} = {result}")
    return result, first_number, operator, second_number  # Return result and operands
