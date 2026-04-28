<!-- nav -->
[← Day 35](../../Week05/Day35/lesson.md) | [🏠 Home](../../) | [Day 37 →](../Day37/lesson.md)

---
<!-- nav -->

# Day 36 – Classes & Objects

## Learning Objectives
- Define a class and create objects (instances)
- Understand what `self` means
- Add attributes and methods to a class

---

## What Is a Class?

A class is a blueprint. An object is a specific instance built from that blueprint.

```python
class Dog:
    def bark(self):
        print("Woof!")

my_dog = Dog()   # create an instance
my_dog.bark()    # Woof!
```

---

## The `__init__` Constructor

`__init__` runs automatically when an object is created.

```python
class Person:
    def __init__(self, name, age):
        self.name = name   # instance attribute
        self.age  = age

alice = Person("Alice", 25)
print(alice.name)  # Alice
```

---

## Instance Methods

Methods are functions defined inside a class. `self` always refers to the current object.

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        import math
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"Circle(r={self.radius})"

c = Circle(5)
print(c.area())   # 78.54...
print(c)          # Circle(r=5)
```

---

## Key Takeaways
- `self` is a reference to the current object — always the first parameter of any method
- `__init__` is the constructor — it sets up initial state
- Attributes are data; methods are behaviour

---

## Exercises
See `exercises.py`

---

<!-- nav -->
[📝 Exercises](exercises.py) | [← Day 35](../../Week05/Day35/lesson.md) | [Day 37 →](../Day37/lesson.md)
<!-- nav -->
