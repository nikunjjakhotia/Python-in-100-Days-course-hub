<!-- nav -->
[← Day 37](../Day37/lesson.md) | [🏠 Home](../../) | [Day 39 →](../Day39/lesson.md)

---
<!-- nav -->

# Day 38 – Constructors & Magic Methods

## Learning Objectives
- Use `__init__`, `__str__`, `__repr__`, `__len__`, and `__eq__`
- Understand Python's data model and operator overloading
- Make classes that behave like built-in types

---

## __str__ vs __repr__

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"      # user-friendly

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"  # developer-friendly

p = Point(3, 4)
print(str(p))   # (3, 4)
print(repr(p))  # Point(x=3, y=4)
```

---

## __len__ and __eq__

```python
class Basket:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def __len__(self):
        return len(self.items)

    def __eq__(self, other):
        return self.items == other.items

b = Basket()
b.add("apple")
print(len(b))  # 1
```

---

## __add__ — Operator Overloading

```python
class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)   # Vector(4, 6)
```

---

## Key Takeaways
- Magic methods (dunder methods) make objects work with built-in operators
- Always define both `__str__` and `__repr__` for production classes
- `__eq__` is needed to compare objects by value, not identity

---

## Exercises
See `exercises.py`

---

<!-- nav -->
[📝 Exercises](https://github.com/nikunjjakhotia/Python-in-100-Days-course-hub/blob/main/Week06/Day38/exercises.py) | [← Day 37](../Day37/lesson.md) | [Day 39 →](../Day39/lesson.md)
<!-- nav -->
