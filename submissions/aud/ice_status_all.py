import os
import argparse

# --- Config ---
# UNC base to NAS (do not change slashes here; we’ll join parts below)
NAS_BASE = r"\\lonshr-emlogmgmt\CIBFIEMCRET_LOGS\vol2\fixlink\ws9100ppc00462"

# Regions and which product folders they have
REGIONS = {
    "AUD": {"folder": "AUDforUS", "products": ["Index", "SingleName"]},
    "SGD": {"folder": "SGDforUS", "products": ["Index", "SingleName"]},
    "EUR": {"folder": "EURforUS", "products": ["Index", "SingleName", "IndexOption"]},
    "USD": {"folder": "USD",      "products": ["Index", "SingleName", "IndexOption"]},
}

# Internal slot keys (avoid key collision with "Submission" column)
SLOT_KEYS = ("SLOT_MORNING", "SLOT_LATE1", "SLOT_LATE2", "SLOT_FINAL")
# Display names for Outlook/email (always show local names)
SLOT_HEADERS = (
    "Early run (10am)",
    "Latest run #1 (4pm)",
    "Latest run #2 (4:15pm)",
    "Submission (4:30pm)",
)

# Status -> background color (inline CSS for Outlook)
COLOR_MAP = {
    "OK":  "#c6efce",  # light green
    "NOK": "#ffc7ce",  # light red/amber
    "TBC": "#fff2cc",  # light yellow
    "HOLIDAY": "#d9d9d9",  # grey
}

def nas_log_path(date_str: str, product: str, region_folder: str, slot_key: str) -> str:
    """
    Build the NAS UNC path for the log file to hyperlink in the 'Submission' column.
    As per your requirement, this always points to the EarlyRun log.
    """
    # product folder name is exactly the product (Index / SingleName / IndexOption)
    # file name is always PriceGeneration_<RegionFolder>_EarlyRun.log
    fname = f"PriceGeneration_{region_folder}_EarlyRun.log"
    # Use os.path.join to keep backslashes consistent on Windows UNC
    return os.path.join(NAS_BASE, date_str, "ICEDIRECT", product, region_folder, fname)

def build_rows(date_str: str):
    """
    Build the table rows. Each row has:
      - Region (AUD/SGD/EUR/USD)
      - SubmissionTitle (e.g., 'AUDforUS - Index')
      - SubmissionLink (UNC path to EarlyRun log)
      - Four slot statuses: default to TBC (we’ll wire parsers later)
    """
    rows = []
    for region, cfg in REGIONS.items():
        region_folder = cfg["folder"]
        for product in cfg["products"]:
            submission_title = f"{region_folder} - {product}"
            link_path = nas_log_path(date_str, product, region_folder, "SLOT_MORNING")  # always EarlyRun in hyperlink

            row = {
                "Region": region,
                "SubmissionTitle": submission_title,
                "SubmissionLink": link_path,
                # default statuses; parsers will set OK/NOK later
                "SLOT_MORNING":  "TBC",
                "SLOT_LATE1":    "TBC",
                "SLOT_LATE2":    "TBC",
                "SLOT_FINAL":    "TBC",
            }
            rows.append(row)
    return rows

def print_text(rows):
    # widths
    w_region = 6
    w_subm = 28
    w_slot = 14

    header = (
        f"{'Region':<{w_region}} | "
        f"{'Submission':<{w_subm}} | "
        f"{SLOT_HEADERS[0]:<{w_slot}} | "
        f"{SLOT_HEADERS[1]:<{w_slot}} | "
        f"{SLOT_HEADERS[2]:<{w_slot}} | "
        f"{SLOT_HEADERS[3]:<{w_slot}}"
    )
    print(header)
    print("-" * len(header))
    for r in rows:
        print(
            f"{r['Region']:<{w_region}} | "
            f"{r['SubmissionTitle']:<{w_subm}} | "
            f"{r['SLOT_MORNING']:<{w_slot}} | "
            f"{r['SLOT_LATE1']:<{w_slot}} | "
            f"{r['SLOT_LATE2']:<{w_slot}} | "
            f"{r['SLOT_FINAL']:<{w_slot}}"
        )

def print_html(rows):
    # simple, Outlook-friendly inline styles
    print("<table border='1' cellspacing='0' cellpadding='4' "
          "style='border-collapse:collapse;font-family:Calibri;font-size:12px;'>")
    # Header
    print("<tr style='background-color:#f2f2f2;'>"
          "<th>Region</th>"
          "<th>Submission</th>"
          f"<th>{SLOT_HEADERS[0]}</th>"
          f"<th>{SLOT_HEADERS[1]}</th>"
          f"<th>{SLOT_HEADERS[2]}</th>"
          f"<th>{SLOT_HEADERS[3]}</th>"
          "</tr>")
    # Rows
    for r in rows:
        print("<tr>")
        print(f"<td>{r['Region']}</td>")
        # Submission column: hyperlink with text like "AUDforUS - Index"
        # Note: UNC links usually work as-is in Outlook; if needed, prefix with file://
        href = r['SubmissionLink']
        title = r['SubmissionTitle']
        print(f"<td><a href=\"{href}\">{title}</a></td>")

        # Four status cells with background color
        for key in SLOT_KEYS:
            status = r[key]
            bg = COLOR_MAP.get(status, "#ffffff")
            print(f"<td style='background-color:{bg};text-align:center;'>{status}</td>")
        print("</tr>")
    print("</table>")

if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Build multi-region ICE status table (skeleton)")
    ap.add_argument("--date", required=True, help="YYYY-MM-DD")
    ap.add_argument("--mode", choices=["text", "html"], default="text")
    args = ap.parse_args()

    rows = build_rows(args.date)

    if args.mode == "text":
        print_text(rows)
    else:
        print_html(rows)
