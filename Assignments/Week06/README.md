<!-- assignments-nav -->
[🏠 Home](../../) | [📚 Week 06 Lessons — Object-Oriented Programming](../../Week06/)

---
<!-- assignments-nav -->

# Week 06 Assignment: Build an OOP Inventory System

**Days 36–42 · Topics: Classes, Inheritance, Encapsulation, Magic Methods, Class & Static Methods**

Using the OOP concepts from Days 36–42, build a product inventory tracker with a class hierarchy, encapsulated properties, and CSV import/export.

## What to Build
- A `Product` base class with `name`, `price` (validated via `@property`), and `category`; override `__str__` and `__repr__`
- `ElectronicsProduct` and `FoodProduct` subclasses that add category-specific fields (e.g. warranty months, expiry date)
- An `Inventory` class that implements `__len__`, `__contains__`, and `__iter__` to support natural Python idioms
- A `@classmethod from_csv(path)` to import products and a `to_csv(path)` instance method to export them
- A `@staticmethod validate_price(price)` that raises `ValueError` for negative or non-numeric values
