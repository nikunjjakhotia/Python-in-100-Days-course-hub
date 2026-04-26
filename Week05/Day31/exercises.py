# Day 31 – Sets & Operations

# Exercise 1: Remove duplicates from a list using a set (preserve order).

# Solution:
raw = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
seen = set()
unique = [x for x in raw if not (x in seen or seen.add(x))]
print("No duplicates:", unique)


# Exercise 2: Find students who passed both Math and Science.

# Solution:
math_pass = {"Alice", "Bob", "Charlie", "Diana"}
science_pass = {"Bob", "Charlie", "Eve", "Frank"}
both = math_pass & science_pass
print("Passed both:", both)
print("Passed only Math:", math_pass - science_pass)
print("Passed at least one:", math_pass | science_pass)


# Exercise 3: Check if a user input is a valid command (membership test).

# Solution:
valid_commands = {"start", "stop", "restart", "status", "help"}
cmd = input("Enter command: ").lower()
if cmd in valid_commands:
    print(f"Executing: {cmd}")
else:
    print(f"Unknown command. Valid: {sorted(valid_commands)}")


# Exercise 4: Find words that appear in one sentence but not the other.

# Solution:
s1 = set("the quick brown fox jumps over the lazy dog".split())
s2 = set("the slow grey fox walks under the old tree".split())
only_in_s1 = s1 - s2
only_in_s2 = s2 - s1
print("Only in S1:", only_in_s1)
print("Only in S2:", only_in_s2)


# Exercise 5: Use frozenset as a dictionary key.

# Solution:
graph = {
    frozenset({"A", "B"}): 10,
    frozenset({"B", "C"}): 7,
    frozenset({"A", "C"}): 15,
}
for edge, weight in graph.items():
    nodes = " - ".join(sorted(edge))
    print(f"{nodes}: {weight}")
