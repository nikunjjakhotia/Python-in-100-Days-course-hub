# Day 20 – Functions: Practice Problems

# Exercise 1: Write is_palindrome(word) — returns True if the word reads the same backwards.

# Solution:
def is_palindrome(word):
    word = word.lower().replace(" ", "")
    return word == word[::-1]

print(is_palindrome("racecar"))  # True
print(is_palindrome("Python"))   # False
print(is_palindrome("A man a plan a canal Panama"))  # True


# Exercise 2: Write caesar_cipher(text, shift) to encrypt a string.

# Solution:
def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord("A") if char.isupper() else ord("a")
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

print(caesar_cipher("Hello, World!", 3))  # Khoor, Zruog!
print(caesar_cipher("Khoor, Zruog!", -3)) # Hello, World!


# Exercise 3: Write word_frequency(sentence) that returns a dict of word counts.

# Solution:
def word_frequency(sentence):
    freq = {}
    for word in sentence.lower().split():
        freq[word] = freq.get(word, 0) + 1
    return freq

print(word_frequency("the cat sat on the mat the cat"))


# Exercise 4: Write flatten(nested_list) that converts [[1,2],[3,4],[5]] → [1,2,3,4,5].

# Solution:
def flatten(nested_list):
    result = []
    for sublist in nested_list:
        for item in sublist:
            result.append(item)
    return result

print(flatten([[1, 2], [3, 4], [5]]))  # [1, 2, 3, 4, 5]


# Exercise 5: Write remove_duplicates(lst) that returns a list with unique elements
# in original order (without using set directly on the whole list).

# Solution:
def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

print(remove_duplicates([3, 1, 4, 1, 5, 9, 2, 6, 5, 3]))
