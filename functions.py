import math

def log_history(first_operand, operator, second_operand, result):
    with open('./source/history_log.txt', 'a') as file:
        file.write(f"{first_operand} {operator} {second_operand} = {result}\n")

def show_history():
    try:
        with open('./source/history_log.txt', 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "History is empty."

def input_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Incorrect input! Please enter a number.")

def calculator(decimal_places):
    first_number = input_number("Enter the first number: ")
    operator = input("Enter the operator (+, -, *, /, ^, sq, %): ")
    
    while operator not in ['+', '-', '*', '/', '^', 'sq', '%']:
        print("Invalid operator. Available operators: +, -, *, /, ^, sq, %.")
        operator = input("Enter operator (+, -, *, /, ^, sq, %): ")

    second_number = input_number("Enter the second number: ")
    result = None  # Initialize result

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
    print(first_number, operator, second_number, "=", result)
    return result, first_number, operator, second_number  # Return result and operands
