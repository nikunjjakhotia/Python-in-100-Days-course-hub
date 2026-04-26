# Day 09 – Nested Conditions

# Exercise 1: Ticket price system
# Child (<12): $5, Senior (65+): $7, Member adult: $10, Non-member adult: $15

# Solution:
age = int(input("Enter age: "))
is_member = input("Are you a member? (yes/no): ").lower() == "yes"

if age < 12:
    price = 5
elif age >= 65:
    price = 7
else:
    price = 10 if is_member else 15

print(f"Ticket price: ${price}")


# Exercise 2: Bank access — check account active, then check balance

# Solution:
is_active = True
balance = 150

if is_active:
    amount = int(input("Enter withdrawal amount: "))
    if amount <= balance:
        balance -= amount
        print(f"Withdrawn ${amount}. New balance: ${balance}")
    else:
        print("Insufficient funds.")
else:
    print("Account is inactive.")


# Exercise 3: Weather advisor
# Hot (>30) and sunny → beach; Hot and rainy → stay in; Cold (<10) → wear a coat

# Solution:
temp = int(input("Temperature (°C): "))
weather = input("Sunny or Rainy? ").lower()

if temp > 30:
    if weather == "sunny":
        print("Go to the beach!")
    else:
        print("Stay indoors, it's hot and rainy.")
elif temp < 10:
    print("Wear a coat, it's cold!")
else:
    print("Nice weather, enjoy your day.")


# Exercise 4: Nested grade with pass/fail sub-decision

# Solution:
score = int(input("Enter score: "))
passed = score >= 50

if passed:
    if score >= 90:
        print("Distinction!")
    elif score >= 75:
        print("Merit")
    else:
        print("Pass")
else:
    print("Fail — please retake.")


# Exercise 5: Rewrite Exercise 1 using only logical operators (no nesting)

# Solution:
age2 = int(input("Age again: "))
member2 = input("Member? (yes/no): ").lower() == "yes"

if age2 < 12:
    p = 5
elif age2 >= 65:
    p = 7
elif member2:
    p = 10
else:
    p = 15

print(f"Flat logic ticket price: ${p}")
