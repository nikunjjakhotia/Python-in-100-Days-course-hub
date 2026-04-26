# Day 21 – Project: Calculator App
import math

def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

def power(a, b): return a ** b

def square_root(a):
    if a < 0:
        return "Error: Cannot take square root of a negative number"
    return math.sqrt(a)

def show_menu():
    print("\n" + "=" * 32)
    print("      PYTHON CALCULATOR")
    print("=" * 32)
    print("1. Add         2. Subtract")
    print("3. Multiply    4. Divide")
    print("5. Power       6. Square Root")
    print("7. Exit")

while True:
    show_menu()
    choice = input("Choose an option (1-7): ").strip()

    if choice == "7":
        print("Goodbye!")
        break

    if choice == "6":
        a = float(input("Enter a number: "))
        result = square_root(a)
        print(f"√{a} = {result}")
        continue

    if choice not in ("1", "2", "3", "4", "5"):
        print("Invalid choice. Please enter 1-7.")
        continue

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    operations = {
        "1": (add, "+"),
        "2": (subtract, "-"),
        "3": (multiply, "×"),
        "4": (divide, "÷"),
        "5": (power, "^"),
    }

    func, symbol = operations[choice]
    result = func(a, b)
    print(f"Result: {a} {symbol} {b} = {result}")
