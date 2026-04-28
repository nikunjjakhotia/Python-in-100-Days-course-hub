<!-- nav -->
[← Day 22](../Day22/lesson.md) | [🏠 Home](../../) | [Day 24 →](../Day24/lesson.md)

---
<!-- nav -->

# Day 23 – Custom Exceptions

## Learning Objectives
- Create your own exception classes by extending `Exception`
- Raise exceptions with meaningful messages
- Build domain-specific error hierarchies

---

## Why Custom Exceptions?

Built-in exceptions are generic. Custom exceptions make errors self-documenting:

```python
# Generic — what went wrong?
raise ValueError("bad value")

# Specific — instantly clear
raise InsufficientFundsError("Balance too low for this withdrawal")
```

---

## Creating a Custom Exception

```python
class InsufficientFundsError(Exception):
    """Raised when a bank account has insufficient funds."""
    pass
```

---

## Raising Custom Exceptions

```python
def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(
            f"Cannot withdraw ${amount}. Balance is only ${balance}."
        )
    return balance - amount

try:
    withdraw(100, 150)
except InsufficientFundsError as e:
    print(f"Error: {e}")
```

---

## Custom Exception with Extra Attributes

```python
class AgeError(Exception):
    def __init__(self, age, message="Invalid age"):
        self.age = age
        super().__init__(f"{message}: {age}")

try:
    age = -5
    if age < 0:
        raise AgeError(age, "Age cannot be negative")
except AgeError as e:
    print(e)
```

---

## Exception Hierarchy

```python
class AppError(Exception): pass
class DatabaseError(AppError): pass
class NetworkError(AppError): pass
```

Catching `AppError` catches all subclasses too.

---

## Key Takeaways
- Inherit from `Exception` (not `BaseException`)
- Name exceptions with the `Error` suffix by convention
- Raise early, catch late — let exceptions propagate to where they can be handled

---

## Exercises
See `exercises.py`

---

<!-- nav -->
[📝 Exercises](exercises.py) | [← Day 22](../Day22/lesson.md) | [Day 24 →](../Day24/lesson.md)
<!-- nav -->
