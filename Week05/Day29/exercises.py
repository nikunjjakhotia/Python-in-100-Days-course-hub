# Day 29 – List Comprehensions

# Exercise 1: Create a list of squares of numbers 1-10 using a comprehension.

# Solution:
squares = [x ** 2 for x in range(1, 11)]
print(squares)


# Exercise 2: Filter a list to keep only strings longer than 4 characters.

# Solution:
words = ["cat", "python", "dog", "elephant", "ox", "code", "hi"]
long_words = [w for w in words if len(w) > 4]
print(long_words)


# Exercise 3: Build a list of (number, square) tuples for 1-8.

# Solution:
pairs = [(x, x**2) for x in range(1, 9)]
print(pairs)


# Exercise 4: Use a dict comprehension to map each word to its length.

# Solution:
sentence = "the quick brown fox jumps over the lazy dog"
word_lengths = {word: len(word) for word in sentence.split()}
print(word_lengths)


# Exercise 5: Flatten a 2D matrix using a nested comprehension.

# Solution:
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for row in matrix for num in row]
print(flat)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
