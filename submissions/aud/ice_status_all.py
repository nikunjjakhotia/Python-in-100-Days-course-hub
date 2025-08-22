# -*- coding: utf-8 -*-
"""
Real parsing for ICE submissions dashboard.

- EarlyRun (10:00), Latest #1 (16:00), Latest #2 (16:15) are parsed
  from *one* EarlyRun log per (Region, Type).
- FinalSubmission (16:30) parsed from FinalRun (Index/SingleName)
  or SubmissionSummary for IndexOption.
- Hyperlinks use NAS UNC paths; parsing uses server paths.

Status rules
------------
✅  if success AND no clearable-missing (quotable-missing allowed)
❌  if any clearable-missing OR explicit errors/rejections
⏳  if no matching block found for the time window / file not present

Missing curve notes
-------------------
Collect "WARN - Curve ... not sent. Invalid !" lines and whether the run
reported "Missing Prices (Quotable ...)" (>0) => INFO
If any "Missing Clearable Prices:" (>0)     => CAUTION (+ ❌ for that slot)

Author: (you)
"""

from __future__ import annotations
import argparse
import datetime as dt
import html
import os
import re
from typing import Dict, List, Optional, Tuple

# --------------------------
# Configuration (defaults)
# --------------------------

REGIONS = [
    ("AUDforUS", "AUD"),
    ("SGDforUS", "SGD"),
    ("EURforUS", "EUR"),
    ("USD",      "USD"),
]

TYPES_FOR_REGION = {
    # Always Index then SingleName; EUR / USD also IndexOption
    "AUDforUS": ["Index", "SingleName"],
    "SGDforUS": ["Index", "SingleName"],
    "EURforUS": ["Index", "SingleName", "IndexOption"],
    "USD":      ["Index", "SingleName", "IndexOption"],
}

# File name patterns (by Type)
EARLY_FILE = {
    "Index":       "PriceGeneration_{region}_EarlyRun.log",
    "SingleName":  "PriceGeneration_{region}_EarlyRun.log",
    "IndexOption": "PriceGeneration_{region}_EarlyRun.log",  # runs at ~16:00/16:10; early column likely ⏳
}

FINAL_FILE = {
    "Index":       "PriceGeneration_{region}_FinalRun.log",
    "SingleName":  "PriceGeneration_{region}_FinalRun.log",
    # IndexOption has no FinalRun; use submission summary file instead
}

IDX_OPT_SUMMARY_FILE = "SubmissionSummaryIDX_OPT_{region}.log"  # region: EURforUS / USD


# Time windows (local server time assumed in logs)
# We match blocks by end time (timestamp on "Program is ending successfully")
WINDOWS = {
    "EarlyRun":  (dt.time(9, 30),  dt.time(10, 30)),
    "Latest1":   (dt.time(15, 45), dt.time(16, 5)),
    "Latest2":   (dt.time(16, 5),  dt.time(16, 25)),
}

FINAL_TIME_HINT = (dt.time(16, 25), dt.time(16, 40))  # helpful for sanity checks, not strictly enforced


# --------------------------
# Utilities
# --------------------------

def make_server_path(server_root: str, day: dt.date, typ: str, region: str, filename: str) -> str:
    # D:\DATA\logs\fixlink\YYYY-MM-DD\ICEDIRECT\Type\Region\filename
    return os.path.join(
        server_root,
        day.strftime("%Y-%m-%d"),
        "ICEDIRECT",
        typ,
        region,
        filename,
    )

def make_nas_path(nas_root: str, nas_host: str, day: dt.date, typ: str, region: str, filename: str) -> str:
    # \\lonshr-emlogmgmt\CIBFIEMCRET_LOGS\vol2\fixlink\ws9100ppc00462\YYYY-MM-DD\ICEDIRECT\Type\Region\filename
    # Use forward slashes in href for HTML escaping convenience, but UNC works either way.
    parts = [nas_root, nas_host, day.strftime("%Y-%m-%d"), "ICEDIRECT", typ, region, filename]
    # Ensure UNC slashes
    return "\\".join(parts)

def read_text(path: str) -> Optional[str]:
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as f:
            return f.read()
    except FileNotFoundError:
        return None

_TIMESTAMP = re.compile(r"(?P<dt>\d{4}[/\-]\d{2}[/\-]\d{2}\s+\d{2}:\d{2}:\d{2})")
_SUCCESS_LINE = re.compile(r"Program is ending successfully", re.IGNORECASE)
_VALIDATION_ERRS = re.compile(r"Validation Error\(s\)\s*:\s*(\d+)", re.IGNORECASE)
MISSING_CLEARABLE = re.compile(r"Missing\s+Clearable\s+Prices\s*:\s*(\d+)", re.IGNORECASE)
MISSING_QUOTABLE = re.compile(r"Missing\s+Prices\s*\(Quotable.*?\)\s*:\s*(\d+)", re.IGNORECASE)
MISSING_GENERIC   = re.compile(r"Missing\s+Prices\s*:\s*(\d+)", re.IGNORECASE)
WARN_CURVE_LINE   = re.compile(r"^\s*[\[\(]?\d{4}.+?WARN\s*-\s*Curve\s*\[.+?not sent\. Invalid !.*$", re.IGNORECASE | re.MULTILINE)

def parse_timestamp_from_line(line: str) -> Optional[dt.datetime]:
    m = _TIMESTAMP.search(line)
    if not m:
        return None
    raw = m.group("dt").replace("-", "/")
    try:
        return dt.datetime.strptime(raw, "%Y/%m/%d %H:%M:%S")
    except ValueError:
        return None

def split_runs_early(log_text: str) -> List[Tuple[dt.datetime, str]]:
    """
    Return list of (end_time, block_text) for each run in an EarlyRun log.
    A run ends where we see 'Program is ending successfully'.
    """
    lines = log_text.splitlines()
    blocks: List[Tuple[dt.datetime, str]] = []
    acc: List[str] = []
    last_cut = 0
    for i, line in enumerate(lines):
        acc.append(line)
        if _SUCCESS_LINE.search(line):
            ts = parse_timestamp_from_line(line)
            if ts is None:
                # try the previous line for timestamp if needed
                for back in range(1, 4):
                    if i - back >= 0:
                        ts = parse_timestamp_from_line(lines[i - back])
                        if ts:
                            break
            if ts is None:
                # fallback: skip this block
                acc = []
                last_cut = i + 1
                continue
            # flush block
            block_text = "\n".join(lines[last_cut:i + 1])
            blocks.append((ts, block_text))
            acc = []
            last_cut = i + 1
    return blocks

def classify_block_status(block_text: str, submission_type: str) -> Tuple[str, Dict[str, int], List[str], List[str]]:
    """
    Return (status_emoji, counters, info_lines, caution_lines)

    counters: {
        'validation_errors': int,
        'missing_clearable': int or 0,
        'missing_quotable': int or 0,
        'missing_generic': int or 0
    }

    - If missing_clearable > 0 => ❌ and CAUTION.
    - Else if validation_errors > 0 => ❌.
    - Else ✅.
    - info_lines will include WARN curve lines when quotable missing > 0.
    """
    def _int(m, idx=1):
        try:
            return int(m.group(idx))
        except Exception:
            return 0

    val_err = _int(_VALIDATION_ERRS.search(block_text) or re.match(r"$^", ""))
    miss_clr = _int(MISSING_CLEARABLE.search(block_text) or re.match(r"$^", ""))
    miss_qtb = _int(MISSING_QUOTABLE.search(block_text) or re.match(r"$^", ""))
    miss_gen = _int(MISSING_GENERIC.search(block_text) or re.match(r"$^", ""))

    info_lines: List[str] = []
    caution_lines: List[str] = []

    # Harvest WARN curve lines to display under notes
    warn_lines = WARN_CURVE_LINE.findall(block_text) or []
    # If clearable missing, mark all warn lines as CAUTION; otherwise, if quotable missing > 0, mark as INFO
    if miss_clr > 0:
        caution_lines.extend(warn_lines)
    elif miss_qtb > 0:
        info_lines.extend(warn_lines)

    if miss_clr > 0 or val_err > 0:
        status = "❌"
    else:
        status = "✅"

    return status, {
        "validation_errors": val_err,
        "missing_clearable": miss_clr,
        "missing_quotable": miss_qtb,
        "missing_generic": miss_gen,
    }, info_lines, caution_lines

def pick_block_for_window(blocks: List[Tuple[dt.datetime, str]], day: dt.date, window: Tuple[dt.time, dt.time]) -> Optional[Tuple[dt.datetime, str]]:
    start_dt = dt.datetime.combine(day, window[0])
    end_dt   = dt.datetime.combine(day, window[1])
    # pick the last successful run within the window
    candidates = [(ts, blk) for (ts, blk) in blocks if start_dt <= ts <= end_dt]
    if not candidates:
        return None
    candidates.sort(key=lambda x: x[0])
    return candidates[-1]

# ---- FinalRun (Index/SingleName) ----

FINAL_SUCCESS = re.compile(r"Program is ending successfully", re.IGNORECASE)

def parse_final_status_index_sn(text: Optional[str]) -> Tuple[str, List[str], List[str]]:
    """
    Return (status_emoji, info_lines, caution_lines).
    """
    if not text:
        return "⏳", [], []
    # Look at the whole file last block (assume last success is the final run we care about)
    blocks = split_runs_early(text)
    if not blocks:
        return "⏳", [], []
    ts, blk = blocks[-1]
    status, counters, info_lines, caution_lines = classify_block_status(blk, "Index/SingleName")
    return status, info_lines, caution_lines

# ---- Submission Summary (IndexOption final) ----

REJ_COUNTS = re.compile(r"Rejected\s+Index\s+Option\s+quotes\s+(\d+)", re.IGNORECASE)
ACC_COUNTS = re.compile(r"Accepted\s+Index\s+Option\s+quotes\s+(\d+)", re.IGNORECASE)

def parse_idxopt_final_from_summary(text: Optional[str]) -> str:
    if not text:
        return "⏳"
    # Choose final summary near 16:35
    rej = 0
    acc = 0
    # take the last numbers in the file
    for m in REJ_COUNTS.finditer(text):
        try:
            rej = int(m.group(1))
        except:
            pass
    for m in ACC_COUNTS.finditer(text):
        try:
            acc = int(m.group(1))
        except:
            pass
    if rej > 0:
        return "❌"
    # If accepted > 0 and we see "The settlement window is CLOSED", call it good
    if acc > 0 and "settlement window is CLOSED" in text:
        return "✅"
    # otherwise still waiting
    return "⏳"

# --------------------------
# HTML Rendering
# --------------------------

CSS = """
<style>
  body { font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif; margin: 24px; }
  table { border-collapse: collapse; width: 100%; }
  th, td { border: 1px solid #e5e7eb; padding: 10px 12px; }
  th { background: #f9fafb; text-align: center; font-weight: 600; }
  td.center { text-align: center; vertical-align: middle; }
  .big { font-size: 24px; line-height: 1; }
  a { text-decoration: none; color: #065f46; }
  .logs a { color: #1f2937; }
  .label { font-weight: 600; }
  .notes { margin-top: 20px; padding: 12px; background: #f9fafb; border: 1px solid #e5e7eb; border-radius: 8px; }
  .note-title { font-weight: 700; margin-bottom: 8px; }
  .note-row { margin-bottom: 10px; }
  .tag { display:inline-block; font-size: 12px; padding: 2px 6px; border-radius: 999px; margin-right: 8px; }
  .info { background:#ecfeff; border:1px solid #a5f3fc; }
  .caution { background:#fff7ed; border:1px solid #fdba74; }
  .mono { font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace; font-size:12px; }
  .nowrap { white-space: nowrap; }
  .two-line { white-space: pre-line; }
</style>
"""

def render_html(rows: List[Dict], notes: List[Dict]) -> str:
    # Column headers with times on new line
    headers = [
        "Region",
        "SubmissionType",
        "EarlyRun\n(10:00 AM)",
        "LatestRun #1\n(4:00 PM)",
        "LatestRun #2\n(4:15 PM)",
        "FinalSubmission\n(4:30 PM)",
        "SubmissionLogs",
    ]

    def cell_status(emoji: str) -> str:
        return f'<td class="center big">{html.escape(emoji)}</td>'

    # Build table rows
    tr_html = []
    for r in rows:
        region = html.escape(r["region_label"])
        sub_type_label = html.escape(r["submission_type_label"])
        sub_href = r["early_href"]
        logs_label = html.escape(r["logs_label"])
        logs_href = r["logs_href"]

        tr = []
        tr.append(f'<td class="center">{region}</td>')
        tr.append(f'<td class="center"><a class="label" href="{html.escape(sub_href)}" target="_blank">{sub_type_label}</a></td>')
        tr.append(cell_status(r["early_status"]))
        tr.append(cell_status(r["latest1_status"]))
        tr.append(cell_status(r["latest2_status"]))
        tr.append(cell_status(r["final_status"]))
        tr.append(f'<td class="center logs"><a class="mono" href="{html.escape(logs_href)}" target="_blank">{logs_label}</a></td>')
        tr_html.append("<tr>" + "".join(tr) + "</tr>")

    # Notes section
    notes_html_parts = []
    if notes:
        notes_html_parts.append('<div class="notes">')
        notes_html_parts.append('<div class="note-title">Notes (missing curves and run details)</div>')
        for n in notes:
            head = f'{html.escape(n["region_label"])} – {html.escape(n["submission_type_label"])}'
            notes_html_parts.append(f'<div class="note-row"><div class="label">{head}</div>')
            if n["info_lines"]:
                notes_html_parts.append('<div class="tag info">INFO (Quotable missing)</div>')
                notes_html_parts.append("<pre class='mono'>" + html.escape("\n".join(n["info_lines"])) + "</pre>")
            if n["caution_lines"]:
                notes_html_parts.append('<div class="tag caution">CAUTION (Clearable missing)</div>')
                notes_html_parts.append("<pre class='mono'>" + html.escape("\n".join(n["caution_lines"])) + "</pre>")
            notes_html_parts.append("</div>")
        notes_html_parts.append("</div>")

    # Assemble
    thead = "<thead><tr>" + "".join(f'<th class="two-line">{html.escape(h)}</th>' for h in headers) + "</tr></thead>"
    tbody = "<tbody>" + "\n".join(tr_html) + "</tbody>"
    html_doc = f"""<!doctype html>
<html>
<head>
<meta charset="UTF-8">{CSS}
<title>ICE Submissions Status</title>
</head>
<body>
<table>
{thead}
{tbody}
</table>
{''.join(notes_html_parts)}
</body>
</html>"""
    return html_doc

# --------------------------
# Orchestration
# --------------------------

def build_rows(day: dt.date, server_root: str, nas_root: str, nas_host: str) -> Tuple[List[Dict], List[Dict]]:
    rows: List[Dict] = []
    notes: List[Dict] = []

    # Precompute time windows
    w_early  = WINDOWS["EarlyRun"]
    w_l1     = WINDOWS["Latest1"]
    w_l2     = WINDOWS["Latest2"]

    for region, label in REGIONS:
        for typ in TYPES_FOR_REGION[region]:
            # File names (server + NAS)
            early_name = EARLY_FILE[typ].format(region=region)
            early_server = make_server_path(server_root, day, typ, region, early_name)
            early_nas    = make_nas_path(nas_root, nas_host, day, typ, region, early_name)

            # SubmissionLogs column (FinalRun or Summary link)
            if typ != "IndexOption":
                final_name = FINAL_FILE[typ].format(region=region)
                final_server = make_server_path(server_root, day, typ, region, final_name)
                final_nas    = make_nas_path(nas_root, nas_host, day, typ, region, final_name)
                logs_label   = "FinalRun"
                logs_href    = final_nas
            else:
                summ_name = IDX_OPT_SUMMARY_FILE.format(region=region)
                final_server = make_server_path(server_root, day, typ, region, summ_name)
                final_nas    = make_nas_path(nas_root, nas_host, day, typ, region, summ_name)
                logs_label   = "SubmissionSummary"
                logs_href    = final_nas

            # Parse early log (for 10:00 / 16:00 / 16:15)
            early_text = read_text(early_server)
            if early_text:
                blocks = split_runs_early(early_text)
            else:
                blocks = []

            def status_for_window(win) -> Tuple[str, List[str], List[str]]:
                pick = pick_block_for_window(blocks, day, win)
                if not pick:
                    return "⏳", [], []
                ts, blk = pick
                status, counters, info_lines, caution_lines = classify_block_status(blk, typ)
                return status, info_lines, caution_lines

            early_status, early_info, early_caution = status_for_window(w_early)
            l1_status,    l1_info,    l1_caution    = status_for_window(w_l1)
            l2_status,    l2_info,    l2_caution    = status_for_window(w_l2)

            # Final status
            if typ != "IndexOption":
                final_text = read_text(final_server)
                final_status, fin_info, fin_caution = parse_final_status_index_sn(final_text)
            else:
                final_status = parse_idxopt_final_from_summary(read_text(final_server))
                fin_info, fin_caution = [], []

            # Row label & hyperlink in SubmissionType cell (to EarlyRun NAS path)
            subtype_label = f"{region}-{('INDEX' if typ=='Index' else 'SINGLENAME' if typ=='SingleName' else 'INDEXOPTION')}"

            row = {
                "region_label": label,
                "submission_type_label": subtype_label,
                "early_status":   early_status,
                "latest1_status": l1_status,
                "latest2_status": l2_status,
                "final_status":   final_status,
                "early_href":     early_nas,
                "logs_label":     logs_label,
                "logs_href":      logs_href,
            }
            rows.append(row)

            # Notes aggregation (only include if we actually captured lines)
            n_info = list(dict.fromkeys(early_info + l1_info + l2_info + fin_info))  # dedupe
            n_caut = list(dict.fromkeys(early_caution + l1_caution + l2_caution + fin_caution))
            if n_info or n_caut:
                notes.append({
                    "region_label": label,
                    "submission_type_label": subtype_label,
                    "info_lines": n_info,
                    "caution_lines": n_caut,
                })

    return rows, notes

# --------------------------
# CLI
# --------------------------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", required=True, help="YYYY-MM-DD")
    ap.add_argument("--server-root", default=r"D:\DATA\logs\fixlink")
    ap.add_argument("--nas-root", default=r"\\lonshr-emlogmgmt\CIBFIEMCRET_LOGS\vol2\fixlink")
    ap.add_argument("--nas-host", default=r"ws9100ppc00462")
    ap.add_argument("--mode", choices=["html", "text"], default="html")
    args = ap.parse_args()

    day = dt.datetime.strptime(args.date, "%Y-%m-%d").date()
    rows, notes = build_rows(day, args.server_root, args.nas_root, args.nas_host)

    if args.mode == "text":
        # simple text (fallback)
        for r in rows:
            print(f"{r['region_label']:>3} | {r['submission_type_label']:<24} | "
                  f"{r['early_status']} | {r['latest1_status']} | {r['latest2_status']} | {r['final_status']} | {r['logs_label']}")
        if notes:
            print("\nNOTES:")
            for n in notes:
                print(f"- {n['region_label']} – {n['submission_type_label']}")
                if n["info_lines"]:
                    print("  INFO:")
                    for line in n["info_lines"]:
                        print("   ", line)
                if n["caution_lines"]:
                    print("  CAUTION:")
                    for line in n["caution_lines"]:
                        print("   ", line)
    else:
        html_out = render_html(rows, notes)
        import sys
        sys.stdout.buffer.write(html_out.encode("utf-8"))

if __name__ == "__main__":
    main()
