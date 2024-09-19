from functions import calculator, show_history, log_history

memory_value = 0
decimal_places = 1

def set_decimal_places():
    global decimal_places
    while True:
        try:
            decimal_places = int(input("How many decimal places do you want to display: "))
            print(f"Decimal places set to: {decimal_places}")
            break
        except ValueError:
            print("Incorrect input! Enter an integer.")

def main():
    global memory_value, decimal_places

    while True:
        print("\n--- Calculator ---")
        print("1. New calculation")
        print("2. Show history")
        print("3. Set the number of decimal places")
        print("4. Exit")
        choice = input("Choose option (1-4): ")

        if choice == '1':
            result, first_number, operator, second_number = calculator(decimal_places, memory_value)
            
            if result is not None:
                choice_memory = input('Would you like to store result in memory (MS), add to memory (M+), clear memory (MC), or skip? ').upper()
                match choice_memory:
                    case 'MS':
                        memory_value = result
                        print(f"Stored {result} in memory.")
                    case 'M+':
                        memory_value += result
                        print(f"Added {result} to memory. New memory value: {memory_value}.")
                    case 'MC':
                        memory_value = 0
                        print("Memory cleared.")

                log_history(first_number, operator, second_number, result)
                print(f"Result: {result}")

                if input("Do you want to view history? (y/n): ").strip().lower() == 'y':
                    print(show_history())
            
            if input('Do you want to make another calculation? (y/n): ').lower() != 'y':
                break
        elif choice == '2':
            print(show_history())
        elif choice == '3':
            set_decimal_places()
        elif choice == '4':
            print("Exit.")
            break
        else:
            print("Wrong choice! Try again.")

main()
