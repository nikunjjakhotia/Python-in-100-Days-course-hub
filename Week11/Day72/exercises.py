# Day 72 – Web Scraping with requests + BeautifulSoup

import requests, time
from bs4 import BeautifulSoup

BASE_URL = "https://quotes.toscrape.com"


# Exercise 1: Fetch the homepage and print the page title.

# Solution:
r = requests.get(BASE_URL, timeout=10)
r.raise_for_status()
soup = BeautifulSoup(r.text, "html.parser")
print("Title:", soup.find("title").text.strip())


# Exercise 2: Extract all quote texts from the first page.

# Solution:
quotes = [span.get_text(strip=True) for span in soup.select("span.text")]
print(f"\nFound {len(quotes)} quotes:")
for q in quotes[:3]:
    print(" ", q[:80])


# Exercise 3: Extract all unique authors from the first page.

# Solution:
authors = set(small.get_text(strip=True) for small in soup.select("small.author"))
print("\nAuthors:", sorted(authors))


# Exercise 4: Extract all tag links (href) from the first page.

# Solution:
tags = set()
for a in soup.select("a.tag"):
    tags.add(a.get("href", ""))
print("\nTag links (first 5):", sorted(tags)[:5])


# Exercise 5: Scrape two pages and count total quotes collected.

# Solution:
all_quotes = []
for page in range(1, 3):
    time.sleep(0.5)
    r = requests.get(f"{BASE_URL}/page/{page}/", timeout=10)
    s = BeautifulSoup(r.text, "html.parser")
    for div in s.select(".quote"):
        all_quotes.append({
            "text":   div.select_one(".text").get_text(strip=True),
            "author": div.select_one(".author").get_text(strip=True),
        })

print(f"\nTotal quotes scraped (2 pages): {len(all_quotes)}")
