<!-- nav -->
[← Day 38](../Day38/lesson.md) | [🏠 Home](../../) | [Day 40 →](../Day40/lesson.md)

---
<!-- nav -->

# Day 39 – Inheritance

## Learning Objectives
- Create child classes that extend parent classes
- Override parent methods in child classes
- Use `super()` to call parent class code

---

## Basic Inheritance

```python
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

d = Dog("Rex")
c = Cat("Whiskers")
print(d.speak())   # Rex says: Woof!
print(c.speak())   # Whiskers says: Meow!
```

---

## Using super()

`super()` calls the parent class method, avoiding code duplication.

```python
class Employee:
    def __init__(self, name, salary):
        self.name   = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)   # reuse parent init
        self.team_size = team_size

    def __str__(self):
        return f"Manager {self.name}, team: {self.team_size}"

m = Manager("Alice", 120000, 8)
print(m)
```

---

## isinstance() and issubclass()

```python
print(isinstance(d, Dog))      # True
print(isinstance(d, Animal))   # True — Dog IS an Animal
print(issubclass(Dog, Animal)) # True
```

---

## Key Takeaways
- Child classes inherit all parent methods and attributes
- Override methods when you need specialised behaviour
- Always call `super().__init__()` when the parent has an `__init__`

---

## Exercises
See `exercises.py`

---

<!-- nav -->
[📝 Exercises](https://github.com/nikunjjakhotia/Python-in-100-Days-course-hub/blob/main/Week06/Day39/exercises.py) | [← Day 38](../Day38/lesson.md) | [Day 40 →](../Day40/lesson.md)
<!-- nav -->
