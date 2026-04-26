# Day 44 – Standard Library Highlights

import os, sys, math, random
from datetime import datetime, date, timedelta

# Exercise 1: Print the current working directory and the number of files/folders in it.

# Solution:
cwd = os.getcwd()
print(f"CWD: {cwd}")
print(f"Items: {len(os.listdir(cwd))}")


# Exercise 2: Using `math`, compute the hypotenuse of a right triangle with legs 3 and 4.

# Solution:
print(math.hypot(3, 4))   # 5.0


# Exercise 3: Generate a random password of 8 characters from letters + digits.

# Solution:
import string
chars = string.ascii_letters + string.digits
password = "".join(random.choices(chars, k=8))
print(password)


# Exercise 4: Print today's date, and the date 30 days from now.

# Solution:
today = date.today()
future = today + timedelta(days=30)
print(f"Today   : {today}")
print(f"30 days : {future}")


# Exercise 5: Use `os.path` to check whether a path "data/report.csv" exists,
# and print "Found" or "Not found".

# Solution:
path = os.path.join("data", "report.csv")
print("Found" if os.path.exists(path) else "Not found")


# Exercise 6: Print the Python version and platform using `sys`.

# Solution:
print(sys.version)
print(sys.platform)
