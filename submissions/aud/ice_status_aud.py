# ice_status_aud.py
# Prototype: AUD-only parser for ICEDIRECT logs
# Python 3.11+
#
# Usage examples:
#   D:\apps\python\64\3.11.6\python.exe ice_status_aud.py --date 2025-08-20 --slot 10:00
#   D:\apps\python\64\3.11.6\python.exe ice_status_aud.py --date today --slot 16:00
#   D:\apps\python\64\3.11.6\python.exe ice_status_aud.py --date today --slot 16:30 --verbose
#
# Notes:
# - Default status is TBC for each area until a qualifying block is parsed.
# - For 16:30 (Final), we only inspect FinalRun log.
# - For Early slots (10:00, 16:00, 16:15), we inspect EarlyRun log.
# - Window == ±3 minutes around the target slot time (London time).

import argparse
import datetime as dt
import os
import re
import sys
from typing import List, Tuple, Optional

# ---------- Config ----------

WINDOW_MINUTES = 3  # ± window around scheduled time
ROOT_DIR = r"D:\Data\logs\fixlink"  # daily folder beneath this
REGION = "AUD"  # this prototype is AUD-only
AREAS = ["Index", "SingleName"]  # AUD areas

# Some environments show different EarlyRun filename patterns.
# We'll try both, in this order.
EARLYRUN_CANDIDATES = [
    "PriceGeneration_{region}forUS_EarlyRun.log",  # expected pattern (AUDforUS, SGDforUS, etc.)
    "PriceGeneration_EURforUS_EarlyRun.log",       # fallback seen in sample
]

FINALRUN_NAME = "PriceGeneration_{region}forUS_FinalRun.log"

# Timestamp at start of each log line, e.g. 2025/08/20 11:00:17
TS_RE = re.compile(r"^(\d{4}/\d{2}/\d{2}\s+\d{2}:\d{2}:\d{2})\b")

# End-of-block marker
END_MARKER_RE = re.compile(r"Program is ending", re.IGNORECASE)

# Success/NOK heuristics (based on user rules)
GOODFILES_RE = re.compile(r"GoodFiles[\\/].*?\.xml", re.IGNORECASE)
BADFILES_RE  = re.compile(r"BadFiles[\\/].*?\.xml", re.IGNORECASE)
TOTAL_SUB_RE = re.compile(r"Total Prices to be submitted:\s*(\d+)", re.IGNORECASE)
TOTAL_VAL_RE = re.compile(r"Total validated Prices submitted:\s*(\d+)", re.IGNORECASE)
PCT_100_RE   = re.compile(r"\(100%\)")
ERROR_RE     = re.compile(r"\bERROR\b", re.IGNORECASE)
SKIP_RE      = re.compile(r"Skipping auto submission", re.IGNORECASE)
END_OK_RE    = re.compile(r"Program is ending successfully", re.IGNORECASE)
END_ERR_RE   = re.compile(r"Program is ending with error", re.IGNORECASE)


def parse_args():
    p = argparse.ArgumentParser(description="AUD-only ICEDIRECT log parser (prototype)")
    p.add_argument("--date", default="today",
                   help="Date folder in YYYY-MM-DD or 'today' (default). Example: 2025-08-20")
    p.add_argument("--slot", required=True,
                   choices=["10:00", "16:00", "16:15", "16:30"],
                   help="Scheduled slot time (London time). Use '16:30' for FinalRun.")
    p.add_argument("--root", default=ROOT_DIR, help="Root directory containing daily folders")
    p.add_argument("--verbose", action="store_true", help="Verbose output")
    return p.parse_args()


def resolve_date_folder(s: str) -> str:
    if s.lower() == "today":
        # Today in server local time (assumed London). Adjust if needed.
        return dt.date.today().strftime("%Y-%m-%d")
    # basic validation
    try:
        dt.datetime.strptime(s, "%Y-%m-%d")
    except ValueError:
        raise SystemExit("Invalid --date. Use YYYY-MM-DD or 'today'.")
    return s


def make_paths_for_area(date_folder: str, area: str, slot: str) -> List[str]:
    """
    Build candidate log file paths for the given area and slot.
    Early slots (10:00/16:00/16:15) use EarlyRun logs.
    Final slot (16:30) uses FinalRun log.
    """
    base = os.path.join(ROOT_DIR, date_folder, "ICEDIRECT", area, f"{REGION}forUS")
    paths = []

    if slot == "16:30":
        fname = FINALRUN_NAME.format(region=REGION)
        paths.append(os.path.join(base, fname))
    else:
        for cand in EARLYRUN_CANDIDATES:
            fname = cand.format(region=REGION)
            paths.append(os.path.join(base, fname))

    return paths


def _hm_to_time(hm: str) -> dt.time:
    return dt.datetime.strptime(hm, "%H:%M").time()


def _within_window(ts: dt.time, target: dt.time, window_min: int) -> bool:
    """
    Compare times-of-day within ±window_min, ignoring date.
    Handles wrap-around by comparing absolute minute difference in both directions.
    """
    tmin = target.hour * 60 + target.minute
    smin = ts.hour * 60 + ts.minute
    diff = abs(smin - tmin)
    diff = min(diff, 24*60 - diff)  # wrap around midnight
    return diff <= window_min


def extract_block(lines: List[str], target_hm: str, window_min: int) -> Tuple[List[str], Optional[str]]:
    """
    From full log lines, capture the block that starts at the first timestamp that falls
    within the ±window_min around target_hm. Capture until 'Program is ending...' marker.
    Returns (block_lines, starting_timestamp_string_or_None).
    """
    target_t = _hm_to_time(target_hm)
    capturing = False
    block: List[str] = []
    start_ts: Optional[str] = None

    for line in lines:
        m = TS_RE.match(line)
        if m:
            ts_str = m.group(1)
            try:
                ts = dt.datetime.strptime(ts_str, "%Y/%m/%d %H:%M:%S")
            except ValueError:
                ts = None
            if ts and not capturing:
                if _within_window(ts.time(), target_t, window_min):
                    capturing = True
                    start_ts = ts_str
                    block.append(line)
                    continue

        if capturing:
            block.append(line)
            if END_MARKER_RE.search(line):
                break

    return block, start_ts


def evaluate_block(block_lines: List[str], is_final_slot: bool) -> Tuple[str, List[str]]:
    """
    Return (status, reasons)
      status ∈ { 'OK', 'NOK', 'TBC' }
    """
    if not block_lines:
        return "TBC", ["No lines captured in the time window (±%d min)" % WINDOW_MINUTES]

    blob = "\\n".join(block_lines)

    # Immediate NOK signals
    if END_ERR_RE.search(blob) or ERROR_RE.search(blob) or SKIP_RE.search(blob) or BADFILES_RE.search(blob):
        return "NOK", ["Found error/skip/badfiles marker"]

    # Check success conditions
    good = bool(GOODFILES_RE.search(blob))
    total_sub = TOTAL_SUB_RE.search(blob)
    total_val = TOTAL_VAL_RE.search(blob)
    pct100 = bool(PCT_100_RE.search(blob))
    end_ok = bool(END_OK_RE.search(blob))

    if good and total_sub and total_val and (total_sub.group(1) == total_val.group(1)) and pct100 and end_ok:
        return "OK", ["GoodFiles + totals match + 100% + ending successfully"]

    # If we reached here, we didn't get a clear OK; treat as NOK
    return "NOK", ["Missing one or more success markers (GoodFiles/totals/100%/ending successfully)"]


def read_file_safely(path: str) -> Optional[List[str]]:
    if not os.path.exists(path):
        return None
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            return f.readlines()
    except Exception:
        return None


def main():
    args = parse_args()
    date_folder = resolve_date_folder(args.date)

    print("== AUD Parser Prototype ==")
    print("Date folder:", date_folder)
    print("Slot:", args.slot, "(FinalRun)" if args.slot == "16:30" else "(EarlyRun)")
    print("")

    for area in AREAS:
        status = "TBC"
        reasons: List[str] = []
        start_ts = None
        used_file = None

        # Identify which file to use
        for candidate in make_paths_for_area(date_folder, area, args.slot):
            lines = read_file_safely(candidate)
            if lines is None:
                continue  # try next candidate
            used_file = candidate
            if args.slot == "16:30":
                # Capture last block ending with Program is ending...
                end_idx = None
                for i in range(len(lines)-1, -1, -1):
                    if END_MARKER_RE.search(lines[i]):
                        end_idx = i
                        break
                if end_idx is not None:
                    start_idx = 0
                    for j in range(end_idx, -1, -1):
                        if TS_RE.match(lines[j]):
                            start_idx = j
                            break
                    block = lines[start_idx:end_idx+1]
                    m = TS_RE.match(block[0]) if block else None
                    start_ts = m.group(1) if m else None
                else:
                    block = lines[:]
                status, reasons = evaluate_block(block, is_final_slot=True)
            else:
                block, start_ts = extract_block(lines, args.slot, WINDOW_MINUTES)
                status, reasons = evaluate_block(block, is_final_slot=False)

            break  # stop after first readable candidate

        label = f"AUD for US - {area}"
        hyperlink_hint = used_file if used_file else "(file not found)"
        print(f"{label:28s} | {status:3s} | start={start_ts or 'n/a'} | file={hyperlink_hint}")
        if args.verbose and reasons:
            for r in reasons:
                print("   -", r)

    print("\\nLegend: OK=Green, NOK=Orange (or Red if FinalRun in later phase), TBC=Yellow, HOLIDAY=Grey (handled later).")


if __name__ == "__main__":
    sys.exit(main())
