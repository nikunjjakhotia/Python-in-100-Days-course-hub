#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import datetime as dt
import html
import os
import re
import sys
from typing import List, Tuple, Dict, Optional

# ---------------------------
# CONSTANTS (do not change links)
# ---------------------------

# Parse FROM server paths:
SERVER_ROOT = r"D:\DATA\logs\fixlink"

# Build NAS hyperlinks TO these UNC roots (LOCKED):
NAS_ROOT = r"\\lonshr-emlogmgmt\CIBFIEMCRET_LOGS\vol2\fixlink\ws9100ppc00462"

# Submission rows order: region pairs, with EUR IndexOption tucked after EUR
REGIONS = ["AUDforUS", "SGDforUS", "EURforUS", "USD"]
TYPES = ["Index", "SingleName"]
IDX_OPT_REGIONS = ["EURforUS"]  # extendable later if USD options are added

# Filenames (kept per your environment)
EARLY_FILENAME = "PriceGeneration_{region}_EarlyRun.log"
FINAL_FILENAME = "PriceGeneration_{region}_FinalRun.log"
IDX_OPT_EARLY_FILENAME = "PriceGeneration_{region}_EarlyRun.log"
IDX_OPT_SUMMARY = "SubmissionSummaryIDX_OPT_{region}.log"  # e.g., EURforUS

# Subdirectories by type
TYPE_DIR = {
    "Index":       r"ICEDIRECT\Index\{region}",
    "SingleName":  r"ICEDIRECT\SingleName\{region}",
    "IndexOption": r"ICEDIRECT\IndexOption\{region}",
}

# Status glyphs
OK = "✅"
WAIT = "⏳"
NOK = "❌"

# ---------------------------
# Regional time windows (local)
# ---------------------------

# Default windows for Index & SingleName (local region time)
WINDOWS_INDEX_SN = {
    "EarlyRun": (dt.time(10, 0), dt.time(10, 15)),
    "Latest1":  (dt.time(16, 0), dt.time(16, 4)),
    "Latest2":  (dt.time(16, 15), dt.time(16, 19)),
    "Final":    (dt.time(16, 30), dt.time(16, 35)),
}
# AUD special: EarlyRun is 11:00–11:15 (Sydney)
WINDOWS_AUD_SN = {
    **WINDOWS_INDEX_SN,
    "EarlyRun": (dt.time(11, 0), dt.time(11, 15)),
}

# Index Options windows (local)
WINDOWS_IDX_OPT = {
    "EarlyRun": (dt.time(10, 0), dt.time(10, 15)),
    "Latest1":  (dt.time(16, 0), dt.time(16, 4)),
    "Latest2":  (dt.time(16, 10), dt.time(16, 19)),
    "Final":    (dt.time(16, 30), dt.time(16, 40)),
}

# ---------------------------
# Minimal timezone math (no tzdata install)
# Server timestamps are LONDON local; windows are defined in region local.
# We convert region-local windows -> London-local datetime ranges.
# ---------------------------

def last_sunday(year: int, month: int) -> dt.date:
    d1 = dt.date(year, month, 1)
    if month == 12:
        d2 = dt.date(year + 1, 1, 1)
    else:
        d2 = dt.date(year, month + 1, 1)
    d2 -= dt.timedelta(days=1)
    while d2.weekday() != 6:
        d2 -= dt.timedelta(days=1)
    return d2

def first_sunday(year: int, month: int) -> dt.date:
    d = dt.date(year, month, 1)
    while d.weekday() != 6:
        d += dt.timedelta(days=1)
    return d

def second_sunday(year: int, month: int) -> dt.date:
    return first_sunday(year, month) + dt.timedelta(days=7)

def europe_london_offset(d: dt.date) -> int:
    # BST between last Sunday Mar and last Sunday Oct
    start = last_sunday(d.year, 3)
    end = last_sunday(d.year, 10)
    return 1 if (start <= d < end) else 0

def europe_paris_offset(d: dt.date) -> int:
    return 1 + europe_london_offset(d)  # CET/CEST

def asia_singapore_offset(_d: dt.date) -> int:
    return 8

def australia_sydney_offset(d: dt.date) -> int:
    # DST from first Sunday in Oct to first Sunday in Apr
    start = first_sunday(d.year, 10)
    end = first_sunday(d.year, 4)
    return 11 if (d >= start or d < end) else 10

def america_newyork_offset(d: dt.date) -> int:
    start = second_sunday(d.year, 3)
    end = first_sunday(d.year, 11)
    return -4 if (start <= d < end) else -5

def region_offset(date_: dt.date, region: str) -> int:
    if region.startswith("AUD"):
        return australia_sydney_offset(date_)
    if region.startswith("SGD"):
        return asia_singapore_offset(date_)
    if region.startswith("EUR"):
        return europe_paris_offset(date_)
    if region == "USD":
        return america_newyork_offset(date_)
    return europe_london_offset(date_)  # fallback

def to_london_window(date_: dt.date, region: str, t0: dt.time, t1: dt.time) -> Tuple[dt.datetime, dt.datetime]:
    london_off = europe_london_offset(date_)
    reg_off = region_offset(date_, region)
    # London_local = region_local - reg_off + london_off
    delta_h = london_off - reg_off
    start = dt.datetime.combine(date_, t0) + dt.timedelta(hours=delta_h)
    end   = dt.datetime.combine(date_, t1) + dt.timedelta(hours=delta_h)
    return start, end

# ---------------------------
# File path helpers
# ---------------------------

def server_path(date_iso: str, region: str, typ: str, phase: str) -> str:
    """
    typ: "Index"|"SingleName"|"IndexOption"
    phase: "Early"|"Final"|"Summary"
    """
    if typ in ("Index", "SingleName"):
        base = os.path.join(SERVER_ROOT, date_iso, TYPE_DIR[typ].format(region=region))
        if phase == "Early":
            return os.path.join(base, EARLY_FILENAME.format(region=region))
        else:
            return os.path.join(base, FINAL_FILENAME.format(region=region))
    else:
        base = os.path.join(SERVER_ROOT, date_iso, TYPE_DIR["IndexOption"].format(region=region))
        if phase == "Early":
            return os.path.join(base, IDX_OPT_EARLY_FILENAME.format(region=region))
        else:
            return os.path.join(base, IDX_OPT_SUMMARY.replace("{region}", region))

def nas_path(date_iso: str, region: str, typ: str, phase: str) -> str:
    """
    Build UNC NAS path with EXACT same structure as server, just different root.
    (Locked request: we won’t alter this again.)
    """
    if typ in ("Index", "SingleName"):
        base = os.path.join(NAS_ROOT, date_iso, TYPE_DIR[typ].replace("{region}", region))
        if phase == "Early":
            return os.path.join(base, EARLY_FILENAME.format(region=region))
        else:
            return os.path.join(base, FINAL_FILENAME.format(region=region))
    else:
        base = os.path.join(NAS_ROOT, date_iso, TYPE_DIR["IndexOption"].replace("{region}", region))
        if phase == "Early":
            return os.path.join(base, IDX_OPT_EARLY_FILENAME.format(region=region))
        else:
            return os.path.join(base, IDX_OPT_SUMMARY.replace("{region}", region))

def read_lines(path: str) -> List[str]:
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        return f.readlines()

# ---------------------------
# Parsing
# ---------------------------

TS_RE = re.compile(r'(?:\[)?(?P<date>\d{4}[-/]\d{2}[-/]\d{2})[ T](?P<h>\d{2}):(?P<m>\d{2}):(?P<s>\d{2})')

def ts_of(line: str) -> Optional[dt.datetime]:
    m = TS_RE.search(line)
    if not m:
        return None
    y, mo, dd = map(int, m.group('date').replace('/', '-').split('-'))
    h, mi, s = int(m.group('h')), int(m.group('m')), int(m.group('s'))
    try:
        return dt.datetime(y, mo, dd, h, mi, s)
    except ValueError:
        return None

def scan_window(lines: List[str],
                w: Tuple[dt.datetime, dt.datetime],
                kind: str) -> Tuple[bool, bool, List[str]]:
    ok = False
    hard_fail = False
    notes: List[str] = []

    for raw in lines:
        t = ts_of(raw)
        if not t or t < w[0] or t > w[1]:
            continue
        L = raw.strip()

        if kind in ("Index", "SingleName"):
            if "Program is ending successfully" in L:
                ok = True
            m = re.search(r"Validation Error\(s\):\s*(\d+)", L)
            if m and int(m.group(1)) > 0:
                hard_fail = True
            if kind == "SingleName":
                mq = re.search(r"Missing Prices \(Quotable redcodes\)\s*:\s*(\d+)", L, re.I)
                if mq and int(mq.group(1)) > 0:
                    notes.append(f"[INFO] Missing Quotable prices: {mq.group(1)} (OK)")
                # Caution if explicitly clearable missing appears (rare in samples)
                mc = re.search(r"Missing Clearable Prices\s*:\s*(\d+)", L, re.I)
                if mc and int(mc.group(1)) > 0:
                    hard_fail = True
                    notes.append(f"[CAUTION] Missing Clearable prices: {mc.group(1)}")

        elif kind == "IdxOptEarlyLatest":
            if "Index Option Quotes sent" in L:
                ok = True

        elif kind == "IdxOptFinal":
            if "Final Summary" in L:
                ok = True  # presence indicates summary reached
            acc = re.search(r"Accepted Index Option quotes\s+(\d+)", L)
            rej = re.search(r"Rejected Index Option quotes\s+(\d+)", L)
            if acc:
                notes.append(f"[INFO] Accepted quotes: {acc.group(1)}")
            if rej:
                r = int(rej.group(1))
                notes.append(f"[INFO] Rejected quotes: {r}")
                if r > 0:
                    hard_fail = True

    return ok, hard_fail, notes

def status_from(lines: List[str],
                w: Tuple[dt.datetime, dt.datetime],
                now_london: dt.datetime,
                kind: str) -> Tuple[str, List[str]]:
    ok, fail, notes = scan_window(lines, w, kind)
    if ok and not fail:
        return OK, notes
    if now_london <= w[1] and not ok:
        return WAIT, notes
    return NOK, notes

# ---------------------------
# Build rows
# ---------------------------

def compute_rows(date_: dt.date, now_london: dt.datetime) -> Tuple[List[Dict], List[str]]:
    rows: List[Dict] = []
    footnotes: List[str] = []

    def windows_for(region: str, typ: str):
        if typ in ("Index", "SingleName"):
            return WINDOWS_AUD_SN if region.startswith("AUD") else WINDOWS_INDEX_SN
        else:
            return WINDOWS_IDX_OPT

    def win_london(region: str, t0: dt.time, t1: dt.time):
        return to_london_window(date_, region, t0, t1)

    for region in REGIONS:
        # Index + SN
        for typ in TYPES:
            W = windows_for(region, typ)
            early_srv = server_path(date_.isoformat(), region, typ, "Early")
            final_srv = server_path(date_.isoformat(), region, typ, "Final")
            early_lines = read_lines(early_srv)
            final_lines = read_lines(final_srv)

            e0 = win_london(region, *W["EarlyRun"])
            l10 = win_london(region, *W["Latest1"])
            l20 = win_london(region, *W["Latest2"])
            f0 = win_london(region, *W["Final"])

            kind = "SingleName" if typ == "SingleName" else "Index"
            s_e, n1 = status_from(early_lines, e0, now_london, kind)
            s_l1, n2 = status_from(early_lines, l10, now_london, kind)
            s_l2, n3 = status_from(early_lines, l20, now_london, kind)
            s_f, n4 = status_from(final_lines, f0, now_london, kind)

            for n in (n1 + n2 + n3 + n4):
                if "[INFO]" in n or "[CAUTION]" in n:
                    footnotes.append(f"{region}-{typ}: {n}")

            # NAS paths for links (locked)
            early_nas = nas_path(date_.isoformat(), region, typ, "Early")
            final_nas = nas_path(date_.isoformat(), region, typ, "Final")

            rows.append({
                "region": region.replace("forUS", ""),
                "subtype": f"{region}-{typ}",
                "status_early": s_e,
                "status_l1": s_l1,
                "status_l2": s_l2,
                "status_final": s_f,
                "early_nas": early_nas,   # used ONLY for SubmissionType hyperlink
                "logs_nas": final_nas,    # used ONLY in SubmissionLogs column
            })

        # Index Options row for EUR (extendable)
        if region in IDX_OPT_REGIONS:
            typ = "IndexOption"
            W = windows_for(region, typ)
            early_srv = server_path(date_.isoformat(), region, typ, "Early")      # PriceGeneration_{region}_EarlyRun.log
            summ_srv  = server_path(date_.isoformat(), region, typ, "Summary")    # SubmissionSummaryIDX_OPT_{region}.log

            early_lines = read_lines(early_srv)      # for Early/L1/L2
            summ_lines  = read_lines(summ_srv)       # for Final only

            e0 = win_london(region, *W["EarlyRun"])
            l10 = win_london(region, *W["Latest1"])
            l20 = win_london(region, *W["Latest2"])
            f0 = win_london(region, *W["Final"])

            s_e, n1 = status_from(early_lines, e0, now_london, "IdxOptEarlyLatest")
            s_l1, n2 = status_from(early_lines, l10, now_london, "IdxOptEarlyLatest")
            s_l2, n3 = status_from(early_lines, l20, now_london, "IdxOptEarlyLatest")
            s_f, n4 = status_from(summ_lines,  f0, now_london, "IdxOptFinal")

            for n in (n1 + n2 + n3 + n4):
                if "[INFO]" in n or "[CAUTION]" in n:
                    footnotes.append(f"{region}-IndexOption: {n}")

            # NAS hyperlinks: Early -> EarlyRun log, Logs -> SubmissionSummary
            early_nas = nas_path(date_.isoformat(), region, typ, "Early")
            logs_nas  = nas_path(date_.isoformat(), region, typ, "Summary")

            rows.append({
                "region": region.replace("forUS", ""),
                "subtype": f"{region}-IndexOption",
                "status_early": s_e,
                "status_l1": s_l1,
                "status_l2": s_l2,
                "status_final": s_f,
                "early_nas": early_nas,   # SubmissionType hyperlink
                "logs_nas": logs_nas,     # SubmissionLogs column
            })

    return rows, footnotes

# ---------------------------
# HTML rendering (LOCKED link behavior)
# ---------------------------

def td_center_big(s: str) -> str:
    return f'<td style="text-align:center;font-size:28px;">{html.escape(s)}</td>'

def unc_to_file_href(unc: str) -> str:
    # Convert \\server\share\path -> file://///server/share/path
    # Avoid backslashes in f-expression
    stripped = unc.lstrip("\\")
    href = "file://///" + stripped.replace("\\", "/").replace(" ", "%20")
    return href

def render_html(rows: List[Dict], notes: List[str]) -> str:
    head = """<!DOCTYPE html>
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
    body_rows = []
    for r in rows:
        region = html.escape(r["region"])
        subtype_text = html.escape(r["subtype"])  # link text
        early_href = unc_to_file_href(r["early_nas"])
        logs_href  = unc_to_file_href(r["logs_nas"])
        subtype_link = f'<a href="{early_href}">{subtype_text}</a>'
        logs_link = f'<a href="{logs_href}">{html.escape(os.path.basename(r["logs_nas"]))}</a>'

        row_html = (
            "<tr>"
            f"<td>{region}</td>"
            f"<td>{subtype_link}</td>"
            f"{td_center_big(r['status_early'])}"
            f"{td_center_big(r['status_l1'])}"
            f"{td_center_big(r['status_l2'])}"
            # FinalSubmission: NO hyperlink here—just the glyph (per your instruction)
            f"{td_center_big(r['status_final'])}"
            f"<td>{logs_link}</td>"
            "</tr>"
        )
        body_rows.append(row_html)

    notes_html = ""
    if notes:
        notes_html = "<h3>Notes</h3><ul>" + "".join(f"<li class='small'>{html.escape(n)}</li>" for n in notes) + "</ul>"

    tail = f"""
</tbody>
</table>
{notes_html}
</body>
</html>"""
    return head + "\n".join(body_rows) + tail

def render_text(rows: List[Dict], notes: List[str]) -> None:
    for r in rows:
        print(f"{r['region']:>3} | {r['subtype']:<28} | {r['status_early']} {r['status_l1']} {r['status_l2']} {r['status_final']}")
    if notes:
        print("\nNotes:")
        for n in notes:
            print(" -", n)

# ---------------------------
# MAIN
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

    # Server time is London local; use that as "now"
    now_london = dt.datetime.now()

    rows, notes = compute_rows(date_, now_london)

    if args.mode == "text":
        render_text(rows, notes)
    else:
        out = render_html(rows, notes)
        sys.stdout.buffer.write(out.encode("utf-8"))

if __name__ == "__main__":
    main()
