# Day 15 – Defining Functions

# Exercise 1: Write a function greet() that prints "Hello, World!" when called.

# Solution:
def greet():
    print("Hello, World!")

greet()


# Exercise 2: Write greet_user(name) that prints a personalised greeting.

# Solution:
def greet_user(name):
    print(f"Hello, {name}! Welcome to Python.")

greet_user("Nikunj")
greet_user("Alice")


# Exercise 3: Write a function with a default parameter.
# say_hello(name="Stranger") → "Hello, Stranger!" if no argument is given.

# Solution:
def say_hello(name="Stranger"):
    print(f"Hello, {name}!")

say_hello()
say_hello("Bob")


# Exercise 4: Write is_even(n) — prints whether n is even or odd.

# Solution:
def is_even(n):
    if n % 2 == 0:
        print(f"{n} is Even")
    else:
        print(f"{n} is Odd")

is_even(4)
is_even(7)


# Exercise 5: Write a function print_stars(n) that prints n stars on one line.

# Solution:
def print_stars(n):
    print("*" * n)

print_stars(5)
print_stars(10)
