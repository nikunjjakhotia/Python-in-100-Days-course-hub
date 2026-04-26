# Day 43 – Intro to Modules

# Exercise 1: Import the `math` module and print the square root of 144 and the value of pi.

# Solution:
import math
print(math.sqrt(144))   # 12.0
print(math.pi)


# Exercise 2: Use `from math import` to import only `factorial` and `gcd`, then print factorial(6) and gcd(48, 18).

# Solution:
from math import factorial, gcd
print(factorial(6))    # 720
print(gcd(48, 18))     # 6


# Exercise 3: Import `random` as `rnd` and print three random integers between 1 and 100.

# Solution:
import random as rnd
for _ in range(3):
    print(rnd.randint(1, 100))


# Exercise 4: Write a small module-style file below.
# Define a function `circle_area(r)` and a constant `PI = 3.14159`.
# Use the __name__ guard to print "Running directly" only when executed directly.

# Solution:
PI = 3.14159

def circle_area(r):
    return PI * r ** 2

if __name__ == "__main__":
    print("Running directly")
    print(circle_area(5))


# Exercise 5: Import `datetime` and print today's date in the format YYYY-MM-DD.

# Solution:
from datetime import date
print(date.today().strftime("%Y-%m-%d"))
