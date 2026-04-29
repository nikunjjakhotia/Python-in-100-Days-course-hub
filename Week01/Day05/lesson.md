<!-- nav -->
[← Day 04](../Day04/lesson) | [🏠 Home](/Python-in-100-Days-course-hub/) | [Day 06 →](../Day06/lesson)

---
<!-- nav -->

# 📘 Day 05 – Tuples, Sets, and Dictionaries

Welcome to Day 05! Today, we’ll explore **tuples**, **sets**, and **dictionaries** — three fundamental data structures in Python. Each serves a unique purpose and is used frequently in real-world applications.

---

## 🔗 Tuples
Tuples are **immutable** (unchangeable) sequences.

```python
coordinates = (10, 20)
print(coordinates[0])  # 10
```

- Use when data should not change
- Tuple elements can be accessed by indexing

---

## 🔁 Sets
Sets are **unordered** collections of **unique** items.

```python
fruits = {"apple", "banana", "cherry", "apple"}
print(fruits)  # {'banana', 'cherry', 'apple'}
```

- Removes duplicates automatically
- Useful for membership testing and removing duplicates

### 🔧 Common Set Operations
```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2))      # {1, 2, 3, 4, 5}
print(set1.intersection(set2)) # {3}
```

---

## 📚 Dictionaries
Dictionaries store data as **key-value** pairs.

```python
person = {"name": "Alice", "age": 25}
print(person["name"])  # Alice
```

- Keys must be unique and immutable
- Values can be of any data type

### 🔧 Dictionary Operations
```python
person["city"] = "Montreal"     # Add new key-value pair
print(person.get("age"))        # Get value safely
```

---

<!-- nav -->
[📝 Exercises](https://github.com/nikunjjakhotia/Python-in-100-Days-course-hub/blob/main/Week01/Day05/exercises.py) | [← Day 04](../Day04/lesson) | [Day 06 →](../Day06/lesson)
<!-- nav -->
