import argparse
import os
import re
import sys
from datetime import datetime, timedelta, date, time
from zoneinfo import ZoneInfo

# ============================ Configuration ============================

# Root directory that contains daily folders (YYYY-MM-DD)
ROOT_DIR = r"D:\Data\logs\fixlink"

# AUD local TZ (handles DST via zoneinfo + the provided --date)
AUD_TZ = ZoneInfo("Australia/Sydney")

# Default server TZ (change with --server-tz if needed)
DEFAULT_SERVER_TZ = "Europe/Paris"

# Areas for AUD
AREAS = ["Index", "SingleName"]  # IndexOption does not apply to AUD

# Filename patterns (with robust fallbacks for some environments)
EARLYRUN_PRIMARY = "PriceGeneration_AUDforUS_EarlyRun.log"
EARLYRUN_FALLBACKS = [
    "PriceGeneration_EURforUS_EarlyRun.log",  # seen in some samples
]
FINALRUN_PRIMARY = "PriceGeneration_AUDforUS_FinalRun.log"

# Local slot definitions (AUD local time)
SLOTS_LOCAL_REGULAR = {
    "morning": time(10, 0),
    "late1":   time(16, 0),
    "late2":   time(16, 15),
    "final":   time(16, 30),
}
SLOTS_LOCAL_EARLYCLOSE = {
    "morning": time(7, 0),
    "late1":   time(12, 0),
    "late2":   time(12, 15),
    "final":   time(12, 30),
}

# Time window (± minutes) to capture a block around the SERVER time
WINDOW_MINUTES = 3

# ============================ Regexes ============================

TS_RE            = re.compile(r"^(\d{4}/\d{2}/\d{2}\s+\d{2}:\d{2}:\d{2})\b")
END_MARKER_RE    = re.compile(r"Program is ending", re.IGNORECASE)

GOODFILES_RE     = re.compile(r"GoodFiles", re.IGNORECASE)
BADFILES_RE      = re.compile(r"BadFiles", re.IGNORECASE)

TOTAL_SUB_RE     = re.compile(r"Total Prices to be submitted:\s*(\d+)", re.IGNORECASE)
TOTAL_VAL_RE     = re.compile(r"Total validated Prices submitted:\s*(\d+)", re.IGNORECASE)
TOTAL_CONTRIB_RE = re.compile(r"Contributed Prices:\s*(\d+)", re.IGNORECASE)

PCT_100_RE       = re.compile(r"\(100(\.\d+)?%\)", re.IGNORECASE)

END_OK_RE        = re.compile(r"Program is ending successfully", re.IGNORECASE)
END_ERR_RE       = re.compile(r"Program is ending with error", re.IGNORECASE)
SKIP_RE          = re.compile(r"Skipping auto submission", re.IGNORECASE)

# ============================ Helpers ============================

def parse_args():
    p = argparse.ArgumentParser(description="AUD ICEDIRECT parser (TZ-aware)")
    p.add_argument("--date", required=True, help="Date folder in YYYY-MM-DD (server daily folder date)")
    p.add_argument("--schedule", required=True, choices=["regular", "earlyclose"], help="Which schedule to use")
    p.add_argument("--slot", required=True, choices=["morning", "late1", "late2", "final"], help="Local slot name")
    p.add_argument("--server-tz", default=DEFAULT_SERVER_TZ, help="Server timezone, e.g. Europe/Paris or Europe/London")
    p.add_argument("--window", type=int, default=WINDOW_MINUTES, help="± minutes window (default 3)")
    p.add_argument("--verbose", action="store_true", help="Verbose output")
    return p.parse_args()

def resolve_date_folder(s: str) -> str:
    try:
        datetime.strptime(s, "%Y-%m-%d")
        return s
    except ValueError:
        raise SystemExit("Invalid --date. Use YYYY-MM-DD")

def local_slot_time(schedule: str, slot_name: str) -> time:
    if schedule == "regular":
        return SLOTS_LOCAL_REGULAR[slot_name]
    return SLOTS_LOCAL_EARLYCLOSE[slot_name]

def local_to_server_time(d_folder: str, local_hm: time, server_tz_name: str) -> time:
    """Convert AUD local time on given date to server time-of-day (HH:MM[:SS])."""
    y, m, d = map(int, d_folder.split("-"))
    local_dt = datetime(y, m, d, local_hm.hour, local_hm.minute, local_hm.second, tzinfo=AUD_TZ)
    server_tz = ZoneInfo(server_tz_name)
    server_dt = local_dt.astimezone(server_tz)
    return server_dt.time()

def area_base_path(date_folder: str, area: str) -> str:
    # AUD lives under AUDforUS for Index & SingleName
    return os.path.join(ROOT_DIR, date_folder, "ICEDIRECT", area, "AUDforUS")

def candidate_paths_for(area: str, slot_name: str, date_folder: str):
    base = area_base_path(date_folder, area)
    if slot_name == "final":
        return [os.path.join(base, FINALRUN_PRIMARY)]
    # Early slots
    cands = [os.path.join(base, EARLYRUN_PRIMARY)]
    for fb in EARLYRUN_FALLBACKS:
        cands.append(os.path.join(base, fb))
    return cands

def read_lines(path: str):
    if not os.path.exists(path):
        return None
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            return f.readlines()
    except Exception:
        return None

def within_window(ts: time, target: time, window_min: int) -> bool:
    tmin = target.hour * 60 + target.minute
    smin = ts.hour * 60 + ts.minute
    diff = abs(smin - tmin)
    diff = min(diff, 24*60 - diff)  # wrap-around safeguard
    return diff <= window_min

def extract_block_around(lines, target_server_time: time, window_min: int):
    """Capture block starting at first timestamp within ±window, until 'Program is ending...'"""
    capturing = False
    block = []
    start_ts_str = None

    for line in lines:
        m = TS_RE.match(line)
        if m:
            ts_str = m.group(1)
            try:
                ts = datetime.strptime(ts_str, "%Y/%m/%d %H:%M:%S").time()
            except ValueError:
                ts = None
            if ts and not capturing and within_window(ts, target_server_time, window_min):
                capturing = True
                start_ts_str = ts_str
                block.append(line)
                continue

        if capturing:
            block.append(line)
            if END_MARKER_RE.search(line):
                break

    return block, start_ts_str

def extract_last_block(lines):
    """For FinalRun: grab the last 'Program is ending...' block."""
    end_idx = None
    for i in range(len(lines)-1, -1, -1):
        if END_MARKER_RE.search(lines[i]):
            end_idx = i
            break
    if end_idx is None:
        return lines[:], None  # fallback: whole file
    # backtrack to the previous timestamp line
    start_idx = 0
    for j in range(end_idx, -1, -1):
        if TS_RE.match(lines[j]):
            start_idx = j
            break
    block = lines[start_idx:end_idx+1]
    m = TS_RE.match(block[0]) if block else None
    return block, (m.group(1) if m else None)

def evaluate_block(block_lines):
    """Return (status, reasons). Auto-detects SingleName vs Index/IndexOption."""
    if not block_lines:
        return "TBC", [f"No lines captured in the time window (±{WINDOW_MINUTES} min)"]

    blob = "\n".join(block_lines)

    # immediate NOK markers
    if END_ERR_RE.search(blob) or SKIP_RE.search(blob) or BADFILES_RE.search(blob):
        return "NOK", ["Error/skip/badfiles marker detected"]

    good          = GOODFILES_RE.search(blob)
    total_sub     = TOTAL_SUB_RE.search(blob)
    total_val     = TOTAL_VAL_RE.search(blob)      # Index/IndexOption
    total_contrib = TOTAL_CONTRIB_RE.search(blob)  # SingleName
    pct100        = PCT_100_RE.search(blob)
    end_ok        = END_OK_RE.search(blob)

    if good and total_sub and pct100 and end_ok:
        sub_val = total_sub.group(1)
        if total_contrib and sub_val == total_contrib.group(1):
            return "OK", ["SingleName: totals match + 100% + successful end"]
        if total_val and sub_val == total_val.group(1):
            return "OK", ["Index/IndexOption: totals match + 100% + successful end"]
        return "NOK", [f"Totals mismatch (submitted={sub_val}, validated={total_val.group(1) if total_val else 'NA'}, contributed={total_contrib.group(1) if total_contrib else 'NA'})"]

    reasons = []
    if not total_sub:
        reasons.append("Missing 'Total Prices to be submitted'")
    if not (total_val or total_contrib):
        reasons.append("No validated/contributed totals found")
    if not good:
        reasons.append("No GoodFiles marker found")
    if not pct100:
        reasons.append("No 100% confirmation")
    if not end_ok:
        reasons.append("No successful end marker")
    return "NOK", reasons

# ============================ Main ============================

def main():
    args = parse_args()
    date_folder = resolve_date_folder(args.date)
    server_tz_name = args.server_tz
    window_min = args.window

    # Map local slot -> server slot (time-of-day) on this date
    local_hm = local_slot_time(args.schedule, args.slot)
    server_hm = local_to_server_time(date_folder, local_hm, server_tz_name)

    print("== AUD Parser (TZ-aware) ==")
    print(f"Date folder: {date_folder}")
    print(f"Schedule: {args.schedule} | Slot: {args.slot}")
    print(f"Local (Australia/Sydney): {local_hm.strftime('%H:%M')}  →  Server ({server_tz_name}): {server_hm.strftime('%H:%M')}")
    print(f"Window: ±{window_min} minutes\n")

    for area in AREAS:
        used_file = None
        lines = None

        # Pick file depending on slot (early vs final) with fallbacks
        for cand in candidate_paths_for(area, args.slot, date_folder):
            lines = read_lines(cand)
            if lines:
                used_file = cand
                break

        if not lines:
            print(f"{'AUD for US - ' + area:28s} | TBC | file not found")
            continue

        if args.slot == "final":
            block, start_ts = extract_last_block(lines)
        else:
            block, start_ts = extract_block_around(lines, server_hm, window_min)

        status, reasons = evaluate_block(block)
        print(f"{'AUD for US - ' + area:28s} | {status:3s} | start={start_ts or 'n/a'} | file={used_file}")
        if args.verbose and reasons:
            for r in reasons:
                print(f"   - {r}")

    print("\nLegend: OK=Green, NOK=Orange/Red (later phase), TBC=Yellow, HOLIDAY=Grey (later).")
    return 0

if __name__ == "__main__":
    sys.exit(main())
