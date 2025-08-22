# -*- coding: utf-8 -*-
"""
ICE status table – real parsing (server paths), NAS-only hyperlinks.
Time windows (local server time) – Index/SingleName vs IndexOption:

Index/SingleName:
  EarlyRun:   10:00–10:15
  Latest #1:  16:00–16:04
  Latest #2:  16:15–16:19
  Final:      16:30–16:35

IndexOption:
  EarlyRun:   10:00–10:15
  Latest #1:  16:00–16:04
  Latest #2:  16:10–16:19
  Final:      16:30–16:40  (from SubmissionSummaryIDX_OPT_*.log)

Important: parsing ALWAYS reads from SERVER paths under D:\DATA\logs\fixlink\...
Hyperlinks ALWAYS use NAS paths under \\lonshr-emlogmgmt\CIBFIEMCRET_LOGS\vol2\fixlink\ws9100ppc00462\...
"""

import argparse
import os
import re
from datetime import datetime, time

############################
# CONSTANTS (do not change)
############################
REGIONS = ["AUDforUS", "SGDforUS", "EURforUS", "USD"]
TYPES = ["Index", "SingleName"]  # IndexOption handled conditionally per region

# Root path to PARSE logs (server)
SERVER_ROOT = r"D:\DATA\logs\fixlink"

# Root path to LINK in HTML (NAS)
NAS_ROOT = r"\\lonshr-emlogmgmt\CIBFIEMCRET_LOGS\vol2\fixlink\ws9100ppc00462"

# Filenames
EARLY_FILE = "PriceGeneration_{region}_EarlyRun.log"
FINAL_FILE = "PriceGeneration_{region}_FinalRun.log"
IDXOPT_SUMMARY_FILE = "SubmissionSummaryIDX_OPT_{region}.log"

# Regions that have IndexOption rows
IDXOPT_REGIONS = ["EURforUS", "USD"]

# Column titles (keep timings)
COLS = [
    ("Region", None),
    ("SubmissionType", None),
    ("EarlyRun", "10:00 AM"),
    ("LatestRun #1", "4:00 PM"),
    ("LatestRun #2", "4:15 PM"),
    ("FinalSubmission", "4:30 PM"),
    ("SubmissionLogs", None),
]

# Time windows (inclusive) per type
def _win(h1,m1,h2,m2):
    return (time(h1,m1), time(h2,m2))

WINDOWS_IDX_SN = {
    "early": _win(10, 0, 10, 15),
    "latest1": _win(16, 0, 16, 4),
    "latest2": _win(16, 15, 16, 19),
    "final": _win(16, 30, 16, 35),
}
WINDOWS_IDXOPT = {
    "early": _win(10, 0, 10, 15),
    "latest1": _win(16, 0, 16, 4),
    "latest2": _win(16, 10, 16, 19),
    "final": _win(16, 30, 16, 40),  # from SubmissionSummary
}

# Timestamp patterns (handles [YYYY-MM-DD HH:MM:SS.mmm], YYYY/MM/DD HH:MM:SS, etc.)
TS_PAT = re.compile(r"(?P<dt>\d{4}[-/]\d{2}[-/]\d{2}\s+\d{2}:\d{2}:\d{2})")

OK_LINE = re.compile(r"Program is ending successfully", re.IGNORECASE)
ERROR_HINT = re.compile(r"\b(ERROR|Exception|Validation Error\(s\):\s*[1-9]\d*)\b", re.IGNORECASE)

# Missing/invalids parsing
MISSING_CLEARABLE_PAT = re.compile(r"Missing\s+Clearable\s+Prices\s*:\s*(\d+)", re.IGNORECASE)
MISSING_QUOTABLE_PAT = re.compile(r"Missing\s+Prices\s*\(Quotable.*?\)\s*:\s*(\d+)", re.IGNORECASE)
INVALID_SN_LINE = re.compile(r"Curve\s+\[.*?\]\s+.*?not sent\.\s*Invalid\s*!.*", re.IGNORECASE)

# IndexOption SubmissionSummary pats
IDXOPT_ACCEPTED = re.compile(r"Accepted Index Option quotes\s+(\d+)", re.IGNORECASE)
IDXOPT_REJECTED = re.compile(r"Rejected Index Option quotes\s+(\d+)", re.IGNORECASE)

################################
# Helpers
################################
def parse_args():
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", required=True, help="YYYY-MM-DD")
    ap.add_argument("--mode", choices=["html", "text"], default="html")
    return ap.parse_args()

def server_file(date_str, typ, region, kind):
    day = date_str
    base = os.path.join(SERVER_ROOT, day, "ICEDIRECT", typ, region)
    if typ == "IndexOption" and kind == "summary":
        return os.path.join(base, IDXOPT_SUMMARY_FILE.format(region=region))
    if kind == "early":
        return os.path.join(base, EARLY_FILE.format(region=region))
    if kind == "final":
        return os.path.join(base, FINAL_FILE.format(region=region))
    return None

def nas_link(date_str, typ, region, kind):
    day = date_str
    base = os.path.join(NAS_ROOT, day, "ICEDIRECT", typ, region)
    if typ == "IndexOption" and kind == "summary":
        return os.path.join(base, IDXOPT_SUMMARY_FILE.format(region=region))
    if kind == "early":
        return os.path.join(base, EARLY_FILE.format(region=region))
    if kind == "final":
        return os.path.join(base, FINAL_FILE.format(region=region))
    return "#"

def read_text(path):
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            return f.read()
    except Exception:
        return ""

def last_timestamp_in_text(txt):
    last = None
    for m in TS_PAT.finditer(txt):
        try:
            dt = datetime.strptime(m.group("dt"), "%Y-%m-%d %H:%M:%S")
        except ValueError:
            dt = datetime.strptime(m.group("dt"), "%Y/%m/%d %H:%M:%S")
        last = dt  # keep updating to end
    return last

def time_in_window(dt, start_t, end_t):
    if dt is None:
        return False
    tt = dt.time()
    return start_t <= tt <= end_t

def split_runs_early(txt):
    """
    Return list of (block_text, end_dt) for each run in EarlyRun file.
    A run is considered to end at an 'ending successfully' line; end_dt is the last timestamp seen in that block.
    """
    if not txt:
        return []
    lines = txt.splitlines()
    blocks = []
    cur = []
    for ln in lines:
        cur.append(ln)
        if OK_LINE.search(ln):
            block = "\n".join(cur)
            end_dt = last_timestamp_in_text(block)
            blocks.append((block, end_dt))
            cur = []
    # trailing partial (no successful end) is ignored for status
    return blocks

def classify_block(block_text):
    """
    Return "OK", "NOK", "WAIT", info_notes(list), caution_notes(list)
    WAIT only used by callers when no block in window; here we assume we got a finished block.
    """
    info, caution = [], []

    # SingleName invalids (informational unless clearable missing)
    invalids = INVALID_SN_LINE.findall(block_text)
    if invalids:
        info.extend(invalids)

    # Missing quotable (info)
    mq = MISSING_QUOTABLE_PAT.search(block_text)
    if mq and int(mq.group(1)) > 0:
        info.append(f"Missing Quotable Prices: {mq.group(1)}")

    # Missing clearable (caution -> NOK)
    mc = MISSING_CLEARABLE_PAT.search(block_text)
    if mc and int(mc.group(1)) > 0:
        caution.append(f"Missing Clearable Prices: {mc.group(1)}")

    # Hard errors
    if ERROR_HINT.search(block_text) or caution:
        return "NOK", info, caution

    # Otherwise OK
    return "OK", info, caution

def pick_status_from_early(early_txt, win):
    """
    From EarlyRun file text, find the last finished block whose end timestamp falls within 'win'.
    Return (status, info, caution). If none in window -> WAIT.
    """
    blocks = split_runs_early(early_txt)
    start_t, end_t = win
    best = None
    for block_text, end_dt in blocks:
        if end_dt and time_in_window(end_dt, start_t, end_t):
            if best is None or end_dt > best[1]:
                best = (block_text, end_dt)
    if not best:
        return "WAIT", [], []
    status, info, caution = classify_block(best[0])
    return status, info, caution

def status_for_final_idx_sn(final_txt, win):
    """
    FinalRun (Index/SingleName). We require a finished block within final window.
    """
    return pick_status_from_early(final_txt, win)  # same logic: finished blocks with end time in window

def status_for_idxopt_summary(sum_txt, win):
    """
    From SubmissionSummary (IndexOption) – if there is any activity in final window,
    mark OK if Accepted>0 and Rejected==0; NOK if Rejected>0; else WAIT.
    """
    if not sum_txt:
        return "WAIT", [], []
    # Is there any timestamp in final window?
    start_t, end_t = win
    any_in_window = False
    for m in TS_PAT.finditer(sum_txt):
        try:
            dt = datetime.strptime(m.group("dt"), "%Y-%m-%d %H:%M:%S")
        except ValueError:
            dt = datetime.strptime(m.group("dt"), "%Y/%m/%d %H:%M:%S")
        if time_in_window(dt, start_t, end_t):
            any_in_window = True
            break
    if not any_in_window:
        return "WAIT", [], []

    acc = 0
    rej = 0
    ma = list(IDXOPT_ACCEPTED.finditer(sum_txt))
    mr = list(IDXOPT_REJECTED.finditer(sum_txt))
    if ma:
        acc = sum(int(m.group(1)) for m in ma)
    if mr:
        rej = sum(int(m.group(1)) for m in mr)

    if rej > 0:
        return "NOK", [], [f"IndexOption rejected quotes: {rej}"]
    if acc > 0:
        return "OK", [], []
    # If we got here, activity but no counts? treat as WAIT conservatively
    return "WAIT", [], []

############################
# HTML rendering
############################
def badge(status):
    # ensure UTF-8 output; symbols are UTF-8
    if status == "OK":
        return "✅"
    if status == "NOK":
        return "❌"
    return "⏳"

def link(href, text):
    if not href or href == "#":
        return text
    return f'<a href="{href}">{text}</a>'

def render_html(rows):
    # Column heads with timings on new line where present
    ths = []
    for title, tm in COLS:
        if tm:
            ths.append(f"<th><div>{title}</div><div style='font-size:12px;opacity:.75'>{tm}</div></th>")
        else:
            ths.append(f"<th>{title}</th>")

    # build table
    trs = []
    for r in rows:
        trs.append(
            "<tr>"
            f"<td>{r['region']}</td>"
            f"<td>{r['subtype_html']}</td>"
            f"<td class='st'>{badge(r['early'])}</td>"
            f"<td class='st'>{badge(r['latest1'])}</td>"
            f"<td class='st'>{badge(r['latest2'])}</td>"
            f"<td class='st'>{badge(r['final'])}</td>"
            f"<td>{r['loglinks_html']}</td>"
            "</tr>"
        )

    # notes
    info_lines = []
    caution_lines = []
    for r in rows:
        for s in r.get("info_notes", []):
            info_lines.append(f"{r['subtype_plain']}: {s}")
        for s in r.get("caution_notes", []):
            caution_lines.append(f"{r['subtype_plain']}: {s}")

    notes_html = ""
    if info_lines or caution_lines:
        notes_html = "<div style='margin-top:14px'>"
        if info_lines:
            notes_html += "<div><b>Info (Quotable missing / invalid curves):</b><br>" + "<br>".join(info_lines) + "</div>"
        if caution_lines:
            notes_html += "<div style='margin-top:10px;color:#b91c1c'><b>Caution (Clearable missing / rejects):</b><br>" + "<br>".join(caution_lines) + "</div>"
        notes_html += "</div>"

    css = """
    <style>
      table{border-collapse:collapse;width:100%;font-family:Segoe UI,Arial,sans-serif}
      th,td{border:1px solid #ddd;padding:10px;text-align:left;vertical-align:middle}
      th{background:#f7f7f8}
      td.st{font-size:22px;text-align:center}
      a{color:#0b60d0;text-decoration:none} a:hover{text-decoration:underline}
    </style>
    """

    html = f"""<!doctype html>
<html><head<meta charset="utf-8">{css}</head>
<body>
<table>
<thead><tr>{''.join(ths)}</tr></thead>
<tbody>
{''.join(trs)}
</tbody>
</table>
{notes_html}
</body></html>"""
    return html

############################
# Row builder
############################
def build_rows(day):
    rows = []

    def add_row(region, typ, windows):
        subtype_plain = f"{region}-{ 'IDX_OPT' if typ=='IndexOption' else ('INDEX' if typ=='Index' else 'SN') }"
        subtype_html = link(nas_link(day, typ, region, "early"), subtype_plain)

        # Load texts
        early_txt = read_text(server_file(day, typ, region, "early")) if typ in ("Index","SingleName","IndexOption") else ""
        final_txt = ""
        sum_txt = ""
        if typ in ("Index", "SingleName"):
            final_txt = read_text(server_file(day, typ, region, "final"))
        else:  # IndexOption
            sum_txt = read_text(server_file(day, "IndexOption", region, "summary"))

        # statuses
        s_early, info_e, caut_e = pick_status_from_early(early_txt, windows["early"])
        s_l1, info_l1, caut_l1 = pick_status_from_early(early_txt, windows["latest1"])
        s_l2, info_l2, caut_l2 = pick_status_from_early(early_txt, windows["latest2"])

        if typ in ("Index", "SingleName"):
            s_final, info_f, caut_f = status_for_final_idx_sn(final_txt, windows["final"])
        else:
            s_final, info_f, caut_f = status_for_idxopt_summary(sum_txt, windows["final"])

        # links column
        logs_links = []
        logs_links.append(link(nas_link(day, typ, region, "early"), "EarlyRun"))
        if typ in ("Index","SingleName"):
            logs_links.append(link(nas_link(day, typ, region, "final"), "FinalRun"))
        else:
            logs_links.append(link(nas_link(day, "IndexOption", region, "summary"), "SubmissionSummary"))
        loglinks_html = " | ".join(logs_links)

        # notes aggregate
        info_notes = info_e + info_l1 + info_l2 + info_f
        caution_notes = caut_e + caut_l1 + caut_l2 + caut_f

        rows.append({
            "region": region.split("for")[0],  # display as AUD / SGD / EUR / USD
            "subtype_plain": subtype_plain,
            "subtype_html": subtype_html,
            "early": s_early,
            "latest1": s_l1,
            "latest2": s_l2,
            "final": s_final,
            "loglinks_html": loglinks_html,
            "info_notes": info_notes,
            "caution_notes": caution_notes,
        })

    # Order: AUD(Index, SN), SGD(Index, SN), EUR(Index, SN, IDX_OPT), USD(Index, SN, IDX_OPT)
    for r in ["AUDforUS", "SGDforUS", "EURforUS", "USD"]:
        # Index
        add_row(r, "Index", WINDOWS_IDX_SN)
        # SingleName
        add_row(r, "SingleName", WINDOWS_IDX_SN)
        # IndexOption where applicable
        if r in IDXOPT_REGIONS:
            add_row(r, "IndexOption", WINDOWS_IDXOPT)

    return rows

############################
# TEXT renderer (optional)
############################
def render_text(rows):
    def s(x): return {"OK":"OK","NOK":"NOK","WAIT":"WAIT"}[x]
    print("Region | SubmissionType | Early | L#1 | L#2 | Final | Logs")
    for r in rows:
        print(f"{r['region']} | {r['subtype_plain']} | {s(r['early'])} | {s(r['latest1'])} | {s(r['latest2'])} | {s(r['final'])} | {r['loglinks_html']}")

############################
# main
############################
if __name__ == "__main__":
    args = parse_args()
    rows = build_rows(args.date)

    if args.mode == "text":
        render_text(rows)
    else:
        html = render_html(rows)
        # Always write UTF-8 to stdout to preserve emoji
        import sys
        sys.stdout.buffer.write(html.encode("utf-8"))
