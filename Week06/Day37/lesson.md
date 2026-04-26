# Day 37 – Instance vs Class Variables

## Learning Objectives
- Distinguish instance variables (per object) from class variables (shared)
- Use class variables for counters and shared constants
- Understand class methods and static methods

---

## Instance Variables

Defined with `self.` — each object gets its own copy.

```python
class Dog:
    def __init__(self, name):
        self.name = name   # each Dog has its own name

d1 = Dog("Rex")
d2 = Dog("Buddy")
print(d1.name, d2.name)  # Rex Buddy
```

---

## Class Variables

Defined at the class level — shared by all instances.

```python
class Dog:
    species = "Canis lupus familiaris"  # class variable
    count = 0

    def __init__(self, name):
        self.name = name
        Dog.count += 1

d1 = Dog("Rex")
d2 = Dog("Buddy")
print(Dog.count)   # 2
print(Dog.species) # shared
```

---

## Class Methods & Static Methods

```python
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @classmethod
    def from_fahrenheit(cls, f):
        return cls((f - 32) * 5 / 9)

    @staticmethod
    def is_freezing(celsius):
        return celsius <= 0

t = Temperature.from_fahrenheit(212)
print(t.celsius)             # 100.0
print(Temperature.is_freezing(-5))  # True
```

---

## Key Takeaways
- Class variables are dangerous if mutable (e.g., a list) — changes affect all instances
- `@classmethod` receives the class (`cls`) as first arg — good for alternate constructors
- `@staticmethod` receives neither `self` nor `cls` — just a namespaced function

---

## Exercises
See `exercises.py`
