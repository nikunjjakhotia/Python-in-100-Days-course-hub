import argparse
import os
from datetime import datetime

# ------------------------------------------------------------
# Configuration
# ------------------------------------------------------------
REGIONS = [
    ("AUD", "AUDforUS", "Index"),
    ("EUR", "EURforUS", "Index"),
    ("SGD", "SGDforUS", "Index"),
    ("USD", "USD", "Index"),
    ("AUD", "AUDforUS", "SingleName"),
    ("EUR", "EURforUS", "SingleName"),
    ("SGD", "SGDforUS", "SingleName"),
    ("USD", "USD", "SingleName"),
    ("EUR", "EURforUS", "IndexOption"),
    ("USD", "USD", "IndexOption"),
]

NAS_BASE = r"\\lonshr-emlogmgmt\CIBFIEMCRET_LOGS\vol2\fixlink\ws9100ppc00462"

FINAL_RUN_FILES = {
    "Index": "PriceGeneration_{region}_FinalRun.log",
    "SingleName": "PriceGeneration_{region}_FinalRun.log",
    "IndexOption": "SubmissionSummaryIDX_OPT_{region}.log"
}

EARLY_RUN_FILES = {
    "Index": "PriceGeneration_{region}_EarlyRun.log",
    "SingleName": "PriceGeneration_{region}_EarlyRun.log",
    "IndexOption": "SubmissionSummaryIDX_OPT_{region}.log"
}

# ------------------------------------------------------------
# Helpers
# ------------------------------------------------------------
def make_nas_path(date_str, submission_type, region, kind="final"):
    """Build NAS path for logs"""
    date_folder = date_str
    if kind == "final":
        fname = FINAL_RUN_FILES[submission_type].format(region=region)
    else:
        fname = EARLY_RUN_FILES[submission_type].format(region=region)

    if submission_type == "Index":
        subdir = f"ICEDIRECT\\Index\\{region}"
    elif submission_type == "SingleName":
        subdir = f"ICEDIRECT\\SingleName\\{region}"
    else:
        subdir = f"ICEDIRECT\\IndexOption\\{region}"

    return os.path.join(NAS_BASE, date_folder, subdir, fname)


def status_icon(ok=True, pending=False):
    """Return ✅ ❌ ⏳ as HTML centered"""
    if pending:
        return '<td style="text-align:center; font-size:22px;">⏳</td>'
    if ok:
        return '<td style="text-align:center; font-size:22px;">✅</td>'
    return '<td style="text-align:center; font-size:22px;">❌</td>'


# ------------------------------------------------------------
# Build Table
# ------------------------------------------------------------
def build_table(date_str):
    rows = []
    for region_short, region, submission_type in REGIONS:
        early_log = make_nas_path(date_str, submission_type, region, kind="early")
        final_log = make_nas_path(date_str, submission_type, region, kind="final")

        row = {
            "Region": region_short,
            "SubmissionType": f"{region} - {submission_type}",
            "EarlyLog": early_log,
            "FinalLog": final_log,
            # Stub statuses for now
            "EarlyRun": "✅",
            "LatestRun1": "✅",
            "LatestRun2": "⏳",
            "FinalSubmission": "✅",
        }
        rows.append(row)
    return rows


# ------------------------------------------------------------
# Renderers
# ------------------------------------------------------------
def render_text(rows):
    header = (
        "Region | SubmissionType | EarlyRun (10:00 AM) "
        "| LatestRun #1 (4:00 PM) | LatestRun #2 (4:15 PM) "
        "| FinalSubmission (4:30 PM) | SubmissionLogs"
    )
    sep = "-" * len(header)
    print(header)
    print(sep)
    for r in rows:
        print(
            f"{r['Region']:<6} | {r['SubmissionType']:<25} | "
            f"{r['EarlyRun']:^10} | {r['LatestRun1']:^18} | {r['LatestRun2']:^18} | "
            f"{r['FinalSubmission']:^20} | {r['FinalLog']}"
        )


def render_html(rows):
    html = """
    <html>
    <head>
    <style>
        table { border-collapse: collapse; width: 100%; font-family: Arial, sans-serif; }
        th, td { border: 1px solid #ccc; padding: 6px; text-align: center; }
        th { background-color: #f2f2f2; }
        td { font-size: 14px; }
    </style>
    </head>
    <body>
    <table>
    <tr>
        <th>Region</th>
        <th>SubmissionType</th>
        <th>EarlyRun<br>(10:00 AM)</th>
        <th>LatestRun #1<br>(4:00 PM)</th>
        <th>LatestRun #2<br>(4:15 PM)</th>
        <th>FinalSubmission<br>(4:30 PM)</th>
        <th>SubmissionLogs</th>
    </tr>
    """
    for r in rows:
        html += "<tr>"
        html += f"<td>{r['Region']}</td>"
        html += f"<td><a href='{r['EarlyLog']}'>{r['SubmissionType']}</a></td>"

        # Status cells
        html += status_icon(ok=(r['EarlyRun']=="✅"), pending=(r['EarlyRun']=="⏳"))
        html += status_icon(ok=(r['LatestRun1']=="✅"), pending=(r['LatestRun1']=="⏳"))
        html += status_icon(ok=(r['LatestRun2']=="✅"), pending=(r['LatestRun2']=="⏳"))
        html += status_icon(ok=(r['FinalSubmission']=="✅"), pending=(r['FinalSubmission']=="⏳"))

        # Submission logs hyperlink
        html += f"<td><a href='{r['FinalLog']}'>FinalRun</a></td>"
        html += "</tr>\n"
    html += "</table></body></html>"
    return html


# ------------------------------------------------------------
# Main
# ------------------------------------------------------------
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", required=False, help="Date YYYY-MM-DD")
    parser.add_argument("--mode", choices=["text", "html"], default="text")
    args = parser.parse_args()

    date_str = args.date or datetime.today().strftime("%Y-%m-%d")
    rows = build_table(date_str)

    if args.mode == "text":
        render_text(rows)
    else:
        print(render_html(rows))
