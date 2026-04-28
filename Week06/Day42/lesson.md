<!-- nav -->
[← Day 41](../Day41/lesson.md) | [🏠 Home](../../) | [Day 43 →](../../Week07/Day43/lesson.md)

---
<!-- nav -->

# Day 42 – Project: Bank Account System

## What You're Building
A fully encapsulated bank account system with deposit, withdrawal, transfer, and transaction history — all using OOP principles.

---

## Learning Objectives
- Apply encapsulation with private attributes and `@property`
- Use class-level tracking of all accounts
- Implement a full transaction history log

---

## Project Spec

### Classes:
1. `Transaction` — stores type, amount, and timestamp
2. `BankAccount` — core account with deposit, withdraw, transfer, and history

### Features:
- `deposit(amount)` — add funds
- `withdraw(amount)` — remove funds (with insufficient funds check)
- `transfer(amount, target_account)` — move funds between accounts
- `get_history()` — print all transactions
- `__str__` — shows account summary

### Sample Output:
```
Account [ACC-001] – Alice
Balance: $750.00

Transaction History:
  [2025-01-10 09:00] DEPOSIT    +$1000.00
  [2025-01-10 09:01] WITHDRAW   -$200.00
  [2025-01-10 09:02] TRANSFER   -$50.00 → ACC-002
```

---

## Skills Used
- Classes, `__init__`, `@property`
- Encapsulation (`__balance`)
- Datetime for timestamps
- Lists for history
- f-strings

---

## Starter Code
See `exercises.py` for the full project.

---

<!-- nav -->
[📝 Exercises](exercises.py) | [← Day 41](../Day41/lesson.md) | [Day 43 →](../../Week07/Day43/lesson.md)
<!-- nav -->
