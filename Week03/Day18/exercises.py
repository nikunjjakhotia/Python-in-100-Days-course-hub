# Day 18 – Recursion

# Exercise 1: Write a recursive countdown(n) that prints n down to 1, then "Go!".

# Solution:
def countdown(n):
    if n <= 0:
        print("Go!")
        return
    print(n)
    countdown(n - 1)

countdown(5)


# Exercise 2: Write recursive factorial(n).

# Solution:
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(f"5! = {factorial(5)}")   # 120
print(f"10! = {factorial(10)}") # 3628800


# Exercise 3: Write recursive fibonacci(n) and print the first 10 terms.

# Solution:
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print("Fibonacci:", [fibonacci(i) for i in range(10)])


# Exercise 4: Write recursive sum_list(lst) that sums a list without using sum().

# Solution:
def sum_list(lst):
    if not lst:
        return 0
    return lst[0] + sum_list(lst[1:])

print(f"Sum: {sum_list([1, 2, 3, 4, 5])}")  # 15


# Exercise 5: Write recursive power(base, exp) that computes base^exp.

# Solution:
def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)

print(f"2^10 = {power(2, 10)}")  # 1024
print(f"3^4  = {power(3, 4)}")   # 81
