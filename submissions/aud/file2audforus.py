#!/usr/bin/env python3
import argparse
import os
import re
import sys
from datetime import datetime, timedelta

# ---------------------------------------------------------------------
# Regex patterns
# ---------------------------------------------------------------------
GOODFILES_RE   = re.compile(r"GoodFiles", re.IGNORECASE)
TOTAL_SUB_RE   = re.compile(r"Total Prices to be submitted:\s*(\d+)", re.IGNORECASE)
TOTAL_VAL_RE   = re.compile(r"Total validated Prices submitted:\s*(\d+)", re.IGNORECASE)
TOTAL_CONTRIB_RE = re.compile(r"Contributed Prices:\s*(\d+)", re.IGNORECASE)
PCT_100_RE     = re.compile(r"\(100%", re.IGNORECASE)
END_OK_RE      = re.compile(r"Program is ending successfully", re.IGNORECASE)
END_ERR_RE     = re.compile(r"Program is ending with error", re.IGNORECASE)
SKIP_RE        = re.compile(r"Skipping submission", re.IGNORECASE)
BADFILES_RE    = re.compile(r"BadFiles", re.IGNORECASE)

# ---------------------------------------------------------------------
# Time slot map (server-side times!)
# ---------------------------------------------------------------------
SLOTS = {
    "02:00": datetime.strptime("02:00:00", "%H:%M:%S").time(),
    "16:00": datetime.strptime("16:00:00", "%H:%M:%S").time(),
    "16:15": datetime.strptime("16:15:00", "%H:%M:%S").time(),
    "16:30": datetime.strptime("16:30:00", "%H:%M:%S").time(),
}

# ---------------------------------------------------------------------
# Core evaluation logic
# ---------------------------------------------------------------------
def evaluate_block(blob):
    """Decide if block is OK / NOK / TBC with reasons"""
    good       = GOODFILES_RE.search(blob)
    total_sub  = TOTAL_SUB_RE.search(blob)
    total_val  = TOTAL_VAL_RE.search(blob)
    total_contrib = TOTAL_CONTRIB_RE.search(blob)
    pct100     = PCT_100_RE.search(blob)
    end_ok     = END_OK_RE.search(blob)
    end_err    = END_ERR_RE.search(blob)
    skip       = SKIP_RE.search(blob)
    badfiles   = BADFILES_RE.search(blob)

    # Defaults
    status  = "TBC"
    reasons = []

    # Failures
    if end_err or skip or badfiles:
        return "NOK", ["Error/skip/badfiles marker detected"]

    # OK checks
    if good and total_sub and pct100 and end_ok:
        sub_val = total_sub.group(1)

        # SingleName (has Contributed Prices)
        if total_contrib and sub_val == total_contrib.group(1):
            return "OK", ["SingleName: totals match + 100% + successful end"]

        # Index / IndexOption (has Validated Prices)
        if total_val and sub_val == total_val.group(1):
            return "OK", ["Index/IndexOption: totals match + 100% + successful end"]

        # Mismatch case
        return "NOK", [f"Mismatch between totals (submitted={sub_val}, validated={total_val.group(1) if total_val else 'NA'}, contributed={total_contrib.group(1) if total_contrib else 'NA'})"]

    # Missing required components
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


# ---------------------------------------------------------------------
# Log parsing
# ---------------------------------------------------------------------
def extract_block(filepath, slot_time, window_minutes=3):
    """Extract block of log lines around slot_time ± window_minutes"""
    if not os.path.exists(filepath):
        return None, f"File not found: {filepath}"

    slot_dt = datetime.combine(datetime.today(), slot_time)
    start_dt = slot_dt - timedelta(minutes=window_minutes)
    end_dt   = slot_dt + timedelta(minutes=window_minutes)

    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        lines = f.readlines()

    block_lines = []
    for line in lines:
        if not line.strip():
            continue
        try:
            ts_str = line.split()[0] + " " + line.split()[1]
            ts = datetime.strptime(ts_str, "%Y/%m/%d %H:%M:%S")
        except Exception:
            continue
        if start_dt.time() <= ts.time() <= end_dt.time():
            block_lines.append(line)

    return ("\n".join(block_lines), None) if block_lines else (None, "No lines captured in time window")


# ---------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(description="AUD Log Parser Prototype")
    parser.add_argument("--date", required=True, help="Date in YYYY-MM-DD format")
    parser.add_argument("--slot", required=True, choices=SLOTS.keys(), help="Which slot to check (server time)")
    parser.add_argument("--verbose", action="store_true", help="Verbose output")
    args = parser.parse_args()

    print("== AUD Parser Prototype ==")
    print(f"Date folder: {args.date}")
    print(f"Slot: {args.slot}")

    date_folder = args.date
    slot_time = SLOTS[args.slot]

    # Define log files for AUD
    log_files = {
        "AUD for US - Index":      f"D:\\Data\\logs\\fixlink\\{date_folder}\\ICEDIRECT\\Index\\AUDforUS\\PriceGeneration_AUDforUS_EarlyRun.log",
        "AUD for US - SingleName": f"D:\\Data\\logs\\fixlink\\{date_folder}\\ICEDIRECT\\SingleName\\AUDforUS\\PriceGeneration_AUDforUS_EarlyRun.log",
    }

    for name, path in log_files.items():
        print()
        block, err = extract_block(path, slot_time)
        if err:
            print(f"{name:25} | TBC | {err}")
            continue

        status, reasons = evaluate_block(block)
        print(f"{name:25} | {status:3} | file={path}")
        if args.verbose:
            for r in reasons:
                print(f"   - {r}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
