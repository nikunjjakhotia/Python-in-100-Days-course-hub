# Day 02 – Comments, Variables & Data Types

# Exercise 1: Declare variables of each core data type and print them with their type.

# Solution:
name = "Nikunj"          # str
age = 34                  # int
height = 5.9              # float
is_student = False        # bool

print(name, type(name))
print(age, type(age))
print(height, type(height))
print(is_student, type(is_student))


# Exercise 2: Swap two variables without using a third variable.

# Solution:
a = 10
b = 25
print(f"Before swap: a={a}, b={b}")
a, b = b, a
print(f"After swap:  a={a}, b={b}")


# Exercise 3: Simple arithmetic using typed variables.

# Solution:
x = 8
y = 2
print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)


# Exercise 4: Temperature converter — Celsius to Fahrenheit.
# Formula: fahrenheit = (celsius * 9/5) + 32

# Solution:
celsius = 26
fahrenheit = (celsius * 9 / 5) + 32
print(f"{celsius}°C = {fahrenheit}°F")


# Exercise 5: Use type() to identify the data type of three different values.

# Solution:
print(type(42))           # int
print(type(3.14))         # float
print(type("Python"))     # str
