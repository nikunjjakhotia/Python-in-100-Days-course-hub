<!-- nav -->
[← Day 15](../Day15/lesson.md) | [🏠 Home](../../) | [Day 17 →](../Day17/lesson.md)

---
<!-- nav -->

# Day 16 – Arguments & Return Values

## Learning Objectives
- Use positional, keyword, and `*args` / `**kwargs`
- Return single and multiple values from functions
- Understand how return values enable chaining

---

## Positional vs Keyword Arguments

```python
def describe(name, age, city):
    print(f"{name}, {age}, from {city}")

describe("Alice", 25, "Montreal")           # positional
describe(age=25, name="Alice", city="Montreal")  # keyword
```

---

## *args — Variable Number of Positional Args

```python
def add_all(*nums):
    return sum(nums)

print(add_all(1, 2, 3))        # 6
print(add_all(10, 20, 30, 40)) # 100
```

---

## **kwargs — Variable Number of Keyword Args

```python
def show_profile(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

show_profile(name="Alice", age=25, city="Montreal")
```

---

## Returning Values

```python
def square(n):
    return n ** 2

result = square(5)
print(result)   # 25
```

---

## Returning Multiple Values

```python
def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([3, 1, 9, 2, 7])
print(low, high)   # 1 9
```

---

## Key Takeaways
- `return` sends a value back to the caller and exits the function
- Multiple return values are packed into a tuple automatically
- `*args` collects extra positional args; `**kwargs` collects extra keyword args

---

## Exercises
See `exercises.py`

---

<!-- nav -->
[📝 Exercises](https://github.com/nikunjjakhotia/Python-in-100-Days-course-hub/blob/main/Week03/Day16/exercises.py) | [← Day 15](../Day15/lesson.md) | [Day 17 →](../Day17/lesson.md)
<!-- nav -->
