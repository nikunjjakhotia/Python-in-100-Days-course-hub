#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ice_status_all.py
- Real status detection from server logs (no tzdata dependency).
- Keeps your existing hyperlink paths logic: we DO NOT alter link building;
  only parsing + status logic here is self-contained.
- Outputs either HTML (with ✅/❌/⏳, big & centered) or text.

Run:
  python ice_status_all.py --date 2025-08-22 --mode html > status.html
"""

import argparse
import datetime as dt
import html
import os
import re
import sys
from typing import List, Tuple, Dict, Optional

# ---------------------------
# Configuration / Constants
# ---------------------------

# Server writes timestamps in LONDON LOCAL TIME.
SERVER_TZ_NAME = "Europe/London"

# Regions and their logical "SubmissionType" rows (Index, SingleName, IndexOption)
REGIONS = ["AUDforUS", "SGDforUS", "EURforUS", "USD"]
TYPES = ["Index", "SingleName"]
IDX_OPT_REGION = "EURforUS"  # Index Options only for EUR (per your earlier examples)

# SERVER file roots (these are used for parsing only; DO NOT CHANGE HYPERLINKS)
SERVER_ROOT = r"D:\DATA\logs\fixlink"

# Filenames
EARLY_FILENAME = "PriceGeneration_{region}_EarlyRun.log"
FINAL_FILENAME = "PriceGeneration_{region}_FinalRun.log"
IDX_OPT_SUMMARY = "SubmissionSummaryIDX_OPT_EURforUS.log"

# Subdirectories by type
TYPE_DIR = {
    "Index": "ICEDIRECT\\Index\\{region}",
    "SingleName": "ICEDIRECT\\SingleName\\{region}",
    "IndexOption": "ICEDIRECT\\IndexOption\\EURforUS",
}

# Windows (local region time)
WINDOWS_INDEX_SN = {
    "EarlyRun": (dt.time(10, 0), dt.time(10, 15)),
    "Latest1": (dt.time(16, 0), dt.time(16, 4)),
    "Latest2": (dt.time(16, 15), dt.time(16, 19)),
    "Final":   (dt.time(16, 30), dt.time(16, 35)),
}
WINDOWS_IDX_OPT = {
    "EarlyRun": (dt.time(10, 0), dt.time(10, 15)),
    "Latest1":  (dt.time(16, 0), dt.time(16, 4)),
    "Latest2":  (dt.time(16, 10), dt.time(16, 19)),
    "Final":    (dt.time(16, 30), dt.time(16, 40)),
}

# HTML status glyphs (keep UTF-8 output)
GLYPH_OK = "✅"
GLYPH_WAIT = "⏳"
GLYPH_NOK = "❌"

# ---------------------------
# Minimal time-zone support (built-in DST rules, no tzdata)
# ---------------------------

def last_sunday(year: int, month: int) -> dt.date:
    # Find last Sunday of a given month
    d = dt.date(year, month, 1)
    # go to next month then back one day until Sunday
    if month == 12:
        d2 = dt.date(year + 1, 1, 1)
    else:
        d2 = dt.date(year, month + 1, 1)
    d2 -= dt.timedelta(days=1)
    while d2.weekday() != 6:  # Sunday=6
        d2 -= dt.timedelta(days=1)
    return d2

def first_sunday(year: int, month: int) -> dt.date:
    d = dt.date(year, month, 1)
    while d.weekday() != 6:
        d += dt.timedelta(days=1)
    return d

def second_sunday(year: int, month: int) -> dt.date:
    d = first_sunday(year, month)
    return d + dt.timedelta(days=7)

def europe_london_offset(d: dt.date) -> int:
    # UTC offset in hours for Europe/London (GMT/BST)
    start = last_sunday(d.year, 3)  # last Sunday March
    end = last_sunday(d.year, 10)   # last Sunday October
    # DST from 01:00 UTC last Sun Mar to 01:00 UTC last Sun Oct.
    # For date-only approx, treat between start and end as DST.
    if start <= d < end:
        return 1
    return 0

def europe_paris_offset(d: dt.date) -> int:
    # CET/CEST mirrors London DST but base is UTC+1
    return 1 + europe_london_offset(d)

def asia_singapore_offset(_d: dt.date) -> int:
    return 8  # no DST

def australia_sydney_offset(d: dt.date) -> int:
    # AEST/AEDT: DST from first Sunday in Oct to first Sunday in Apr
    # During DST: UTC+11, otherwise UTC+10
    start = first_sunday(d.year, 10)
    # DST ends first Sunday in April (but careful across year boundary)
    # If date is Jan-Mar: DST if it started previous Oct
    end = first_sunday(d.year, 4)
    if d >= start or d < end:
        return 11
    return 10

def america_newyork_offset(d: dt.date) -> int:
    # EST/EDT: DST from second Sunday in March to first Sunday in November
    start = second_sunday(d.year, 3)
    end = first_sunday(d.year, 11)
    if start <= d < end:
        return -4
    return -5

def region_local_to_london(date_: dt.date, local_t: dt.time, region: str) -> Tuple[dt.datetime, dt.datetime]:
    """
    Convert a (region local) time window start/end to London local datetimes for the same date.
    Returns (start_dt_london, end_dt_london)
    """
    # Offsets in hours
    london_off = europe_london_offset(date_)
    if region.startswith("AUD"):
        reg_off = australia_sydney_offset(date_)
    elif region.startswith("SGD"):
        reg_off = asia_singapore_offset(date_)
    elif region.startswith("EUR"):
        reg_off = europe_paris_offset(date_)
    elif region == "USD":
        reg_off = america_newyork_offset(date_)
    else:
        reg_off = london_off  # fallback, should not happen

    # local_time (region) -> UTC -> London local
    # London_local = region_local - reg_off + london_off
    def to_london(t: dt.time) -> dt.datetime:
        naive = dt.datetime.combine(date_, t)
        # shift by (london - region) hours
        delta_h = london_off - reg_off
        return naive + dt.timedelta(hours=delta_h)

    return to_london(local_t[0]), to_london(local_t[1])

# ---------------------------
# Parsing Helpers
# ---------------------------

TS_RE = re.compile(
    r'(?:\[)?(?P<date>\d{4}[-/]\d{2}[-/]\d{2})[ T](?P<h>\d{2}):(?P<m>\d{2}):(?P<s>\d{2})'
)

def extract_timestamp(line: str) -> Optional[dt.datetime]:
    m = TS_RE.search(line)
    if not m:
        return None
    y, mo, dd = map(int, m.group('date').replace('/', '-').split('-'))
    h, mi, s = int(m.group('h')), int(m.group('m')), int(m.group('s'))
    try:
        return dt.datetime(y, mo, dd, h, mi, s)
    except ValueError:
        return None

def file_lines(path: str) -> List[str]:
    if not os.path.exists(path):
        return []
    # Be defensive about encoding
    with open(path, 'r', encoding='utf-8', errors='replace') as f:
        return f.readlines()

def any_success_in_window(lines: List[str],
                          win_start: dt.datetime,
                          win_end: dt.datetime,
                          kind: str) -> Tuple[bool, bool, List[str]]:
    """
    kind: "Index" | "SingleName" | "IndexOptionFinal" | "IndexOptionEarlyLatest"
    Returns (success_found, hard_fail_found, info_notes)
    """
    success = False
    hard_fail = False
    notes: List[str] = []

    # Track context within window
    for line in lines:
        ts = extract_timestamp(line)
        if not ts:
            continue
        if ts < win_start or ts > win_end:
            continue

        L = line.strip()

        if kind in ("Index", "SingleName"):
            # Success markers
            if "Program is ending successfully" in L:
                success = True
            # Validation errors => hard fail
            m = re.search(r"Validation Error\(s\):\s+(\d+)", L)
            if m and int(m.group(1)) > 0:
                hard_fail = True

            if kind == "SingleName":
                # Missing quotable is OK but we collect as info
                mq = re.search(r"Missing Prices \(Quotable redcodes\)\s*:\s*(\d+)", L, re.I)
                if mq:
                    qmiss = int(mq.group(1))
                    if qmiss > 0:
                        notes.append(f"[INFO] Missing Quotable prices: {qmiss} (OK)")
                # If we ever get an explicit clearable missing line, treat as fail
                mc = re.search(r"Missing (?:Clearable )?Prices\s*:\s*(\d+)", L, re.I)
                # Guard: the SN early sample doesn’t show a distinct “clearable missing” line
                # so we only penalize if explicitly stated and >0
                if mc and int(mc.group(1)) > 0 and "Quotable" not in L:
                    hard_fail = True
                    notes.append(f"[CAUTION] Missing Clearable prices: {mc.group(1)}")
            else:
                # Index: if a total submitted present and no errors, OK; just rely on success flag
                pass

        elif kind == "IndexOptionEarlyLatest":
            # We just confirm activity; the authoritative “final status” comes from FinalSummary
            # Use presence of “Index Option Quotes sent” as success indicator for early/latest.
            if "Index Option Quotes sent" in L:
                success = True

        elif kind == "IndexOptionFinal":
            # From SubmissionSummary: look for Final Summary block KPIs
            if "Final Summary" in L:
                success = True  # we mark presence, then refine below
            acc = re.search(r"Accepted Index Option quotes\s+(\d+)", L)
            rej = re.search(r"Rejected Index Option quotes\s+(\d+)", L)
            if acc:
                notes.append(f"[INFO] Accepted quotes: {acc.group(1)}")
            if rej:
                r = int(rej.group(1))
                notes.append(f"[INFO] Rejected quotes: {r}")
                if r > 0:
                    hard_fail = True

    return success, hard_fail, notes

# ---------------------------
# Build server paths (parse only)
# ---------------------------

def server_path_for(date_: str, region: str, typ: str, phase: str) -> str:
    """
    phase: "Early" | "Final" | "IdxOptSummary"
    """
    base = os.path.join(SERVER_ROOT, date_, TYPE_DIR["Index" if typ in ("Index", "SingleName") else "IndexOption"].format(region=region))
    if typ == "Index":
        if phase == "Early":
            fn = EARLY_FILENAME.format(region=region)
            return os.path.join(SERVER_ROOT, date_, TYPE_DIR["Index"].format(region=region), fn)
        else:
            fn = FINAL_FILENAME.format(region=region)
            return os.path.join(SERVER_ROOT, date_, TYPE_DIR["Index"].format(region=region), fn)
    elif typ == "SingleName":
        if phase == "Early":
            fn = EARLY_FILENAME.format(region=region)
            return os.path.join(SERVER_ROOT, date_, TYPE_DIR["SingleName"].format(region=region), fn)
        else:
            fn = FINAL_FILENAME.format(region=region)
            return os.path.join(SERVER_ROOT, date_, TYPE_DIR["SingleName"].format(region=region), fn)
    else:  # IndexOption
        return os.path.join(SERVER_ROOT, date_, TYPE_DIR["IndexOption"], IDX_OPT_SUMMARY)

# ---------------------------
# Status computation
# ---------------------------

def status_for_window(lines: List[str],
                      win: Tuple[dt.datetime, dt.datetime],
                      now_london: dt.datetime,
                      kind: str) -> Tuple[str, List[str]]:
    """Return (glyph, notes) for the given window."""
    s, fail, notes = any_success_in_window(lines, win[0], win[1], kind)
    if s and not fail:
        return GLYPH_OK, notes
    if now_london <= win[1] and not s:
        return GLYPH_WAIT, notes
    # window over
    return GLYPH_NOK, notes

def compute_region_rows(date_: dt.date, now_london: dt.datetime) -> Tuple[List[Dict], List[str]]:
    """
    Build rows for all regions/types. Also return collected footnotes (info/caution) to show at bottom.
    """
    rows = []
    footnotes: List[str] = []

    # Helper for windows per type
    def london_window(region: str, tstart: dt.time, tend: dt.time) -> Tuple[dt.datetime, dt.datetime]:
        return region_local_to_london(date_, (tstart, tend), region)

    for region in REGIONS:
        # Index + SingleName
        for typ in TYPES:
            # Choose correct windows set
            W = WINDOWS_INDEX_SN
            # Early/Latest windows (from EARLY log)
            early_log = server_path_for(date_.isoformat(), region, typ, "Early")
            final_log = server_path_for(date_.isoformat(), region, typ, "Final")

            early_lines = file_lines(early_log)
            final_lines = file_lines(final_log)

            # Windows in London
            w_early = london_window(region, *W["EarlyRun"])
            w_l1    = london_window(region, *W["Latest1"])
            w_l2    = london_window(region, *W["Latest2"])
            w_final = london_window(region, *W["Final"])

            # Compute statuses
            s_early, n1 = status_for_window(early_lines, w_early, now_london, typ)
            s_l1, n2    = status_for_window(early_lines, w_l1,    now_london, typ)
            s_l2, n3    = status_for_window(early_lines, w_l2,    now_london, typ)
            s_final, n4 = status_for_window(final_lines, w_final, now_london, typ)

            # Collect notes (only add meaningful lines)
            for n in (n1+n2+n3+n4):
                if "[INFO]" in n or "[CAUTION]" in n:
                    footnotes.append(f"{region} - {typ}: {n}")

            rows.append({
                "region": region.replace("forUS",""),
                "subtype": f"{region}-{typ}",
                "early": s_early,
                "l1": s_l1,
                "l2": s_l2,
                "final": s_final,
                # Leave hyperlinks exactly as in your current HTML builder:
                "early_path": early_log,   # you already render this correctly to NAS link
                "final_path": final_log,
                "logs_col": final_log,     # SubmissionLogs column (FinalRun path only)
            })

        # Index Options (EUR only)
        if region == IDX_OPT_REGION:
            typ = "IndexOption"
            W = WINDOWS_IDX_OPT
            sum_path = server_path_for(date_.isoformat(), region, typ, "IdxOptSummary")
            lines = file_lines(sum_path)

            w_early = london_window(region, *W["EarlyRun"])
            w_l1    = london_window(region, *W["Latest1"])
            w_l2    = london_window(region, *W["Latest2"])
            w_final = london_window(region, *W["Final"])

            s_early, n1 = status_for_window(lines, w_early, now_london, "IndexOptionEarlyLatest")
            s_l1, n2    = status_for_window(lines, w_l1,    now_london, "IndexOptionEarlyLatest")
            s_l2, n3    = status_for_window(lines, w_l2,    now_london, "IndexOptionEarlyLatest")
            s_final, n4 = status_for_window(lines, w_final, now_london, "IndexOptionFinal")

            for n in (n1+n2+n3+n4):
                if "[INFO]" in n or "[CAUTION]" in n:
                    footnotes.append(f"{region} - IndexOption: {n}")

            rows.append({
                "region": region.replace("forUS",""),
                "subtype": f"{region}-IndexOption",
                "early": s_early,
                "l1": s_l1,
                "l2": s_l2,
                "final": s_final,
                "early_path": sum_path,    # EarlyRun hyperlink points to the summary for options (per your last alignment)
                "final_path": sum_path,    # FinalSubmission (options) hyperlinks to SubmissionSummary
                "logs_col": sum_path,      # SubmissionLogs column
            })

    return rows, footnotes

# ---------------------------
# Rendering (HTML/Text)
# ---------------------------

def td_center_big(s: str) -> str:
    return f'<td style="text-align:center;font-size:24px;">{html.escape(s)}</td>'

def render_html(rows: List[Dict], notes: List[str]) -> str:
    # Timings in column headers (new line for readability)
    head = """
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>ICE Direct Submissions Status</title>
<style>
body{font-family:Segoe UI,Arial,Helvetica,sans-serif}
table{border-collapse:collapse;width:100%}
th,td{border:1px solid #ddd;padding:8px}
th{background:#f5f7fa;text-align:center}
.subcol{white-space:pre-line}
a{color:#0645AD;text-decoration:none}
a:hover{text-decoration:underline}
.small{font-size:12px;color:#555}
</style>
</head>
<body>
<h2>ICE Direct Submissions Status</h2>
<table>
<thead>
<tr>
  <th>Region</th>
  <th>SubmissionType</th>
  <th class="subcol">EarlyRun\n(10:00 AM)</th>
  <th class="subcol">LatestRun #1\n(4:00 PM)</th>
  <th class="subcol">LatestRun #2\n(4:15 PM)</th>
  <th class="subcol">FinalSubmission\n(4:30 PM)</th>
  <th>SubmissionLogs</th>
</tr>
</thead>
<tbody>
"""
    rows_html = []
    # Ensure pairing: AUD Index then AUD SingleName, then SGD..., and EUR IndexOption right after EUR SN.
    # compute_region_rows already emits that order.

    for r in rows:
        region_label = html.escape(r["region"])
        subtype_text = f'{r["subtype"]}'
        # Keep your existing hyperlink conversion to NAS path OUTSIDE this script (unchanged).
        # Here we print Windows "file:///" links directly for preview; your existing code can overwrite it.
        def file_link(path, text):
            href = "file:///" + path.replace("\\", "/").replace(" ", "%20")
            return f'<a href="{href}">{html.escape(text)}</a>'

        subtype_link = file_link(r["early_path"], subtype_text)  # hyperlink SubmissionType to EarlyRun log
        final_link = file_link(r["final_path"], "FinalRun")       # FinalSubmission cell hyperlink text
        logs_link = file_link(r["logs_col"], os.path.basename(r["logs_col"]))

        row = (
            f"<tr>"
            f"<td>{region_label}</td>"
            f"<td>{subtype_link}</td>"
            f"{td_center_big(r['early'])}"
            f"{td_center_big(r['l1'])}"
            f"{td_center_big(r['l2'])}"
            f"<td style='text-align:center;font-size:16px;'>{final_link}<br/><div style='font-size:22px;margin-top:4px;'>{html.escape(r['final'])}</div></td>"
            f"<td>{logs_link}</td>"
            f"</tr>"
        )
        rows_html.append(row)

    tail_notes = ""
    if notes:
        tail_notes = "<h3>Notes</h3><ul>" + "".join(f"<li class='small'>{html.escape(n)}</li>" for n in notes) + "</ul>"

    tail = f"""
</tbody>
</table>
{tail_notes}
</body>
</html>
"""
    return head + "\n".join(rows_html) + tail

def render_text(rows: List[Dict], notes: List[str]) -> None:
    for r in rows:
        print(f"{r['region']:>3} | {r['subtype']:<24} | {r['early']} {r['l1']} {r['l2']} {r['final']}")
    if notes:
        print("\nNotes:")
        for n in notes:
            print(" -", n)

# ---------------------------
# Main
# ---------------------------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", required=True, help="YYYY-MM-DD")
    ap.add_argument("--mode", choices=["html","text"], default="html")
    args = ap.parse_args()

    try:
        date_ = dt.date.fromisoformat(args.date)
    except ValueError:
        print("Invalid --date; expected YYYY-MM-DD", file=sys.stderr)
        sys.exit(2)

    now_london = dt.datetime.now()  # Server is London-local; perfect

    rows, notes = compute_region_rows(date_, now_london)

    if args.mode == "text":
        render_text(rows, notes)
    else:
        html_out = render_html(rows, notes)
        # Force UTF-8 bytes to avoid cp1252 issues
        sys.stdout.buffer.write(html_out.encode("utf-8"))

if __name__ == "__main__":
    main()
