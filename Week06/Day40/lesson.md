<!-- nav -->
[← Day 39](../Day39/lesson.md) | [🏠 Home](../../) | [Day 41 →](../Day41/lesson.md)

---
<!-- nav -->

# Day 40 – Polymorphism & Encapsulation

## Learning Objectives
- Use polymorphism to write flexible, type-agnostic code
- Encapsulate data with private attributes and properties
- Use `@property` for controlled attribute access

---

## Polymorphism

One interface, many implementations. Code that calls `.speak()` doesn't care whether it's a Dog or Cat.

```python
def make_noise(animal):
    print(animal.speak())   # works for any Animal subclass

make_noise(Dog("Rex"))
make_noise(Cat("Whiskers"))
```

---

## Encapsulation — Private Attributes

Prefix with `_` (convention) or `__` (name-mangled, harder to access).

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # private

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
```

---

## @property — Pythonic Getters/Setters

```python
class Person:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value

p = Person(25)
p.age = 30       # uses setter
print(p.age)     # 30 — uses getter
```

---

## Key Takeaways
- Single `_` = convention "don't touch directly"; `__` = name-mangled
- Use `@property` instead of explicit `get_x()` / `set_x()` methods
- Polymorphism enables writing code that works with any compatible class

---

## Exercises
See `exercises.py`

---

<!-- nav -->
[📝 Exercises](exercises.py) | [← Day 39](../Day39/lesson.md) | [Day 41 →](../Day41/lesson.md)
<!-- nav -->
