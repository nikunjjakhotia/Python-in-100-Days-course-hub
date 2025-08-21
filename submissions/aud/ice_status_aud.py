#!/usr/bin/env python3
import argparse
import os
import re
import sys
from datetime import datetime, timedelta

# =============================================================
# AUD Status Parser (Clean Copy - No tzdata dependency)
# =============================================================

# Regex patterns
GOODFILES_RE = re.compile(r"GoodFiles", re.IGNORECASE)
TOTAL_SUB_RE = re.compile(r"Total Prices to be submitted:\s*(\d+)", re.IGNORECASE)
TOTAL_VAL_RE = re.compile(r"Total validated Prices submitted:\s*(\d+)", re.IGNORECASE)
TOTAL_CONTRIB_RE = re.compile(r"Contributed Prices:\s*(\d+)", re.IGNORECASE)
PCT_100_RE   = re.compile(r"\(100%|100\.000%\)")
END_OK_RE    = re.compile(r"Program is ending successfully", re.IGNORECASE)

# Slot definitions in LOCAL Australia time
AUD_SLOTS = {
    "regular": {
        "morning": "10:00",
        "early": "16:00",
        "early2": "16:15",
        "final": "16:30",
    },
    "early_close": {
        "morning": "07:00",
        "early": "12:00",
        "early2": "12:15",
        "final": "12:30",
    }
}

def parse_args():
    p = argparse.ArgumentParser(description="AUD Status Parser")
    p.add_argument("--date", required=True, help="Date in YYYY-MM-DD format")
    p.add_argument("--schedule", choices=["regular", "early_close"], default="regular")
    p.add_argument("--slot", choices=["morning", "early", "early2", "final"], required=True)
    p.add_argument("--verbose", action="store_true")
    return p.parse_args()

def read_log_file(path):
    if not os.path.exists(path):
        return ""
    with open(path, encoding="utf-8", errors="ignore") as f:
        return f.read()

def evaluate_block(blob):
    reasons = []
    good = GOODFILES_RE.search(blob)
    total_sub = TOTAL_SUB_RE.search(blob)
    total_val = TOTAL_VAL_RE.search(blob)
    total_contrib = TOTAL_CONTRIB_RE.search(blob)
    pct100 = PCT_100_RE.search(blob)
    end_ok = END_OK_RE.search(blob)

    if good: reasons.append("GoodFiles present")
    if total_sub: reasons.append(f"Total Submitted={total_sub.group(1)}")
    if total_val: reasons.append(f"Total Validated={total_val.group(1)}")
    if total_contrib: reasons.append(f"Contributed={total_contrib.group(1)}")
    if pct100: reasons.append("100% confirmed")
    if end_ok: reasons.append("Ended successfully")

    # Validation logic
    if good and total_sub and (total_val or total_contrib) and pct100 and end_ok:
        # Compare totals
        sub_val = total_sub.group(1)
        val_ok = (total_val and total_val.group(1) == sub_val)
        contrib_ok = (total_contrib and total_contrib.group(1) == sub_val)
        if val_ok or contrib_ok:
            return "OK", reasons

    return "NOK", reasons

def main():
    args = parse_args()

    # Map slot to human time (for display only)
    slot_time = AUD_SLOTS[args.schedule][args.slot]

    base_dir = f"D:\\Data\\logs\\fixlink\\{args.date}\\ICEDIRECT"
    targets = [
        ("Index", "AUDforUS", "PriceGeneration_AUDforUS_EarlyRun.log"),
        ("SingleName", "AUDforUS", "PriceGeneration_AUDforUS_EarlyRun.log"),
    ]

    print("== AUD Parser ==")
    print(f"Date: {args.date}")
    print(f"Schedule: {args.schedule}, Slot: {args.slot} ({slot_time} local)")

    for area, region, filename in targets:
        path = os.path.join(base_dir, area, region, filename)
        blob = read_log_file(path)
        if not blob:
            print(f"AUD for US - {area:<12} | TBC | file missing: {path}")
            continue

        status, reasons = evaluate_block(blob)
        print(f"AUD for US - {area:<12} | {status:<3} | file={path}")
        if args.verbose:
            for r in reasons:
                print(f"   - {r}")

if __name__ == "__main__":
    sys.exit(main())
