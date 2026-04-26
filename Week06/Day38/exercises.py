# Day 38 – Constructors & Magic Methods

# Exercise 1: Create a Point class with __str__, __repr__, and __eq__.

# Solution:
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

p1 = Point(3, 4)
p2 = Point(3, 4)
p3 = Point(1, 2)
print(p1)            # (3, 4)
print(repr(p1))      # Point(x=3, y=4)
print(p1 == p2)      # True
print(p1 == p3)      # False


# Exercise 2: Add __add__ to Point to support p1 + p2.

# Solution:
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v = Vector(1, 2) + Vector(4, 5)
print(v)  # Vector(5, 7)


# Exercise 3: Create a ShoppingCart class with __len__ and __str__.

# Solution:
class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add(self, product, price):
        self.items[product] = price

    def __len__(self):
        return len(self.items)

    def total(self):
        return sum(self.items.values())

    def __str__(self):
        lines = [f"  {k}: ${v:.2f}" for k, v in self.items.items()]
        return "Cart:\n" + "\n".join(lines) + f"\n  TOTAL: ${self.total():.2f}"

cart = ShoppingCart()
cart.add("Python Book", 39.99)
cart.add("USB Hub", 24.99)
cart.add("Coffee", 12.50)
print(cart)
print(f"Items: {len(cart)}")


# Exercise 4: Create a Fraction class that supports __add__ and __str__.

# Solution:
from math import gcd

class Fraction:
    def __init__(self, num, den):
        g = gcd(abs(num), abs(den))
        self.num = num // g
        self.den = den // g

    def __add__(self, other):
        new_num = self.num * other.den + other.num * self.den
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __str__(self):
        return f"{self.num}/{self.den}"

f1 = Fraction(1, 2)
f2 = Fraction(1, 3)
print(f"{f1} + {f2} = {f1 + f2}")   # 1/2 + 1/3 = 5/6
