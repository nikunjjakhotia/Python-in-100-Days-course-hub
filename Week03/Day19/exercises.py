# Day 19 – Lambda Functions

# Exercise 1: Write a lambda that doubles a number. Call it with 5 and 12.

# Solution:
double = lambda x: x * 2
print(double(5))   # 10
print(double(12))  # 24


# Exercise 2: Use map() with a lambda to square every number in a list.

# Solution:
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)   # [1, 4, 9, 16, 25]


# Exercise 3: Use filter() with a lambda to keep only strings longer than 4 chars.

# Solution:
words = ["cat", "elephant", "dog", "python", "ox", "hippo"]
long_words = list(filter(lambda w: len(w) > 4, words))
print(long_words)  # ['elephant', 'python', 'hippo']


# Exercise 4: Sort a list of tuples (name, score) by score descending using sorted().

# Solution:
students = [("Alice", 88), ("Bob", 95), ("Charlie", 72), ("Diana", 99)]
ranked = sorted(students, key=lambda s: s[1], reverse=True)
for rank, (name, score) in enumerate(ranked, start=1):
    print(f"{rank}. {name}: {score}")


# Exercise 5: Use map() + lambda to convert a list of Celsius temps to Fahrenheit.

# Solution:
celsius_list = [0, 20, 25, 37, 100]
fahrenheit_list = list(map(lambda c: round((c * 9 / 5) + 32, 1), celsius_list))
print(fahrenheit_list)
