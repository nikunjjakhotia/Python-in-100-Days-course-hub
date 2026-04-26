# Day 06 – Type Casting & String Formatting

# Exercise 1: Take a numeric string from the user, cast to int, and add 10.

# Solution:
num_str = input("Enter a number: ")
result = int(num_str) + 10
print(f"Your number plus 10 is: {result}")


# Exercise 2: Convert float to int and show both values.

# Solution:
price = float(input("Enter a price (e.g. 9.99): "))
truncated = int(price)
print(f"Float: {price}  →  Int: {truncated}")


# Exercise 3: Build a profile sentence using an f-string.

# Solution:
name = input("Your name: ")
age = int(input("Your age: "))
city = input("Your city: ")
print(f"Hi, I'm {name}, {age} years old, living in {city}.")


# Exercise 4: Tax calculator — format total to 2 decimal places.

# Solution:
item_price = float(input("Item price: "))
tax_rate = float(input("Tax rate (%): "))
tax_amount = (item_price * tax_rate) / 100
total = item_price + tax_amount
print(f"Subtotal: ${item_price:.2f}  |  Tax: ${tax_amount:.2f}  |  Total: ${total:.2f}")


# Exercise 5: Cast bool from int — show that 0 is False and any non-zero is True.

# Solution:
print(bool(0))    # False
print(bool(1))    # True
print(bool(-5))   # True
print(bool(""))   # False
print(bool("hi")) # True
