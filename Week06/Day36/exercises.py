# Day 36 – Classes & Objects
import math

# Exercise 1: Create a Rectangle class with width and height; add area() and perimeter().

# Solution:
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return f"Rectangle({self.width}x{self.height})"

r = Rectangle(5, 3)
print(r)
print(f"Area: {r.area()}, Perimeter: {r.perimeter()}")


# Exercise 2: Create a Car class with make, model, year; add a describe() method.

# Solution:
class Car:
    def __init__(self, make, model, year):
        self.make  = make
        self.model = model
        self.year  = year

    def describe(self):
        return f"{self.year} {self.make} {self.model}"

car = Car("Toyota", "Camry", 2022)
print(car.describe())


# Exercise 3: Create a Circle class; add area(), circumference(), and __str__.

# Solution:
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(math.pi * self.radius ** 2, 2)

    def circumference(self):
        return round(2 * math.pi * self.radius, 2)

    def __str__(self):
        return f"Circle(radius={self.radius})"

c = Circle(7)
print(c)
print(f"Area: {c.area()}, Circumference: {c.circumference()}")


# Exercise 4: Create a Student class; add a method is_passing() that returns True if score >= 60.

# Solution:
class Student:
    def __init__(self, name, score):
        self.name  = name
        self.score = score

    def is_passing(self):
        return self.score >= 60

    def __str__(self):
        status = "Passing" if self.is_passing() else "Failing"
        return f"{self.name}: {self.score} ({status})"

for name, score in [("Alice", 85), ("Bob", 55), ("Charlie", 62)]:
    print(Student(name, score))
