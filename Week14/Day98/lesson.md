<!-- nav -->
[← Day 97](../Day97/lesson.md) | [🏠 Home](../../) | [Day 99 →](../Day99/lesson.md)

---
<!-- nav -->

# Day 98 – Interview Prep: OOP & Design Patterns

## Learning Objectives
- Explain the four pillars of OOP in Python
- Implement common design patterns
- Answer typical OOP interview questions

---

## Four Pillars

### Encapsulation
```python
class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance          # private

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
```

### Inheritance
```python
class Animal:
    def speak(self): raise NotImplementedError

class Dog(Animal):
    def speak(self): return "Woof!"

class Cat(Animal):
    def speak(self): return "Meow!"
```

### Polymorphism
```python
animals = [Dog(), Cat()]
for a in animals:
    print(a.speak())   # each calls its own speak()
```

### Abstraction
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> float: ...

class Circle(Shape):
    def __init__(self, r): self.r = r
    def area(self): return 3.14159 * self.r ** 2
```

---

## Common Patterns

### Singleton (one instance ever)
```python
class Config:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
```

### Factory
```python
def make_shape(kind, **kwargs):
    shapes = {"circle": Circle, "rectangle": Rectangle}
    return shapes[kind](**kwargs)
```

### Observer
```python
class EventEmitter:
    def __init__(self):
        self._listeners = []
    def on(self, fn): self._listeners.append(fn)
    def emit(self, data):
        for fn in self._listeners: fn(data)
```

---

## Key Takeaways
- Be able to give a one-sentence definition of each of the four pillars with a code example
- Singleton and Factory are the most commonly asked patterns in Python interviews
- `ABC` and `@abstractmethod` enforce interfaces in Python

---

## Exercises
See `exercises.py`

---

<!-- nav -->
[📝 Exercises](https://github.com/nikunjjakhotia/Python-in-100-Days-course-hub/blob/main/Week14/Day98/exercises.py) | [🏠 Home](/Python-in-100-Days-course-hub/) | [← Day 97](../Day97/lesson.md) | [Day 99 →](../Day99/lesson.md)
<!-- nav -->
