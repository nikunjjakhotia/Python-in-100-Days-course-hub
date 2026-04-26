# Day 39 – Inheritance

# Exercise 1: Create Animal → Dog and Cat hierarchy; override speak().

# Solution:
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

class Dog(Animal):
    def speak(self):
        return f"{self.name} says: Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says: Meow!"

animals = [Dog("Rex"), Cat("Whiskers"), Animal("Unknown")]
for a in animals:
    print(a.speak())


# Exercise 2: Create Shape → Rectangle and Circle; both implement area().

# Solution:
import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement area()")

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w, self.h = w, h
    def area(self):
        return self.w * self.h

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return round(math.pi * self.r ** 2, 2)

shapes = [Rectangle(4, 6), Circle(5)]
for s in shapes:
    print(f"{type(s).__name__}: area = {s.area()}")


# Exercise 3: Create Employee → Manager; Manager adds team_size and uses super().

# Solution:
class Employee:
    def __init__(self, name, salary):
        self.name   = name
        self.salary = salary

    def __str__(self):
        return f"{self.name} (${self.salary:,})"

class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def __str__(self):
        return f"Manager {self.name} (team={self.team_size}, salary=${self.salary:,})"

print(Employee("Alice", 75000))
print(Manager("Bob", 120000, 8))


# Exercise 4: Verify isinstance() and issubclass() on your hierarchy.

# Solution:
d = Dog("Buddy")
print(isinstance(d, Dog))      # True
print(isinstance(d, Animal))   # True
print(isinstance(d, Cat))      # False
print(issubclass(Dog, Animal)) # True
print(issubclass(Cat, Dog))    # False
