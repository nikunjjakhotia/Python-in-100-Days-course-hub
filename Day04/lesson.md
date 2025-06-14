# 📘 Day 04 – Lists & Indexing

Welcome to Day 04! Today we’ll dive into **lists** — a versatile and commonly used data structure in Python — and learn how to access elements using **indexing**.

---

## 📚 What is a List?
A list is an ordered collection of items (elements), which can be of any data type.

```python
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = ["hello", 42, 3.14, True]
```

---

## 🔢 Accessing Elements with Indexing
Python lists are **zero-indexed**, meaning the first element is at position `0`.

```python
fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # apple
print(fruits[1])  # banana
print(fruits[-1]) # cherry (last element)
```

---

## 🔁 Slicing Lists
You can access a subset of elements using **slicing**:

```python
numbers = [10, 20, 30, 40, 50]
print(numbers[1:4])  # [20, 30, 40]
print(numbers[:3])   # [10, 20, 30]
print(numbers[3:])   # [40, 50]
```

---

## 🛠️ Common List Operations

- `len(list)` – Number of items
- `list.append(item)` – Add item to end
- `list.insert(i, item)` – Add at specific index
- `list.remove(item)` – Remove item
- `list.pop(i)` – Remove and return item
- `list.sort()` – Sort items

```python
colors = ["red", "green", "blue"]
colors.append("yellow")
print(colors)
```

---

## ✅ Practice it Yourself

📚 Assignment

🧠 [Exercise](./exercise.md)

➡️ [Next: Course Contents](../CourseContents.md)

⬅️ [Back: Home](../index.md)
