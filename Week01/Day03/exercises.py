# Day 03 – Numbers, Strings & User Input

# Exercise 1: Ask the user for two numbers and print all four arithmetic results.

# Solution:
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(f"Addition:       {a + b}")
print(f"Subtraction:    {a - b}")
print(f"Multiplication: {a * b}")
print(f"Division:       {a / b:.2f}")


# Exercise 2: String operations — length, slicing, repetition.

# Solution:
word = "Python"
print(f"Length: {len(word)}")
print(f"First 3 chars: {word[:3]}")
print(f"Reversed: {word[::-1]}")
print(f"Repeated: {word * 3}")


# Exercise 3: Take name and hobby as input, print a formatted sentence.

# Solution:
name = input("Enter your name: ")
hobby = input("Enter your favorite hobby: ")
print(f"Hi {name}! It's great that you love {hobby}.")


# Exercise 4: Tip calculator.
# Ask for bill amount, tip %, and number of people. Print each person's share.

# Solution:
bill = float(input("Total bill: "))
tip_pct = float(input("Tip percentage: "))
people = int(input("Number of people: "))
tip_amount = (bill * tip_pct) / 100
total = bill + tip_amount
per_person = total / people
print(f"Each person pays: ${per_person:.2f}")


# Exercise 5: Convert a string to uppercase, lowercase, and title case.

# Solution:
sentence = input("Enter a sentence: ")
print(sentence.upper())
print(sentence.lower())
print(sentence.title())
