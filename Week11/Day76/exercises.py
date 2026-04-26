# Day 76 – Task Scheduling with `schedule`
# Run: pip install schedule

try:
    import schedule
except ImportError:
    print("Install schedule first: pip install schedule")
    raise SystemExit

import time, datetime


# Exercise 1: Schedule a job every 2 seconds that prints the current time.
# Run it for 6 seconds then cancel.

# Solution:
log = []

def tick():
    now = datetime.datetime.now().strftime("%H:%M:%S")
    log.append(now)
    print(f"Tick: {now}")

job = schedule.every(2).seconds.do(tick)

start = time.time()
while time.time() - start < 6:
    schedule.run_pending()
    time.sleep(0.5)

schedule.cancel_job(job)
print(f"Job ran {len(log)} times.\n")


# Exercise 2: Schedule a one-shot job that runs once and cancels itself.

# Solution:
def one_shot():
    print("One-shot job executed!")
    return schedule.CancelJob

schedule.every(1).seconds.do(one_shot)
for _ in range(3):
    schedule.run_pending()
    time.sleep(0.6)


# Exercise 3: Schedule two jobs — one every 3 seconds, one every 5 seconds.
# Run for 10 seconds and count how many times each fired.

# Solution:
counts = {"3s": 0, "5s": 0}

schedule.every(3).seconds.do(lambda: counts.__setitem__("3s", counts["3s"] + 1))
schedule.every(5).seconds.do(lambda: counts.__setitem__("5s", counts["5s"] + 1))

start = time.time()
while time.time() - start < 10:
    schedule.run_pending()
    time.sleep(0.5)

schedule.clear()
print(f"3s job ran {counts['3s']} times, 5s job ran {counts['5s']} times.")
