#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import os
import re
from dataclasses import dataclass
from datetime import datetime, date, time, timedelta, timezone
from typing import List, Optional, Tuple, Dict

# ---- Timezones ----
try:
    from zoneinfo import ZoneInfo
except Exception:
    # If running on older Python or missing tzdata, user should install tzdata.
    raise SystemExit("zoneinfo not available. On Windows, run: python -m pip install tzdata")

SERVER_TZ = ZoneInfo("Europe/London")  # Server writes timestamps in London local time (handles BST/DST)

REGION_TZ: Dict[str, ZoneInfo] = {
    # Region local clocks for *scheduling* windows:
    "AUDforUS": ZoneInfo("Australia/Sydney"),
    "SGDforUS": ZoneInfo("Asia/Singapore"),
    "EURforUS": ZoneInfo("Europe/London"),     # If you later confirm Paris/Frankfurt, change to "Europe/Paris"
    "USD":      ZoneInfo("America/New_York"),
}

# ---- Windows (local to each region) ----
# Index & SingleName
IDX_SN_WINDOWS = {
    "early":   (time(10, 0), time(10, 15)),
    "late1":   (time(16, 0), time(16, 4)),
    "late2":   (time(16, 15), time(16, 19)),
    "final":   (time(16, 30), time(16, 35)),
}
# IndexOption
IDX_OPT_WINDOWS = {
    "early":   (time(10, 0), time(10, 15)),
    "late1":   (time(16, 0), time(16, 4)),
    "late2":   (time(16, 10), time(16, 19)),  # per your note
    "final":   (time(16, 30), time(16, 40)),  # per your note
}

# ---- Files & Paths (DO NOT CHANGE: you said these are 100% correct) ----
def server_path(base_date: str, typ: str, region: str, fname: str) -> str:
    # Example:
    # D:\DATA\logs\fixlink\2025-08-22\ICEDIRECT\Index\AUDforUS\PriceGeneration_AUDforUS_FinalRun.log
    return os.path.join(r"D:\DATA\logs\fixlink", base_date, "ICEDIRECT", typ, region, fname)

def early_log_name(region: str) -> str:
    # PriceGeneration_<REGION>_EarlyRun.log
    return f"PriceGeneration_{region}_EarlyRun.log"

def final_log_name(region: str) -> str:
    # PriceGeneration_<REGION>_FinalRun.log
    return f"PriceGeneration_{region}_FinalRun.log"

def option_summary_name(region: str) -> str:
    # SubmissionSummaryIDX_OPT_<REGION>.log
    return f"SubmissionSummaryIDX_OPT_{region}.log"

# NAS path for SubmissionLogs column (FinalRun only, or SubmissionSummary for IndexOption)
def nas_path(base_date: str, typ: str, region: str, final_filename: str) -> str:
    # Keep the convention exactly as you validated earlier
    return r"\\lonshr-emlogmgmt\CIBFIEMCRET_LOGS\vol2\fixlink\ws9100ppc00462" + "\\" + os.path.join(
        base_date, "ICEDIRECT", typ, region, final_filename
    ).replace("/", "\\")

# ---- Parsing helpers ----
DT_PATTERNS = [
    # [2025-08-21 16:30:00.069]  INFO - ...
    re.compile(r"\[(\d{4}-\d{2}-\d{2})\s+(\d{2}:\d{2}:\d{2}(?:\.\d+)?)\]"),
    # 2025/08/21 16:25:16 INFO - ...
    re.compile(r"(\d{4}/\d{2}/\d{2})\s+(\d{2}:\d{2}:\d{2})"),
    # 2025-08-21 16:25:16 INFO - ...
    re.compile(r"(\d{4}-\d{2}-\d{2})\s+(\d{2}:\d{2}:\d{2})"),
]

def parse_dt_from_line(line: str) -> Optional[datetime]:
    for pat in DT_PATTERNS:
        m = pat.search(line)
        if m:
            dstr = m.group(1)
            tstr = m.group(2)
            # normalize separators
            dstr = dstr.replace("/", "-")
            # strip fractional seconds if present
            if "." in tstr:
                tstr = tstr.split(".")[0]
            try:
                dt_naive = datetime.strptime(f"{dstr} {tstr}", "%Y-%m-%d %H:%M:%S")
                # IMPORTANT: timestamps in files are server (London) local time
                return dt_naive.replace(tzinfo=SERVER_TZ)
            except Exception:
                return None
    return None

@dataclass
class WindowStatus:
    mark: str         # "✅" / "❌" / "⏳"
    detail: str       # reason/debug
    missing_info: List[str]  # lines to add to notes section (quotable/clearable/invalid)

SUCCESS_RE = re.compile(r"Program is ending successfully", re.IGNORECASE)
VALIDATION_ERR_RE = re.compile(r"Validation Error\(s\)\s*:\s*(\d+)", re.IGNORECASE)
MISSING_CLEARABLE_RE = re.compile(r"Missing\s+(?:Clearable\s+Prices|Prices\s*\(Clearable[^)]*\))\s*:\s*(\d+)", re.IGNORECASE)
MISSING_QUOTABLE_RE = re.compile(r"Missing\s+(?:Quotable\s+Prices|Prices\s*\(Quotable[^)]*\))\s*:\s*(\d+)", re.IGNORECASE)
MISSING_GENERIC_RE = re.compile(r"Missing\s+Prices\s*:\s*(\d+)", re.IGNORECASE)
INVALID_CURVE_RE = re.compile(r"not sent\. Invalid", re.IGNORECASE)

# For Index Option Summary
ACCEPTED_OPT_RE = re.compile(r"Accepted\s+Index\s+Option\s+quotes\s+(\d+)", re.IGNORECASE)
REJECTED_OPT_RE = re.compile(r"Rejected\s+Index\s+Option\s+quotes\s+(\d+)", re.IGNORECASE)
WINDOW_OPEN_RE   = re.compile(r"The settlement window is OPEN", re.IGNORECASE)
WINDOW_CLOSED_RE = re.compile(r"The settlement window is CLOSED", re.IGNORECASE)

def region_window_to_server(date_str: str, region: str, t0: time, t1: time) -> Tuple[datetime, datetime]:
    d_parts = [int(p) for p in date_str.split("-")]
    d = date(d_parts[0], d_parts[1], d_parts[2])
    rt0 = datetime.combine(d, t0, tzinfo=REGION_TZ[region])
    rt1 = datetime.combine(d, t1, tzinfo=REGION_TZ[region])
    # Convert to server (London) time for matching log timestamps
    return rt0.astimezone(SERVER_TZ), rt1.astimezone(SERVER_TZ)

def load_lines(path: str) -> List[str]:
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as f:
            return f.readlines()
    except FileNotFoundError:
        return []
    except Exception:
        # fallback cp1252 if needed
        try:
            with open(path, "r", encoding="cp1252", errors="replace") as f:
                return f.readlines()
        except Exception:
            return []

def evaluate_window_from_early_or_final(lines: List[str], win_start: datetime, win_end: datetime) -> WindowStatus:
    found_lines = []
    for ln in lines:
        dt = parse_dt_from_line(ln)
        if dt and (win_start <= dt <= win_end):
            found_lines.append(ln)

    if not found_lines:
        # If the window has already ended (server now past end), show waiting or NOK?
        now_srv = datetime.now(SERVER_TZ)
        if now_srv > win_end:
            return WindowStatus("⏳", "No lines in window (file not ready or run didn’t execute).", [])
        else:
            return WindowStatus("⏳", "Window not yet complete.", [])

    success = any(SUCCESS_RE.search(ln) for ln in found_lines)
    val_errs = sum(int(m.group(1)) for ln in found_lines for m in [VALIDATION_ERR_RE.search(ln)] if m)
    miss_clearable = sum(int(m.group(1)) for ln in found_lines for m in [MISSING_CLEARABLE_RE.search(ln)] if m)
    # Some logs only have "Missing Prices: X" (treat as generic — does not flip to NOK unless we know they’re clearable)
    miss_generic = sum(int(m.group(1)) for ln in found_lines for m in [MISSING_GENERIC_RE.search(ln)] if m)
    miss_quotable = sum(int(m.group(1)) for ln in found_lines for m in [MISSING_QUOTABLE_RE.search(ln)] if m)

    invalid_msgs = [ln.strip() for ln in found_lines if INVALID_CURVE_RE.search(ln)]

    notes = []
    if miss_quotable:
        notes.append(f"Info: Missing Quotable Prices = {miss_quotable}")
    if miss_generic and not miss_clearable and not miss_quotable:
        # Generic message seen in Index logs
        notes.append(f"Info: Missing Prices (unspecified) = {miss_generic}")
    if invalid_msgs:
        notes.extend([f"Info: {imsg}" for imsg in invalid_msgs])

    if val_errs > 0 or miss_clearable > 0:
        return WindowStatus("❌", f"ValidationErrors={val_errs}, MissingClearable={miss_clearable}", notes)

    if success:
        return WindowStatus("✅", "Program ended successfully in window.", notes)

    # No explicit success line but also no hard errors
    return WindowStatus("⏳", "No explicit success line found in window.", notes)

def evaluate_final_from_option_summary(lines: List[str], win_start: datetime, win_end: datetime) -> WindowStatus:
    found_lines = []
    for ln in lines:
        dt = parse_dt_from_line(ln)
        if dt and (win_start <= dt <= win_end):
            found_lines.append(ln)

    if not found_lines:
        now_srv = datetime.now(SERVER_TZ)
        if now_srv > win_end:
            return WindowStatus("⏳", "No lines in summary window.", [])
        else:
            return WindowStatus("⏳", "Summary window not yet complete.", [])

    accepted = 0
    rejected = 0
    for ln in found_lines:
        m1 = ACCEPTED_OPT_RE.search(ln)
        if m1:
            accepted = max(accepted, int(m1.group(1)))
        m2 = REJECTED_OPT_RE.search(ln)
        if m2:
            rejected = max(rejected, int(m2.group(1)))

    if rejected > 0:
        return WindowStatus("❌", f"Rejected Index Option quotes = {rejected}", [])

    if accepted > 0:
        return WindowStatus("✅", f"Accepted Index Option quotes = {accepted}", [])

    # If neither found, keep waiting
    return WindowStatus("⏳", "No accepted/rejected counts found.", [])

# ---- Row + HTML rendering ----
@dataclass
class Row:
    region: str
    submission_type_label: str       # e.g., "AUDforUS – INDEX"
    early_href: Optional[str]
    final_href: Optional[str]
    early_mark: str
    late1_mark: str
    late2_mark: str
    final_mark: str
    submission_logs_text: str        # NAS path string
    notes: List[str]

def build_rows(base_date: str) -> Tuple[List[Row], List[str]]:
    rows: List[Row] = []
    all_notes: List[str] = []

    # helper to make windows in server tz from region/local tz
    def win(typ: str, region: str, key: str) -> Tuple[datetime, datetime]:
        if typ == "IndexOption":
            t0, t1 = IDX_OPT_WINDOWS[key]
        else:
            t0, t1 = IDX_SN_WINDOWS[key]
        return region_window_to_server(base_date, region, t0, t1)

    # Define the ordered set: region → (Index, SingleName) and IndexOption where applicable
    plan = [
        ("AUDforUS", ["Index", "SingleName"], []),                         # no IndexOption for AUD
        ("SGDforUS", ["Index", "SingleName"], []),                         # no IndexOption for SGD
        ("EURforUS", ["Index", "SingleName"], ["IndexOption"]),            # IndexOption exists
        ("USD",      ["Index", "SingleName"], ["IndexOption"]),            # IndexOption exists
    ]

    for region, main_types, opt_types in plan:
        for typ in main_types + opt_types:
            # Build file paths
            if typ == "IndexOption":
                # Early & Latest from EarlyRun.log (IndexOption folder)
                early_path = server_path(base_date, "IndexOption", region, early_log_name(region))
                final_path = server_path(base_date, "IndexOption", region, option_summary_name(region))
                final_filename = option_summary_name(region)
            else:
                early_path = server_path(base_date, typ, region, early_log_name(region))
                final_path = server_path(base_date, typ, region, final_log_name(region))
                final_filename = final_log_name(region)

            # Hrefs (keep as you validated earlier)
            early_href = early_path if os.path.exists(early_path) else early_path  # keep href even if not present yet
            final_href = final_path if os.path.exists(final_path) else final_path

            # NAS path text (Final run logs only; for IndexOption it’s the SubmissionSummary)
            submission_logs_text = nas_path(base_date, typ, region, final_filename)

            # Load files
            early_lines = load_lines(early_path)
            final_lines = load_lines(final_path)

            # Compute marks
            w_early = win(typ, region, "early")
            w_late1 = win(typ, region, "late1")
            w_late2 = win(typ, region, "late2")
            w_final = win(typ, region, "final")

            # Evaluate windows
            early_status = evaluate_window_from_early_or_final(early_lines, *w_early)
            late1_status = evaluate_window_from_early_or_final(early_lines, *w_late1)
            late2_status = evaluate_window_from_early_or_final(early_lines, *w_late2)

            if typ == "IndexOption":
                final_status = evaluate_final_from_option_summary(final_lines, *w_final)
            else:
                final_status = evaluate_window_from_early_or_final(final_lines, *w_final)

            # Accumulate notes
            notes = []
            notes.extend(early_status.missing_info)
            notes.extend(late1_status.missing_info)
            notes.extend(late2_status.missing_info)
            notes.extend(final_status.missing_info)
            # De-dup & keep order
            seen = set()
            deduped = []
            for n in notes:
                if n not in seen:
                    deduped.append(n)
                    seen.add(n)

            # Row label & ordering
            label = f"{region} – {'INDEX' if typ=='Index' else ('SINGLE NAME' if typ=='SingleName' else 'INDEX OPTION')}"
            row = Row(
                region=region.split('forUS')[0],  # "AUD", "SGD", "EUR", "USD"
                submission_type_label=label,
                early_href=early_href,
                final_href=final_href,
                early_mark=early_status.mark,
                late1_mark=late1_status.mark,
                late2_mark=late2_status.mark,
                final_mark=final_status.mark,
                submission_logs_text=submission_logs_text,
                notes=deduped
            )
            rows.append(row)
            all_notes.extend([f"{label}: {n}" for n in deduped])

    return rows, all_notes

def render_html(rows: List[Row], notes: List[str]) -> str:
    # Big centered marks, timings on new lines as requested earlier
    css = """
    <style>
      body { font-family: Arial, Helvetica, sans-serif; }
      table { border-collapse: collapse; width: 100%; }
      th, td { border: 1px solid #ddd; padding: 10px; }
      th { background: #f6f6f6; text-align: center; }
      td { vertical-align: middle; }
      td.center { text-align: center; font-size: 28px; }
      a { text-decoration: none; }
      .label { font-weight: 600; }
      .notes { margin-top: 20px; font-size: 13px; white-space: pre-wrap; }
      .subtype a { font-weight: 600; }
      .mono { font-family: Consolas, "Courier New", monospace; }
    </style>
    """
    header = """
    <tr>
      <th>Region</th>
      <th>SubmissionType</th>
      <th>EarlyRun<br/>(10:00–10:15)</th>
      <th>LatestRun #1<br/>(16:00–16:04)</th>
      <th>LatestRun #2<br/>(16:15–16:19)</th>
      <th>FinalSubmission<br/>(4:30 PM)</th>
      <th>SubmissionLogs</th>
    </tr>
    """

    def cell_link(text: str, href: Optional[str]) -> str:
        if href:
            return f'<a href="file:///{href.replace("\\\\","/").replace(" ","%20")}">{text}</a>'
        return text

    # Build table rows grouped by region order AUD, SGD, EUR, USD with Index then Single Name, then Index Option where applicable
    # rows are already in that order by build_rows
    body_rows = []
    for r in rows:
        # FinalSubmission column title changes in header "4:30 PM" but we still link to FinalRun or SubmissionSummary for options
        body_rows.append(f"""
        <tr>
          <td class="center">{r.region}</td>
          <td class="subtype">{cell_link(r.submission_type_label, r.early_href)}</td>
          <td class="center">{r.early_mark}</td>
          <td class="center">{r.late1_mark}</td>
          <td class="center">{r.late2_mark}</td>
          <td class="center">{cell_link(r.final_mark, r.final_href)}</td>
          <td class="mono">{r.submission_logs_text}</td>
        </tr>
        """)

    notes_section = ""
    if notes:
        notes_text = "\n".join(notes)
        notes_section = f"""
        <div class="notes">
          <div class="label">Notes / Info (quotable), Cautions (clearable), Invalids</div>
          <pre>{notes_text}</pre>
        </div>
        """

    html = f"""<!doctype html>
<html><head><meta charset="utf-8"><title>ICE Status</title>{css}</head>
<body>
  <table>
    {header}
    {''.join(body_rows)}
  </table>
  {notes_section}
</body></html>
"""
    return html

def render_text(rows: List[Row], notes: List[str]) -> None:
    # Minimal text mode for quick checks (UTF-8 safe)
    for r in rows:
        print(f"{r.region} | {r.submission_type_label} | {r.early_mark} | {r.late1_mark} | {r.late2_mark} | {r.final_mark} | {r.submission_logs_text}")
    if notes:
        print("\nNOTES:")
        for n in notes:
            print(f" - {n}")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", required=True, help="Server folder date, e.g. 2025-08-22")
    ap.add_argument("--mode", choices=["html", "text"], default="html")
    args = ap.parse_args()

    rows, notes = build_rows(args.date)

    if args.mode == "text":
        # text mode uses default console encoding, but contains only ASCII + emojis
        # If your console can't show emojis, redirect to a file or use html mode
        render_text(rows, notes)
    else:
        html = render_html(rows, notes)
        # ALWAYS write bytes to preserve UTF-8 (✅/❌/⏳)
        import sys
        sys.stdout.buffer.write(html.encode("utf-8"))

if __name__ == "__main__":
    main()
