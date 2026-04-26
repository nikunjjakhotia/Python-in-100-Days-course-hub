# Day 42 – Project: Bank Account System
from datetime import datetime

class Transaction:
    def __init__(self, t_type, amount, note=""):
        self.t_type    = t_type
        self.amount    = amount
        self.note      = note
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        sign = "+" if self.t_type in ("DEPOSIT",) else "-"
        note = f" {self.note}" if self.note else ""
        return f"  [{self.timestamp}] {self.t_type:<10} {sign}${abs(self.amount):.2f}{note}"


class BankAccount:
    _next_id = 1

    def __init__(self, owner, initial_balance=0):
        self.owner       = owner
        self.account_id  = f"ACC-{BankAccount._next_id:03d}"
        BankAccount._next_id += 1
        self.__balance   = initial_balance
        self.__history   = []
        if initial_balance > 0:
            self.__history.append(Transaction("DEPOSIT", initial_balance, "(opening balance)"))

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.__balance += amount
        self.__history.append(Transaction("DEPOSIT", amount))
        return self

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.__balance:
            raise ValueError(f"Insufficient funds. Balance: ${self.__balance:.2f}")
        self.__balance -= amount
        self.__history.append(Transaction("WITHDRAW", amount))
        return self

    def transfer(self, amount, target):
        self.withdraw(amount)
        target.deposit(amount)
        self.__history[-1] = Transaction("TRANSFER", amount, f"→ {target.account_id}")
        return self

    def get_history(self):
        print(f"\nTransaction History for {self.account_id} ({self.owner}):")
        for t in self.__history:
            print(t)

    def __str__(self):
        return f"Account [{self.account_id}] – {self.owner}\nBalance: ${self.__balance:.2f}"


# Demo
alice = BankAccount("Alice", 1000)
bob   = BankAccount("Bob",   500)

alice.deposit(500).withdraw(200)
alice.transfer(150, bob)

print(alice)
alice.get_history()

print("\n" + str(bob))
bob.get_history()
