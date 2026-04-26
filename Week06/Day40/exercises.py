# Day 40 – Polymorphism & Encapsulation

# Exercise 1: Polymorphic payment processing — Cash, Card, and Crypto all have pay().

# Solution:
class PaymentMethod:
    def pay(self, amount):
        raise NotImplementedError

class Cash(PaymentMethod):
    def pay(self, amount):
        return f"Paid ${amount:.2f} in cash."

class Card(PaymentMethod):
    def __init__(self, last4):
        self.last4 = last4
    def pay(self, amount):
        return f"Charged ${amount:.2f} to card ending in {self.last4}."

class Crypto(PaymentMethod):
    def __init__(self, coin):
        self.coin = coin
    def pay(self, amount):
        return f"Paid ${amount:.2f} using {self.coin}."

cart_total = 79.99
for method in [Cash(), Card("4242"), Crypto("BTC")]:
    print(method.pay(cart_total))


# Exercise 2: Use @property to create a Temperature class that validates celsius.

# Solution:
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius   # triggers setter

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError(f"Temperature {value} is below absolute zero.")
        self._celsius = value

    @property
    def fahrenheit(self):
        return (self._celsius * 9 / 5) + 32

t = Temperature(25)
print(f"{t.celsius}°C = {t.fahrenheit}°F")
t.celsius = 100
print(f"{t.celsius}°C = {t.fahrenheit}°F")


# Exercise 3: Build an encapsulated BankAccount with __balance.

# Solution:
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner     = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds.")
        else:
            self.__balance -= amount

    @property
    def balance(self):
        return self.__balance

    def __str__(self):
        return f"{self.owner}'s account: ${self.__balance:.2f}"

acc = BankAccount("Alice", 500)
acc.deposit(200)
acc.withdraw(100)
print(acc)
print(f"Balance: ${acc.balance:.2f}")
