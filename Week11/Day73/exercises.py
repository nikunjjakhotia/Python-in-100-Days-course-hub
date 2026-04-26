# Day 73 – Parsing & Extracting Structured Data

import requests, time, csv, json, os
from bs4 import BeautifulSoup

BASE = "https://quotes.toscrape.com/page/{}/"


# Exercise 1: Scrape 3 pages of quotes into a list of dicts.

# Solution:
quotes = []
for page in range(1, 4):
    r = requests.get(BASE.format(page), timeout=10)
    soup = BeautifulSoup(r.text, "html.parser")
    for div in soup.select(".quote"):
        quotes.append({
            "text":   div.select_one(".text").get_text(strip=True),
            "author": div.select_one(".author").get_text(strip=True),
            "tags":   ", ".join(t.get_text() for t in div.select(".tag")),
        })
    time.sleep(0.4)

print(f"Total quotes: {len(quotes)}")


# Exercise 2: Save quotes to quotes.csv.

# Solution:
with open("quotes.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["text", "author", "tags"])
    writer.writeheader()
    writer.writerows(quotes)
print("Saved quotes.csv")


# Exercise 3: Save quotes to quotes.json.

# Solution:
with open("quotes.json", "w", encoding="utf-8") as f:
    json.dump(quotes, f, indent=2, ensure_ascii=False)
print("Saved quotes.json")


# Exercise 4: Count how many quotes each author has across all scraped pages.

# Solution:
author_counts = {}
for q in quotes:
    author_counts[q["author"]] = author_counts.get(q["author"], 0) + 1

print("\nTop 5 authors:")
for author, count in sorted(author_counts.items(), key=lambda x: -x[1])[:5]:
    print(f"  {author}: {count}")


# Clean up
for path in ("quotes.csv", "quotes.json"):
    if os.path.exists(path):
        os.remove(path)
