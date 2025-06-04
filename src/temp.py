def calculator ():
    def display_menu():
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

    display_menu()
        try:
            num = float(input(prompt))
            return num
        except ValueError:
            print("Invalid input. Please enter a number.")
    while True:
        display_menu()
        choice = input("Enter choice (1-5): ")

        if choice == '1':
            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")
            print(f"{num1} + {num2} = {num1 + num2}")

        elif choice == '2':
            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")
            print(f"{num1} - {num2} = {num1 - num2}")

        elif choice == '3':
            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")
            print(f"{num1} * {num2} = {num1 * num2}")

        elif choice == '4':
            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")
            if num2 != 0:
                print(f"{num1} / {num2} = {num1 / num2}")
            else:
                print("Error! Division by zero.")

        elif choice == '5':
            print("Exiting the calculator. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
#         elif choice == '7':
#             num = get_number("Enter a number to calculate its factorial: ")
#             result = factorial(num)               