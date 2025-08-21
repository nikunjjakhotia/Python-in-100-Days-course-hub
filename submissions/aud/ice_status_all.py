import os
import argparse
from datetime import datetime

# Regions, submissions and their log paths
CONFIG = {
    "AUD": {
        "Index":       "ICEDIRECT/Index/AUDforUS/PriceGeneration_AUDforUS_{}.log",
        "SingleName":  "ICEDIRECT/SingleName/AUDforUS/PriceGeneration_AUDforUS_{}.log",
    },
    "SGD": {
        "Index":       "ICEDIRECT/Index/SGDforUS/PriceGeneration_SGDforUS_{}.log",
        "SingleName":  "ICEDIRECT/SingleName/SGDforUS/PriceGeneration_SGDforUS_{}.log",
    },
    "EUR": {
        "Index":       "ICEDIRECT/Index/EURforUS/PriceGeneration_EURforUS_{}.log",
        "SingleName":  "ICEDIRECT/SingleName/EURforUS/PriceGeneration_EURforUS_{}.log",
        "IndexOption": "ICEDIRECT/IndexOption/EURforUS/PriceGeneration_EURforUS_{}.log",
    },
    "USD": {
        "Index":       "ICEDIRECT/Index/USD/PriceGeneration_USD_{}.log",
        "SingleName":  "ICEDIRECT/SingleName/USD/PriceGeneration_USD_{}.log",
        "IndexOption": "ICEDIRECT/IndexOption/USD/PriceGeneration_USD_{}.log",
    },
}

SLOTS = ["EarlyRun", "Late1", "Late2", "Submission"]

BASE_NAS = r"\\lonshr-emlogmgmt\CIBFIEMCRET_LOGS\vol2\fixlink\ws9100ppc00462"

def build_status_table(date_str):
    table = []
    for region, submissions in CONFIG.items():
        for submission, path_pattern in submissions.items():
            row = {"Region": region, "Submission": submission}
            for slot in SLOTS:
                log_path = os.path.join(BASE_NAS, date_str, path_pattern.format(slot))
                if os.path.exists(log_path):   # server check
                    status = "TBC"  # placeholder until parser is added
                else:
                    status = "TBC"
                row[slot] = (status, log_path)
            table.append(row)
    return table

def print_text(table):
    header = f"{'Region':<6} | {'Submission':<22} | " + " | ".join([f"{slot:<10}" for slot in SLOTS])
    print(header)
    print("-" * len(header))
    for row in table:
        slots = " | ".join([f"{row[slot][0]:<10}" for slot in SLOTS])
        print(f"{row['Region']:<6} | {row['Submission']:<22} | {slots}")

def print_html(table):
    print("<table border='1' cellspacing='0' cellpadding='4' style='border-collapse:collapse;font-family:Calibri;font-size:12px;'>")
    print("<tr style='background-color:#f2f2f2;'><th>Region</th><th>Submission</th>" + "".join([f"<th>{slot}</th>" for slot in SLOTS]) + "</tr>")
    for row in table:
        print("<tr>")
        print(f"<td>{row['Region']}</td>")
        print(f"<td>{row['Submission']}</td>")
        for slot in SLOTS:
            status, log_path = row[slot]
            color = {"OK":"#c6efce","NOK":"#ffc7ce","TBC":"#e7e6e6"}.get(status,"#ffffff")
            print(f"<td style='background-color:{color};text-align:center;'><a href='{log_path}'>{status}</a></td>")
        print("</tr>")
    print("</table>")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", required=True, help="Date in YYYY-MM-DD")
    parser.add_argument("--mode", choices=["text","html"], default="text")
    args = parser.parse_args()

    table = build_status_table(args.date)

    if args.mode == "text":
        print_text(table)
    else:
        print_html(table)
