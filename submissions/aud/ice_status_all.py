#!/usr/bin/env python3
import os
import re
import argparse
from datetime import datetime

# ---------- Parsing Functions ----------

def parse_index_sn_log(path):
    """
    Parse Index or SingleName FinalRun log and return (status, info_list).
    Status = "✅" | "❌" | "⏳"
    """
    if not os.path.exists(path):
        return "⏳", []

    with open(path, encoding="utf-8", errors="ignore") as f:
        text = f.read()

    info = []

    if "Program is ending successfully" in text:
        # Validation check
        if "Validation Error(s): 0" not in text:
            return "❌", [f"Validation errors found in {os.path.basename(path)}"]

        # Missing prices
        m = re.search(r"Missing Prices\s*=\s*(\d+)", text)
        if m and int(m.group(1)) > 0:
            if "Quotable" in text:  # allowed but must note
                info.append(f"Quotable missing prices in {os.path.basename(path)}")
                return "✅", info
            else:  # clearable missing → failure
                return "❌", [f"Clearable missing prices in {os.path.basename(path)}"]

        return "✅", []

    elif "Program is ending with error" in text:
        return "❌", [f"Error termination in {os.path.basename(path)}"]

    return "⏳", []


def parse_idxopt_summary(path):
    """
    Parse IndexOption SubmissionSummary log and return (status, info_list).
    """
    if not os.path.exists(path):
        return "⏳", []

    with open(path, encoding="utf-8", errors="ignore") as f:
        text = f.read()

    if "Final Summary" not in text:
        return "⏳", []

    if "Rejected Index Option quotes        0" in text:
        return "✅", []
    else:
        return "❌", [f"Rejected quotes in {os.path.basename(path)}"]


# ---------- Rendering Functions ----------

def render_html(rows, info_notes):
    table = """
    <html><head><meta charset="UTF-8">
    <style>
    table { border-collapse: collapse; width: 100%; font-family: Arial; }
    th, td { border: 1px solid #999; padding: 8px; text-align: center; }
    th { background-color: #eee; }
    .big { font-size: 1.5em; }
    </style></head><body>
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
    for row in rows:
        table += "<tr>"
        for i, col in enumerate(row):
            cls = " class='big'" if i in (2,3,4,5) else ""
            table += f"<td{cls}>{col}</td>"
        table += "</tr>"
    table += "</table>"

    if info_notes:
        table += "<h3>ℹ️ Info / Caution Notes</h3><ul>"
        for note in info_notes:
            table += f"<li>{note}</li>"
        table += "</ul>"

    table += "</body></html>"
    return table


def render_text(rows, info_notes):
    # crude plain text fallback
    header = ["Region","SubmissionType","EarlyRun (10:00 AM)",
              "LatestRun #1 (4:00 PM)","LatestRun #2 (4:15 PM)",
              "FinalSubmission (4:30 PM)","SubmissionLogs"]
    col_widths = [max(len(str(x)) for x in [h]+[r[i] for r in rows]) for i,h in enumerate(header)]
    fmt = " | ".join("{:<" + str(w) + "}" for w in col_widths)

    out = fmt.format(*header) + "\n" + "-+-".join("-"*w for w in col_widths) + "\n"
    for r in rows:
        out += fmt.format(*r) + "\n"

    if info_notes:
        out += "\nℹ️ Info / Caution Notes:\n"
        for note in info_notes:
            out += f"- {note}\n"

    return out


# ---------- Main ----------

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", required=True, help="Date in YYYY-MM-DD format")
    parser.add_argument("--mode", choices=["html","text"], default="text")
    args = parser.parse_args()

    # Example file mapping (you’d replace with your real NAS paths)
    regions = [
        ("AUD","Index","PriceGeneration_AUDforUS_FinalRun.log"),
        ("AUD","SingleName","PriceGeneration_AUDforUS_FinalRun.log"),
        ("SGD","Index","PriceGeneration_SGDforUS_FinalRun.log"),
        ("SGD","SingleName","PriceGeneration_SGDforUS_FinalRun.log"),
        ("EUR","Index","PriceGeneration_EURforUS_FinalRun.log"),
        ("EUR","SingleName","PriceGeneration_EURforUS_FinalRun.log"),
        ("EUR","IndexOption","SubmissionSummaryIDX_OPT_EURforUS.log"),
        ("USD","Index","PriceGeneration_USD_FinalRun.log"),
        ("USD","SingleName","PriceGeneration_USD_FinalRun.log"),
        ("USD","IndexOption","SubmissionSummaryIDX_OPT_USD.log"),
    ]

    rows = []
    info_notes = []

    for region,stype,filename in regions:
        path = filename  # TODO: stitch with NAS root + args.date
        if "IndexOption" in stype:
            status, notes = parse_idxopt_summary(path)
        else:
            status, notes = parse_index_sn_log(path)

        info_notes.extend(notes)

        # For now: EarlyRun/LR1/LR2 are stubbed as "✅"
        row = [
            region,
            f"{region}-{stype}",  # this could be hyperlinked like before
            "✅",
            "✅",
            "⏳",
            status,
            path
        ]
        rows.append(row)

    # Render
    if args.mode == "html":
        import sys
        html = render_html(rows, info_notes)
        sys.stdout.buffer.write(html.encode("utf-8"))
    else:
        print(render_text(rows, info_notes))


if __name__ == "__main__":
    main()
