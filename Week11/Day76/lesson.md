<!-- nav -->
[← Day 75](../Day75/lesson.md) | [🏠 Home](../../) | [Day 77 →](../Day77/lesson.md)

---
<!-- nav -->

# Day 76 – Task Scheduling with `schedule`

## Learning Objectives
- Run Python functions on a recurring schedule
- Use the `schedule` library for human-readable intervals
- Understand how to run background jobs

---

## Install

```bash
pip install schedule
```

---

## Basic Usage

```python
import schedule
import time

def job():
    print("Running job…")

schedule.every(10).seconds.do(job)
schedule.every(5).minutes.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("09:00").do(job)
schedule.every().monday.at("08:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
```

---

## Passing Arguments

```python
def send_report(recipient):
    print(f"Sending report to {recipient}")

schedule.every().day.at("18:00").do(send_report, recipient="boss@company.com")
```

---

## Cancelling a Job

```python
job_ref = schedule.every(5).seconds.do(job)
# later…
schedule.cancel_job(job_ref)
```

---

## Running Once and Stopping

```python
def one_time_task():
    print("Done once.")
    return schedule.CancelJob   # returning this cancels the job after one run

schedule.every(1).seconds.do(one_time_task)
```

---

## Real-World Pattern

```python
import schedule, time, logging

logging.basicConfig(level=logging.INFO)

def backup_database():
    logging.info("Backing up database…")
    # ... backup logic ...

def clean_temp_files():
    logging.info("Cleaning temp files…")

schedule.every().day.at("02:00").do(backup_database)
schedule.every(6).hours.do(clean_temp_files)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(60)
```

---

## Key Takeaways
- `schedule` is simple and readable — great for lightweight recurring tasks
- For production, prefer `cron` (Linux) or Task Scheduler (Windows) for reliability
- Always log job runs so you can audit what happened and when

---

## Exercises
See `exercises.py`

---

<!-- nav -->
[📝 Exercises](https://github.com/nikunjjakhotia/Python-in-100-Days-course-hub/blob/main/Week11/Day76/exercises.py) | [🏠 Home](/Python-in-100-Days-course-hub/) | [← Day 75](../Day75/lesson.md) | [Day 77 →](../Day77/lesson.md)
<!-- nav -->
