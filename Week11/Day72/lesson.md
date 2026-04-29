<!-- nav -->
[← Day 71](../Day71/lesson.md) | [🏠 Home](../../) | [Day 73 →](../Day73/lesson.md)

---
<!-- nav -->

# Day 72 – Web Scraping with `requests` + `BeautifulSoup`

## Learning Objectives
- Fetch a web page with `requests`
- Parse HTML with `BeautifulSoup`
- Extract text, links, and structured data

---

## Install

```bash
pip install requests beautifulsoup4
```

---

## Fetch & Parse

```python
import requests
from bs4 import BeautifulSoup

r = requests.get("https://quotes.toscrape.com", timeout=10)
r.raise_for_status()
soup = BeautifulSoup(r.text, "html.parser")
```

---

## Finding Elements

```python
# First matching element
title = soup.find("h1")
print(title.text)

# All matching elements
for quote in soup.find_all("span", class_="text"):
    print(quote.text)

# CSS selector
for author in soup.select(".author"):
    print(author.get_text(strip=True))
```

---

## Extracting Attributes

```python
# Get href from all <a> tags
for a in soup.find_all("a"):
    href = a.get("href", "")
    if href.startswith("http"):
        print(href)
```

---

## Navigating the Tree

```python
div = soup.find("div", class_="quote")
text   = div.find("span", class_="text").text
author = div.find("small", class_="author").text
tags   = [t.text for t in div.find_all("a", class_="tag")]
print(text, "—", author, tags)
```

---

## Polite Scraping Rules
1. Check `robots.txt` before scraping
2. Add `time.sleep(1)` between requests
3. Set a `User-Agent` header
4. Never overload a server — scrape slowly

---

## Key Takeaways
- `soup.find()` returns the first match; `.find_all()` returns a list
- `.text` or `.get_text(strip=True)` extracts the visible text
- `.get("attr")` safely reads an HTML attribute

---

## Exercises
See `exercises.py`

---

<!-- nav -->
[📝 Exercises](https://github.com/nikunjjakhotia/Python-in-100-Days-course-hub/blob/main/Week11/Day72/exercises.py) | [🏠 Home](/Python-in-100-Days-course-hub/) | [← Day 71](../Day71/lesson.md) | [Day 73 →](../Day73/lesson.md)
<!-- nav -->
