# Day 30 – Advanced Dictionaries
from collections import defaultdict, Counter

# Exercise 1: Count word frequency using defaultdict(int).

# Solution:
text = "to be or not to be that is the question to be"
word_freq = defaultdict(int)
for word in text.split():
    word_freq[word] += 1
for word, count in sorted(word_freq.items(), key=lambda x: -x[1]):
    print(f"{word}: {count}")


# Exercise 2: Use Counter to find the 3 most common characters in a string.

# Solution:
sample = "programming in python is pretty powerful"
char_count = Counter(sample.replace(" ", ""))
print("\nTop 3 chars:", char_count.most_common(3))


# Exercise 3: Merge two config dicts; user settings override defaults.

# Solution:
defaults = {"theme": "dark", "language": "en", "timeout": 30}
user = {"theme": "light", "timeout": 60}
config = {**defaults, **user}
print("\nMerged config:", config)


# Exercise 4: Invert a dictionary (swap keys and values).

# Solution:
original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}
print("Inverted:", inverted)


# Exercise 5: Aggregate student scores by subject using defaultdict(list).

# Solution:
records = [
    ("Alice", "Math", 95), ("Bob", "Math", 88),
    ("Alice", "Science", 92), ("Bob", "Science", 79),
    ("Charlie", "Math", 76), ("Charlie", "Science", 84),
]
by_subject = defaultdict(list)
for name, subject, score in records:
    by_subject[subject].append((name, score))

for subject, scores in by_subject.items():
    avg = sum(s for _, s in scores) / len(scores)
    print(f"{subject}: avg={avg:.1f}, scores={scores}")
