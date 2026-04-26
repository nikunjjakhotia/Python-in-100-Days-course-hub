# Day 41 – OOP Challenges

# Exercise 1: Implement a Stack class with push, pop, peek, __len__, __str__.

# Solution:
class Stack:
    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)

    def pop(self):
        if not self._data:
            raise IndexError("Pop from empty stack")
        return self._data.pop()

    def peek(self):
        return self._data[-1] if self._data else None

    def __len__(self):
        return len(self._data)

    def __str__(self):
        return f"Stack{self._data}"

s = Stack()
s.push(1); s.push(2); s.push(3)
print(s)            # Stack[1, 2, 3]
print(s.pop())      # 3
print(s.peek())     # 2
print(len(s))       # 2


# Exercise 2: Build a Queue class (FIFO) with enqueue, dequeue, __len__.

# Solution:
from collections import deque

class Queue:
    def __init__(self):
        self._data = deque()

    def enqueue(self, item):
        self._data.append(item)

    def dequeue(self):
        if not self._data:
            raise IndexError("Dequeue from empty queue")
        return self._data.popleft()

    def __len__(self):
        return len(self._data)

    def __str__(self):
        return f"Queue{list(self._data)}"

q = Queue()
q.enqueue("A"); q.enqueue("B"); q.enqueue("C")
print(q)
print(q.dequeue())  # A (FIFO)


# Exercise 3: Build a Book class with checkout() and return_book() using a copies counter.

# Solution:
class Book:
    def __init__(self, title, author, copies=2):
        self.title  = title
        self.author = author
        self._copies = copies

    @property
    def available(self):
        return self._copies > 0

    def checkout(self):
        if not self.available:
            raise ValueError(f"No copies of '{self.title}' available.")
        self._copies -= 1
        return f"Checked out: '{self.title}'"

    def return_book(self):
        self._copies += 1
        return f"Returned: '{self.title}'"

    def __str__(self):
        status = f"{self._copies} copy/copies available"
        return f"'{self.title}' by {self.author} — {status}"

b = Book("Python Crash Course", "Eric Matthes", copies=2)
print(b)
print(b.checkout())
print(b.checkout())
print(b)
print(b.return_book())
print(b)
