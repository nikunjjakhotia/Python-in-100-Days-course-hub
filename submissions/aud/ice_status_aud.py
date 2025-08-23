import os
import json
import argparse
from datetime import datetime

# ✅ Fixed NAS root for hyperlinks
NAS_ROOT = r"\\lonshr-emlogmgmt\CIBFIEMCRET_LOGS\vol2\fixlink\ws9100ppc00462"

# ✅ Server root for parsing logs
SERVER_ROOT = r"D:\DATA\logs\fixlink"

# Time windows (Sydney local time for AUD)
TIME_WINDOWS = {
    "EarlyRun": ("10:00", "10:15"),
    "Latest#1": ("16:00", "16:04"),
    "Latest#2": ("16:15", "16:19"),
    "FinalRun": ("16:30", "16:35")
}

def parse_log(file_path, run_type, region, submission_type):
    """Parse log file and return status + notes."""
    if not os.path.exists(file_path):
        return {"status": "Waiting", "notes": f"{region} {submission_type} {run_type} log missing"}

    status = "✅"
    notes = []
    try:
        with open(file_path, encoding="utf-8", errors="ignore") as f:
            for line in f:
                line_lower = line.lower()
                if "nok" in line_lower:
                    status = "NOK"
                if "missing curve" in line_lower or "clearable" in line_lower or "quotable" in line_lower:
                    ts = line.split()[0] if line.strip() else "UNKNOWN"
                    notes.append(f"[{region} - {submission_type} - {run_type}] {line.strip()} (TS={ts})")
    except Exception as e:
        status = "Error"
        notes.append(f"Error reading {file_path}: {e}")

    return {"status": status, "notes": notes}


def build_aud_status(date_str):
    """Build status for AUD Index + SingleName runs."""
    base_date = os.path.join(SERVER_ROOT, date_str, "ICEDIRECT")

    submissions = {
        "Index": {
            "EarlyRun": os.path.join(base_date, "Index", "AUDforUS", f"PriceGeneration_AUDforUS_EarlyRun.log"),
            "FinalRun": os.path.join(base_date, "Index", "AUDforUS", f"PriceGeneration_AUDforUS_FinalRun.log")
        },
        "SingleName": {
            "EarlyRun": os.path.join(base_date, "SingleName", "AUDforUS", f"PriceGeneration_AUDforUS_EarlyRun.log"),
            "FinalRun": os.path.join(base_date, "SingleName", "AUDforUS", f"PriceGeneration_AUDforUS_FinalRun.log")
        }
    }

    results = {"region": "AUDforUS", "date": date_str, "submissions": {}, "notes": []}

    for submission_type, paths in submissions.items():
        results["submissions"][submission_type] = {}
        for run_type, log_path in paths.items():
            parsed = parse_log(log_path, run_type, "AUDforUS", submission_type)

            # Build hyperlink for HTML later
            nas_path = log_path.replace(SERVER_ROOT, NAS_ROOT)
            parsed["hyperlink"] = f"file:///{nas_path.replace('\\', '/').replace(' ', '%20')}"

            results["submissions"][submission_type][run_type] = parsed["status"]
            results["notes"].extend(parsed["notes"])

    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", required=True, help="Date in YYYY-MM-DD")
    args = parser.parse_args()

    aud_status = build_aud_status(args.date)

    # Save JSON output
    out_file = f"AUDforUS_{args.date}.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(aud_status, f, indent=2)

    print(f"AUDforUS status written to {out_file}")
