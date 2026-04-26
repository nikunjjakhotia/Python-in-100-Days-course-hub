# Day 22 – try / except / finally

# Exercise 1: Safe integer input — keep asking until a valid integer is entered.

# Solution:
while True:
    try:
        num = int(input("Enter an integer: "))
        break
    except ValueError:
        print("Invalid input. Please enter a whole number.")
print(f"You entered: {num}")


# Exercise 2: Safe division — handle ZeroDivisionError.

# Solution:
try:
    a = float(input("Numerator: "))
    b = float(input("Denominator: "))
    result = a / b
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Please enter numeric values.")
else:
    print(f"{a} / {b} = {result:.4f}")


# Exercise 3: List index access — handle IndexError.

# Solution:
fruits = ["apple", "banana", "cherry"]
try:
    index = int(input(f"Enter an index (0-{len(fruits)-1}): "))
    print(fruits[index])
except IndexError:
    print(f"Error: Index out of range. List has {len(fruits)} items.")
except ValueError:
    print("Error: Please enter a number.")


# Exercise 4: Dictionary key lookup — handle KeyError.

# Solution:
config = {"host": "localhost", "port": 5432, "db": "myapp"}
try:
    key = input("Enter a config key: ")
    print(f"{key} = {config[key]}")
except KeyError:
    print(f"Key '{key}' not found. Available: {list(config.keys())}")


# Exercise 5: Use finally to simulate a resource cleanup message.

# Solution:
print("\nSimulating file read...")
try:
    content = open("nonexistent_file.txt").read()
except FileNotFoundError:
    print("File not found.")
finally:
    print("Cleanup: Done attempting file operation.")
