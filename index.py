"""
Python Calculator
A simple command-line calculator for basic arithmetic operations.
"""


def add(x, y):
    """Add two numbers and return the result."""
    return x + y


def sub(x, y):
    """Subtract y from x and return the result."""
    return x - y


def mul(x, y):
    """Multiply two numbers and return the result."""
    return x * y


def div(x, y):
    """
    Divide x by y and return the result.
    Raises ZeroDivisionError if y is zero.
    """
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
    return x / y

def get_number(prompt):
    """
    Get a valid number from user input.
    Returns a float or None if input is invalid.
    """
    try:
        return float(input(prompt))
    except ValueError:
        print("Error: Please enter a valid number.")
        return None


def main():
    """Main function to run the calculator."""
    print("=" * 40)
    print("Welcome to Python Calculator")
    print("=" * 40)
    
    while True:
        print("\nSelect Operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        
        choice = input("\nEnter choice (1/2/3/4/5): ").strip()
        
        if choice == '5':
            print("Thank you for using Python Calculator!")
            break
        
        if choice not in ('1', '2', '3', '4'):
            print("Invalid Input! Please select a valid operation.")
            continue
        
        # Get numbers from user
        num1 = get_number("Enter first number: ")
        if num1 is None:
            continue
        
        num2 = get_number("Enter second number: ")
        if num2 is None:
            continue
        
        # Perform calculation based on choice
        try:
            if choice == '1':
                result = add(num1, num2)
                print(f"\n{num1} + {num2} = {result}")
            
            elif choice == '2':
                result = sub(num1, num2)
                print(f"\n{num1} - {num2} = {result}")
            
            elif choice == '3':
                result = mul(num1, num2)
                print(f"\n{num1} * {num2} = {result}")
            
            elif choice == '4':
                result = div(num1, num2)
                print(f"\n{num1} / {num2} = {result}")
        
        except ZeroDivisionError as e:
            print(f"\nError: {e}")
        except Exception as e:
            print(f"\nAn unexpected error occurred: {e}")


if __name__ == "__main__":
    main()            