import numpy as np

def add(x, y):
    """Addition function"""
    return x + y

def subtract(x, y):
    """Subtraction function"""
    return x - y

def multiply(x, y):
    """Multiplication function"""
    return x * y

def divide(x, y):
    """Division function"""
    if y == 0:
        return "Error: Division by zero!"
    return x / y

def power(x, y):
    """Power function"""
    return x ** y

def square_root(x):
    """Square root function using numpy"""
    if x < 0:
        return "Error: Square root of negative number!"
    return np.sqrt(x)

def factorial(x):
    """Factorial function"""
    if x < 0:
        return "Error: Factorial of negative number!"
    if x == 0 or x == 1:
        return 1
    result = 1
    for i in range(2, int(x) + 1):
        result *= i
    return result

def display_menu():
    """Display calculator menu"""
    print("\n" + "="*40)
    print("         PYTHON CALCULATOR")
    print("="*40)
    print("Select operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (^)")
    print("6. Square Root (√)")
    print("7. Factorial (!)")
    print("8. Exit")
    print("="*40)

def get_number(prompt):
    """Get a valid number from user input"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def calculator():
    """Main calculator function"""
    print("Welcome to the Python Calculator!")
    
    while True:
        display_menu()
        
        try:
            choice = input("Enter your choice (1-8): ").strip()
            
            if choice == '8':
                print("Thank you for using the calculator! Goodbye!")
                break
            
            if choice in ['1', '2', '3', '4', '5']:
                num1 = get_number("Enter first number: ")
                num2 = get_number("Enter second number: ")
                
                if choice == '1':
                    result = add(num1, num2)
                    print(f"\n{num1} + {num2} = {result}")
                
                elif choice == '2':
                    result = subtract(num1, num2)
                    print(f"\n{num1} - {num2} = {result}")
                
                elif choice == '3':
                    result = multiply(num1, num2)
                    print(f"\n{num1} × {num2} = {result}")
                
                elif choice == '4':
                    result = divide(num1, num2)
                    if isinstance(result, str):
                        print(f"\n{result}")
                    else:
                        print(f"\n{num1} ÷ {num2} = {result}")
                
                elif choice == '5':
                    result = power(num1, num2)
                    print(f"\n{num1} ^ {num2} = {result}")
            
            elif choice == '6':
                num = get_number("Enter number for square root: ")
                result = square_root(num)
                if isinstance(result, str):
                    print(f"\n{result}")
                else:
                    print(f"\n√{num} = {result}")
            
            elif choice == '7':
                num = get_number("Enter number for factorial: ")
                if num != int(num):
                    print("\nError: Factorial requires a whole number!")
                else:
                    result = factorial(int(num))
                    if isinstance(result, str):
                        print(f"\n{result}")
                    else:
                        print(f"\n{int(num)}! = {result}")
            
            else:
                print("Invalid choice! Please select a number between 1-8.")
        
        except KeyboardInterrupt:
            print("\n\nCalculator interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"\nAn error occurred: {e}")
        
        # Ask if user wants to continue
        continue_calc = input("\nPress Enter to continue or 'q' to quit: ").strip().lower()
        if continue_calc == 'q':
            print("Thank you for using the calculator! Goodbye!")
            break

if __name__ == "__main__":
    calculator()
