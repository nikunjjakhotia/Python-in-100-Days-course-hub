# Day 73 – Parsing & Extracting Structured Data

## Learning Objectives
- Scrape multi-page sites with pagination
- Parse tables, lists, and nested HTML
- Export scraped data to CSV and JSON

---

## Multi-Page Scraping

```python
import requests, time
from bs4 import BeautifulSoup

BASE = "https://quotes.toscrape.com/page/{}/"
quotes = []

for page in range(1, 4):
    r = requests.get(BASE.format(page), timeout=10)
    soup = BeautifulSoup(r.text, "html.parser")
    for div in soup.select(".quote"):
        quotes.append({
            "text":   div.select_one(".text").get_text(strip=True),
            "author": div.select_one(".author").get_text(strip=True),
            "tags":   [t.get_text() for t in div.select(".tag")],
        })
    time.sleep(0.5)

print(f"Scraped {len(quotes)} quotes")
```

---

## Parsing an HTML Table

```python
table = soup.find("table")
headers = [th.text.strip() for th in table.find_all("th")]
rows = []
for tr in table.find_all("tr")[1:]:   # skip header row
    cells = [td.text.strip() for td in tr.find_all("td")]
    if cells:
        rows.append(dict(zip(headers, cells)))
```

---

## Exporting to CSV

```python
import csv

with open("quotes.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["text", "author", "tags"])
    writer.writeheader()
    writer.writerows(quotes)
```

---

## Exporting to JSON

```python
import json

with open("quotes.json", "w", encoding="utf-8") as f:
    json.dump(quotes, f, indent=2, ensure_ascii=False)
```

---

## Key Takeaways
- Always add a delay between pages to be a polite scraper
- `soup.select(".class")` and `soup.select_one()` use CSS selectors — more readable for complex HTML
- Export to CSV for spreadsheets, JSON for APIs or further processing

---

## Exercises
See `exercises.py`
