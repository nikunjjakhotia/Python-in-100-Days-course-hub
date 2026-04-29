<!-- nav -->
[← Day 40](../Day40/lesson.md) | [🏠 Home](../../) | [Day 42 →](../Day42/lesson.md)

---
<!-- nav -->

# Day 41 – OOP Challenges

## Learning Objectives
- Apply all OOP concepts in combined challenges
- Design class hierarchies from scratch
- Practise `__dunder__` methods and properties

---

## Challenge 1: Library System

```python
class Book:
    def __init__(self, title, author, copies=1):
        self.title   = title
        self.author  = author
        self._copies = copies

    @property
    def available(self):
        return self._copies > 0

    def checkout(self):
        if self.available:
            self._copies -= 1
        else:
            raise ValueError(f"No copies of '{self.title}' available.")

    def return_book(self):
        self._copies += 1

    def __str__(self):
        status = "Available" if self.available else "Checked Out"
        return f"'{self.title}' by {self.author} [{status}]"
```

---

## Challenge 2: Stack Data Structure

```python
class Stack:
    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)

    def pop(self):
        if not self._data:
            raise IndexError("Stack is empty")
        return self._data.pop()

    def peek(self):
        return self._data[-1]

    def __len__(self):
        return len(self._data)

    def __str__(self):
        return f"Stack{self._data}"
```

---

## Key Takeaways
- Good OOP design means each class has one clear responsibility
- `@property` makes validation transparent to the caller
- Magic methods (`__len__`, `__str__`, `__eq__`) make classes feel native

---

## Exercises
See `exercises.py`

---

<!-- nav -->
[📝 Exercises](https://github.com/nikunjjakhotia/Python-in-100-Days-course-hub/blob/main/Week06/Day41/exercises.py) | [🏠 Home](/Python-in-100-Days-course-hub/) | [← Day 40](../Day40/lesson.md) | [Day 42 →](../Day42/lesson.md)
<!-- nav -->
