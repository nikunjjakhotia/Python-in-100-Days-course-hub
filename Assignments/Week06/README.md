<!-- assignments-nav -->
[🏠 Home](../../) | [📚 Week 06 Lessons — Object-Oriented Programming](../../Week06/)

---
<!-- assignments-nav -->

# Week 6 Assignment — Bank Account System

**Days 36–42 · Topics: Classes, Inheritance, Encapsulation, Magic Methods, Class & Static Methods**

Design and build a bank account system with a class hierarchy, encapsulated balances, transaction history, and CSV export.

---

## 🎯 What You'll Build

A Python OOP system modelling a bank with two account types, enforced business rules via properties, and human-readable object representations.

---

## 📋 Requirements

1. Create a `BankAccount` base class with private `_balance` and `_transactions` attributes; expose `balance` as a **read-only property**.
2. Implement `deposit(amount)` and `withdraw(amount)` methods that raise `ValueError` for negative amounts or insufficient funds; each successful operation appends to `_transactions`.
3. Override `__str__` to return a formatted summary (e.g. `"Savings [ACC-001] — Balance: £1,250.00"`) and `__repr__` for unambiguous debugging output.
4. Create a `SavingsAccount(BankAccount)` subclass that adds an `interest_rate` attribute and an `apply_interest()` method — call `super().__init__()` correctly.
5. Create a `CurrentAccount(BankAccount)` subclass with an `overdraft_limit` — `withdraw()` should be overridden to allow the balance to go negative down to that limit.
6. Add a `@classmethod from_dict(cls, data)` that instantiates an account from a dictionary (for loading saved data).
7. Add a `@staticmethod validate_amount(amount)` that raises `TypeError` if the amount is not a positive number — call it at the start of `deposit` and `withdraw`.
8. Export the full transaction history of any account to `transactions.csv` using `csv.DictWriter` with columns: date, type, amount, balance\_after.

---

## 💡 Hints

- `self.__balance` (name-mangled) vs `self._balance` (convention) — use single underscore for protected access.
- `f"£{self._balance:,.2f}"` formats currency with thousand separators.
- `datetime.date.today().isoformat()` gives a sortable date string for transactions.
- Call `BankAccount.__init__(self, ...)` or `super().__init__(...)` inside subclass `__init__`.

---

## 📤 How to Submit

1. Save your solution as `Week06_assignment.py` inside this folder.
2. Demo creating both account types, depositing, withdrawing, applying interest, and exporting.
3. Share a screenshot of the transaction history on LinkedIn with **#Python100Days** and tag [@nikunjjakhotia](https://www.linkedin.com/in/nikunjjakhotia/).

---

## ✅ Marking Criteria

| Criterion | Marks |
|-----------|-------|
| `BankAccount` with encapsulated balance, deposit, withdraw | /10 |
| `__str__` and `__repr__` implemented meaningfully | /10 |
| `SavingsAccount` and `CurrentAccount` inherit correctly | /10 |
| `@classmethod` and `@staticmethod` used appropriately | /10 |
| Transaction history exported to CSV correctly | /10 |
| **Total** | **/50** |
