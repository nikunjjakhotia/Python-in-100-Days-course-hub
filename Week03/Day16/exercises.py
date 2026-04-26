# Day 16 – Arguments & Return Values

# Exercise 1: Write add(a, b) that returns the sum.

# Solution:
def add(a, b):
    return a + b

print(add(3, 5))    # 8
print(add(10, -2))  # 8


# Exercise 2: Write a function using *args that returns the product of all arguments.

# Solution:
def multiply_all(*nums):
    result = 1
    for n in nums:
        result *= n
    return result

print(multiply_all(2, 3, 4))    # 24
print(multiply_all(5, 5, 5, 5)) # 625


# Exercise 3: Write get_stats(numbers) that returns (min, max, average).

# Solution:
def get_stats(numbers):
    return min(numbers), max(numbers), sum(numbers) / len(numbers)

lo, hi, avg = get_stats([10, 25, 3, 47, 8])
print(f"Min: {lo}, Max: {hi}, Avg: {avg:.2f}")


# Exercise 4: Use **kwargs to build and return a user profile dictionary.

# Solution:
def build_profile(**kwargs):
    return kwargs

profile = build_profile(name="Alice", age=25, city="Montreal")
print(profile)


# Exercise 5: Write celsius_to_fahrenheit(c) and fahrenheit_to_celsius(f);
# call both and print results.

# Solution:
def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

print(f"25°C = {celsius_to_fahrenheit(25):.1f}°F")
print(f"77°F = {fahrenheit_to_celsius(77):.1f}°C")
