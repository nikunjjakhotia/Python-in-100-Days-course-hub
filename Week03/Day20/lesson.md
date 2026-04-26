# Day 20 – Functions: Practice Problems

## Learning Objectives
- Apply all function concepts from Week 3 in combined challenges
- Write clean, well-named functions that solve real problems
- Refactor procedural code into functions

---

## Challenge 1: Is Palindrome?

```python
def is_palindrome(word):
    word = word.lower().replace(" ", "")
    return word == word[::-1]

print(is_palindrome("racecar"))  # True
print(is_palindrome("Python"))   # False
```

---

## Challenge 2: Caesar Cipher

```python
def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord("A") if char.isupper() else ord("a")
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

print(caesar_cipher("Hello", 3))  # Khoor
```

---

## Challenge 3: Word Frequency Counter

```python
def word_frequency(sentence):
    words = sentence.lower().split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq

print(word_frequency("the cat sat on the mat the cat"))
```

---

## Key Takeaways
- Break complex logic into small helper functions
- Functions should be testable in isolation
- Good function names reduce the need for comments

---

## Exercises
See `exercises.py`
