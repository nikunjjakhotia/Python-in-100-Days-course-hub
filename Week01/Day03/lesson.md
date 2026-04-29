<!-- nav -->
[← Day 02](../Day02/lesson) | [🏠 Home](/Python-in-100-Days-course-hub/) | [Day 04 →](../Day04/lesson)

---
<!-- nav -->

# 📘 Day 03 – Numbers, Strings & Input

Welcome to Day 03! Today we'll explore how Python handles numbers and strings, and how to accept input from users.

---

## 🔢 Numbers in Python
Python supports:

- **Integers** (`int`): Whole numbers
- **Floats** (`float`): Decimal numbers
- **Complex** (`complex`): Numbers with a real and imaginary part (less common)

```python
a = 10       # integer
b = 3.14     # float
```

### 🧮 Basic Arithmetic
```python
print(5 + 3)   # Addition
print(5 - 2)   # Subtraction
print(4 * 2)   # Multiplication
print(10 / 3)  # Division (float result)
print(10 // 3) # Floor division
print(2 ** 3)  # Exponentiation
```

---

## 🔤 Strings Refresher
A string is a sequence of characters. Use single `'` or double `"` quotes.

```python
name = "Nikunj"
print("Hello, " + name)
```

### String Operations
- Concatenation: `"a" + "b"`
- Repetition: `"ha" * 3`
- Length: `len("text")`
- Indexing: `word[0]`
- Slicing: `word[1:4]`

---

## 🎤 Taking User Input
You can get user input using the `input()` function. Input is always treated as a string.

```python
name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello", name)
```

To use numerical input:
```python
age = int(input("Enter your age: "))
```

---

## ✅ Mini Task
Create a program that asks the user for two numbers, adds them, and prints the result.

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum:", a + b)
```

---

<!-- nav -->
[📝 Exercises](https://github.com/nikunjjakhotia/Python-in-100-Days-course-hub/blob/main/Week01/Day03/exercises.py) | [← Day 02](../Day02/lesson) | [Day 04 →](../Day04/lesson)
<!-- nav -->
