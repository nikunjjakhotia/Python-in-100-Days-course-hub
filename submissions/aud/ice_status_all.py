#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
from datetime import datetime

NAS_BASE = r"\\lonshr-emlogmgmt\CIBFIEMCRET_LOGS\vol2\fixlink\ws9100ppc00462"

REGION_ORDER = ["AUDforUS", "SGDforUS", "EURforUS", "USD"]
TYPES_PER_REGION = {
    "AUDforUS": ["Index", "SingleName"],
    "SGDforUS": ["Index", "SingleName"],
    "EURforUS": ["Index", "SingleName", "IndexOption"],
    "USD":      ["Index", "SingleName", "IndexOption"],
}

# Use HTML entities to avoid encoding issues in Outlook/Windows
SYMBOL = {
    "ok": "&#x2705;",       # ✅
    "fail": "&#x274C;",     # ❌
    "pending": "&#x23F3;",  # ⏳
}

def early_log_filename(region: str, typ: str) -> str:
    # Early-run filename patterns (same base name across Index/SingleName/IndexOption; dir differs)
    return f"PriceGeneration_{region}_EarlyRun.log"

def final_log_filename(region: str, typ: str) -> str:
    if typ == "IndexOption":
        # IndexOption has a submission summary instead of FinalRun
        return f"SubmissionSummaryIDX_OPT_{region}.log"
    else:
        return f"PriceGeneration_{region}_FinalRun.log"

def build_nas_path(date_str: str, typ: str, region: str, filename: str) -> str:
    # Example: \\...\YYYY-MM-DD\ICEDIRECT\Index\AUDforUS\PriceGeneration_AUDforUS_FinalRun.log
    return f"{NAS_BASE}\\{date_str}\\ICEDIRECT\\{typ}\\{region}\\{filename}"

def submission_label(region: str, typ: str) -> str:
    # Display text in the first column
    if typ == "IndexOption":
        return f"{region} - IndexOption"
    elif typ == "SingleName":
        return f"{region} - SingleName"
    else:
        return f"{region} - Index"

def default_statuses():
    # Placeholder statuses; wire in real parsing later
    # EarlyRun ✓, LatestRun1 ✓, LatestRun2 ⏳, FinalSubmission ✓
    return (SYMBOL["ok"], SYMBOL["ok"], SYMBOL["pending"], SYMBOL["ok"])

def render_html(rows):
    html_head = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>ICE Submissions Status</title>
<style>
  body { font-family: Arial, Helvetica, sans-serif; }
  table { border-collapse: collapse; width: 100%; }
  th, td { border: 1px solid #ddd; padding: 10px; }
  th { background: #f4f6f8; font-weight: 600; }
  td.status { text-align: center; font-size: 24px; line-height: 1.2; }
  td a { text-decoration: none; }
  .sublog a { color: #0b57d0; }
  .subtype a { color: #0b57d0; font-weight: 600; }
</style>
</head>
<body>
<table>
<thead>
<tr>
  <th>Region</th>
  <th>SubmissionType</th>
  <th>EarlyRun<br>(10:00 AM)</th>
  <th>LatestRun #1<br>(4:00 PM)</th>
  <th>LatestRun #2<br>(4:15 PM)</th>
  <th>FinalSubmission<br>(4:30 PM)</th>
  <th>SubmissionLogs</th>
</tr>
</thead>
<tbody>
"""
    html_rows = []
    for r in rows:
        html_rows.append(f"""<tr>
  <td>{r['region']}</td>
  <td class="subtype"><a href="{r['early_link']}">{r['subtype_label']}</a></td>
  <td class="status">{r['early_status']}</td>
  <td class="status">{r['late1_status']}</td>
  <td class="status">{r['late2_status']}</td>
  <td class="status">{r['final_status']}</td>
  <td class="sublog"><a href="{r['final_link']}">{r['final_caption']}</a></td>
</tr>""")
    html_tail = """
</tbody>
</table>
</body>
</html>
"""
    return html_head + "\n".join(html_rows) + html_tail

def render_text(rows):
    # ASCII-safe fallback (not typically used now, but keeping it)
    def sym(s):
        return {"ok":"OK","fail":"X","pending":".."}[s]
    print("Region | SubmissionType | Early(10:00) | 4:00 | 4:15 | Final(4:30) | SubmissionLogs")
    print("-"*100)
    for r in rows:
        print(f"{r['region']:<6} | {r['subtype_label']:<24} | "
              f"{r['early_status_txt']:^5} | {r['late1_status_txt']:^4} | {r['late2_status_txt']:^4} | {r['final_status_txt']:^12} | "
              f"{r['final_link']}")

def build_rows(date_str: str):
    rows = []
    for region in REGION_ORDER:
        for typ in TYPES_PER_REGION[region]:
            # Build file names and UNC paths
            early_fname = early_log_filename(region, typ)
            final_fname = final_log_filename(region, typ)

            early_path = build_nas_path(date_str, typ, region, early_fname)
            final_path = build_nas_path(date_str, typ, region, final_fname)

            # Labels & captions
            subtype_lbl = submission_label(region, typ)
            final_cap = "FinalRun" if typ != "IndexOption" else "SubmissionSummary"

            # Status placeholders (wire real parsing later)
            e, l1, l2, fin = default_statuses()

            rows.append({
                "region": region.replace("forUS", ""),  # show AUD/SGD/EUR/USD in the Region column
                "subtype_label": subtype_lbl,
                "early_link": early_path,
                "final_link": final_path,
                "final_caption": final_cap,
                "early_status": e,
                "late1_status": l1,
                "late2_status": l2,
                "final_status": fin,
                # text-mode safe symbols
                "early_status_txt": "OK",
                "late1_status_txt": "OK",
                "late2_status_txt": "..",
                "final_status_txt": "OK",
            })
    return rows

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Render multi-region ICE submission status (Outlook HTML).")
    parser.add_argument("--date", required=False, help="Business date YYYY-MM-DD for NAS links (default=today)")
    parser.add_argument("--mode", choices=["html", "text"], default="html")
    args = parser.parse_args()

    if not args.date:
        args.date = datetime.now().strftime("%Y-%m-%d")

    rows = build_rows(args.date)

    if args.mode == "text":
        render_text(rows)
    else:
        # HTML to stdout, safe for redirection with correct encoding
        html = render_html(rows)
        import sys
        sys.stdout.buffer.write(html.encode("utf-8"))
