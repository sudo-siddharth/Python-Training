def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "error: Division by zero is not allowed..."

def modulus(a,b):
    try:
        return a%b
    except ZeroDivisionError:
        return "Error: Modulus by zero is not allowed."

def calculator():
    print("=" * 30)
    print("       SIMPLE CALCULATOR       ")
    print("=" * 30)
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("=" * 30)

    try:
        choice = int(input("Enter choice (1/2/3/4/5): "))
        if choice not in [1, 2, 3, 4, 5]:
            print("Invalid choice. Please select a valid operation.")
            return

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        print("=" * 30)
        print("       CALCULATION RESULT      ")
        print("=" * 30)
        if choice == 1:
            print(f"Addition: {num1} + {num2} = {add(num1, num2)}")
        elif choice == 2:
            print(f"Subtraction: {num1} - {num2} = {subtract(num1, num2)}")
        elif choice == 3:
            print(f"Multiplication: {num1} * {num2} = {multiply(num1, num2)}")
        elif choice == 4:
            print(f"Division: {num1} / {num2} = {divide(num1, num2)}")
        elif choice == 5:
            print(f"Modulus: {num1} % {num2} = {modulus(num1, num2)}")
        print("=" * 30)

    except ValueError:
        print("error: invalid input. Please enter numeric values..")

if __name__ == "__main__":
    calculator()