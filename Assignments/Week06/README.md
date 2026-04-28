<!-- assignments-nav -->
[🏠 Home](../../) | [📚 Week 06 Lessons — Object-Oriented Programming](../../Week06/)

---
<!-- assignments-nav -->

# Week 06 Assignments — Object-Oriented Programming

**Days 36–42 · Topics: Classes, Inheritance, Encapsulation, Magic Methods, Class Methods**

---

## Assignments

### Day 36 — Classes & Objects
- Create a `Book` class with title, author, year; add a `summary()` method
- Create a `Temperature` class that stores Celsius and provides `to_fahrenheit()` and `to_kelvin()`
- Create a `Deck` class representing a 52-card deck with `shuffle()` and `deal()` methods

### Day 37 — Constructors & Instance Methods
- Add `__str__` and `__repr__` to your `Book` class
- Create a `Counter` class with `increment()`, `decrement()`, `reset()`, and `value` property
- Create a `Circle` class; add methods for area, circumference, and whether two circles overlap

### Day 38 — Inheritance
- Create `Vehicle → Car`, `Truck`, `Motorcycle` hierarchy
- Override `__str__` in each subclass to include vehicle-specific details
- Add a `Fleet` class that holds multiple vehicles and reports total fuel cost

### Day 39 — Encapsulation & Properties
- Rewrite `BankAccount` with `@property` balance that prevents direct setting
- Add a `@property setter` for `age` in a `Person` class that rejects negative values
- Implement `_validate_email` as a private method in a `User` class

### Day 40 — Magic Methods
- Implement `__add__`, `__sub__`, `__mul__`, and `__eq__` for a `Vector2D` class
- Implement `__len__` and `__contains__` for a `Playlist` class
- Implement `__iter__` for a `Matrix` class that yields rows

### Day 41 — Class & Static Methods
- Add a `@classmethod from_csv_row(row)` factory to your `Student` class
- Add a `@staticmethod validate_score(score)` to `Student`
- Create a `Registry` class that tracks all instances using a class variable

### Day 42 — Project: Bank Account System
- Add multi-currency support with a `@classmethod convert_currency(amount, from_cur, to_cur)`
- Add interest calculation based on account type
- Write unit tests for deposit, withdraw, and transfer

---

## Grading Criteria

| Criteria | Points |
|----------|--------|
| Correct OOP principles applied | 40 |
| Magic methods work as expected | 20 |
| Inheritance hierarchy correct | 20 |
| Tests / edge cases | 20 |
| **Total** | **100** |
