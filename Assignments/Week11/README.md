# Week 11 Assignments — Automation

**Days 71–77 · Topics: pathlib, shutil, BeautifulSoup, CSV Automation, Email, Scheduling**

---

## Assignments

### Day 71 — File System Automation
- Write a script that creates 10 numbered `.txt` files, then moves them to an `archive/` folder
- Use `pathlib.rglob` to find all Python files in a directory tree and print their sizes
- Write a `backup(src, dst)` function using `shutil.copytree` with a timestamp suffix

### Day 72 — Web Scraping Basics
- Scrape the titles and authors of all quotes on page 1 of `quotes.toscrape.com`
- Extract all external links from the scraped page
- Check `robots.txt` of any site before scraping and respect the rules

### Day 73 — Extracting Structured Data
- Scrape 5 pages of quotes and save to both `quotes.csv` and `quotes.json`
- Calculate the top 3 most quoted authors
- Add a 1-second delay between page requests

### Day 74 — CSV Report Automation
- Read a CSV of 50 sales records; produce a summary report by region and by product
- Write both summaries to separate CSV files
- Add a timestamp to the output filenames

### Day 75 — Email Automation
- Build a function that assembles an HTML email with a table of data
- Add a CSV attachment to the email
- Describe (in a comment) the exact `.env` variables needed and why they must not be committed

### Day 76 — Scheduling
- Schedule a job that appends a timestamp to a log file every 10 seconds; run for 1 minute
- Schedule a second job at a different interval; show both running concurrently
- Use `schedule.CancelJob` to run one job only once

### Day 77 — Project: File Organiser Bot
- Extend with a `--log` flag that writes every move to `moves.log` with a timestamp
- Add `--undo` support that reads the log and reverses the last N moves
- Run against your real Downloads folder in dry-run mode first

---

## Grading Criteria

| Criteria | Points |
|----------|--------|
| Automation works without manual steps | 40 |
| Polite scraping (delays, User-Agent) | 20 |
| File operations safe (dry-run / backups) | 20 |
| Code quality | 20 |
| **Total** | **100** |
