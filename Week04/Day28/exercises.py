# Day 28 – Project: Log Analyzer
import os

# Create a sample log file
LOG_FILE = "server.log"
with open(LOG_FILE, "w") as f:
    f.write("""2025-01-10 08:23:01 INFO  Server started on port 8080
2025-01-10 08:24:15 ERROR Database connection refused
2025-01-10 08:24:20 WARNING Retrying connection (1/3)
2025-01-10 08:30:00 ERROR Database connection refused
2025-01-10 08:31:05 INFO  User 'admin' logged in
2025-01-10 09:00:00 ERROR Disk quota exceeded
2025-01-10 09:05:00 INFO  Backup job started
2025-01-10 09:10:00 WARNING Memory usage at 80%
2025-01-10 09:15:00 ERROR SSL certificate expired
2025-01-10 09:20:00 INFO  Backup job completed
""")


def analyze_log(filepath):
    counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}
    error_messages = {}
    total = 0

    with open(filepath) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            total += 1
            parts = line.split(None, 3)
            if len(parts) < 4:
                continue
            level = parts[2]
            message = parts[3]

            if level in counts:
                counts[level] += 1

            if level == "ERROR":
                error_messages[message] = error_messages.get(message, 0) + 1

    return total, counts, error_messages


def write_report(total, counts, error_messages, output="report.txt"):
    with open(output, "w") as f:
        f.write("===== LOG ANALYSIS REPORT =====\n")
        f.write(f"Total entries  : {total}\n")
        for level, count in counts.items():
            f.write(f"{level:<15}: {count}\n")
        f.write("\nTop Errors:\n")
        sorted_errors = sorted(error_messages.items(), key=lambda x: x[1])
        for msg, cnt in sorted_errors:
            f.write(f"  {cnt}x - {msg}\n")
        f.write("================================\n")


total, counts, errors = analyze_log(LOG_FILE)
write_report(total, counts, errors)

with open("report.txt") as f:
    print(f.read())

# Cleanup
for fname in [LOG_FILE, "report.txt"]:
    if os.path.exists(fname):
        os.remove(fname)
