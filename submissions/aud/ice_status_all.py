import os
import argparse
from datetime import datetime, timedelta

# ---------------------------
# Configurable Paths
# ---------------------------
LOG_BASE = r"D:\DATA\logs\fixlink"

# NAS path base for Outlook hyperlinks
NAS_BASE = r"\\lonshr-emlogmgmt\CIBFIEMCRET_LOGS\vol2\fixlink\ws9100ppc00462"

# ---------------------------
# Region Configurations
# ---------------------------
REGIONS = {
    "AUD": {
        "local_offsets": {"morning": 10, "late1": 16, "late2": 16.25, "submission": 16.5},
        "submissions": ["Index", "SingleName"],  # No IndexOption for AUD
        "folder": "AUDforUS"
    },
    "SGD": {
        "local_offsets": {"morning": 10, "late1": 16, "late2": 16.25, "submission": 16.5},
        "submissions": ["Index", "SingleName"],  # No IndexOption
        "folder": "SGDforUS"
    },
    "EUR": {
        "local_offsets": {"morning": 10, "late1": 16, "late2": 16.25, "submission": 16.5},
        "submissions": ["Index", "SingleName", "IndexOption"],
        "folder": "EURforUS"
    },
    "USD": {
        "local_offsets": {"morning": 10, "late1": 16, "late2": 16.25, "submission": 16.5},
        "submissions": ["Index", "SingleName", "IndexOption"],
        "folder": "USD"
    }
}

# ---------------------------
# Parser Function
# ---------------------------
def parse_log_file(file_path):
    """Parse log for OK/NOK decision"""
    status = "TBC"
    details = []

    if not os.path.exists(file_path):
        return "TBC", ["Log missing"]

    try:
        with open(file_path, "r") as f:
            content = f.read()
        if "100% confirmed" in content and "Ended successfully" in content:
            status = "OK"
        elif "Ended" in content:
            status = "NOK"
        else:
            status = "TBC"

        if "GoodFiles" in content:
            details.append("GoodFiles present")
        if "Total Submitted" in content:
            details.append("Total Submitted found")
    except Exception as e:
        status = "NOK"
        details.append(f"Error reading log: {e}")

    return status, details


# ---------------------------
# Build Status Table
# ---------------------------
def build_status_table(date_str):
    table = []
    date_path = os.path.join(LOG_BASE, date_str, "ICEDIRECT")
    nas_date_path = os.path.join(NAS_BASE, date_str, "ICEDIRECT")

    for region, cfg in REGIONS.items():
        for sub in cfg["submissions"]:
            subdir = os.path.join(date_path, sub, cfg["folder"])
            nas_subdir = os.path.join(nas_date_path, sub, cfg["folder"])

            # Early Run log file
            log_file = os.path.join(subdir, f"PriceGeneration_{cfg['folder']}_EarlyRun.log")
            nas_file = os.path.join(nas_subdir, f"PriceGeneration_{cfg['folder']}_EarlyRun.log")

            status, details = parse_log_file(log_file)

            table.append({
                "Region": region,
                "Submission": f"{region} - {sub}",
                "EarlyRun": status,
                "Log": nas_file,
                "Details": details
            })
    return table


# ---------------------------
# Print Table
# ---------------------------
def print_status_table(table):
    print(f"{'Region':<6} | {'Submission':<25} | {'EarlyRun':<6} | Log File")
    print("-" * 90)
    for row in table:
        print(f"{row['Region']:<6} | {row['Submission']:<25} | {row['EarlyRun']:<6} | {row['Log']}")


# ---------------------------
# Main
# ---------------------------
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", required=True, help="Date in YYYY-MM-DD")
    args = parser.parse_args()

    status_table = build_status_table(args.date)
    print_status_table(status_table)
