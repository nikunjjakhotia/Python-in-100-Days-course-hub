<!-- nav -->
[← Day 05](../Day05/lesson.md) | [🏠 Home](../../) | [Day 07 →](../Day07/lesson.md)

---
<!-- nav -->

# 📘 Day 06 – Type Casting & String Formatting

Welcome to Day 06! Today, you’ll learn how to **convert data types** and **format strings** in a clean, readable way.

---

## 🔄 Type Casting

Type casting means converting a variable from one type to another.

### 🔧 Examples:
```python
x = "5"
y = int(x)  # y becomes 5 (as an integer)
print(y + 3)  # 8

num = 10
text = str(num)  # "10"
print("Value: " + text)
```

Common casting functions:
- `int()` – to integer
- `float()` – to decimal
- `str()` – to string
- `bool()` – to Boolean

---

## ✨ String Formatting

Use **f-strings** to embed variables into strings.

### 🔧 Example:
```python
name = "Nikunj"
age = 30
print(f"Hello, my name is {name} and I am {age} years old.")
```

This is cleaner than string concatenation:
```python
"Hello, my name is " + name + " and I am " + str(age) + " years old."
```

You can also format numbers:
```python
price = 19.99
print(f"Price: ${price:.2f}")  # Rounds to 2 decimal places
```

---

## ✅ Practice it Yourself

📚 Assignment

🧠 [Exercise](./exercise.md)

➡️ [Next: Course Contents](../CourseContents.md)

⬅️ [Back: Home](../index.md)

---

<!-- nav -->
[📝 Exercises](https://github.com/nikunjjakhotia/Python-in-100-Days-course-hub/blob/main/Week01/Day06/exercises.py) | [← Day 05](../Day05/lesson.md) | [Day 07 →](../Day07/lesson.md)
<!-- nav -->
