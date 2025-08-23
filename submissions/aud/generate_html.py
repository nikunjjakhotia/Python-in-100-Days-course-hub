import argparse
import json
from pathlib import Path
from datetime import datetime

def load_json(region: str, date: str):
    filename = f"ice_status_{region}_{date}.json"
    path = Path(filename)
    if not path.exists():
        return None
    with open(path, "r") as f:
        return json.load(f)

def render_html(region: str, date: str, data: dict):
    # Table header
    html = f"""
    <html>
    <head>
        <style>
            body {{ font-family: Arial, sans-serif; }}
            table {{ border-collapse: collapse; width: 100%; margin-bottom: 20px; }}
            th, td {{ border: 1px solid #ccc; padding: 6px 10px; text-align: left; }}
            th {{ background: #f2f2f2; }}
            .ok {{ color: green; font-weight: bold; }}
            .nok {{ color: red; font-weight: bold; }}
            .tbc {{ color: orange; font-weight: bold; }}
            .holiday {{ color: gray; font-style: italic; }}
            .notes {{ font-size: 14px; margin-top: 20px; }}
        </style>
    </head>
    <body>
        <h2>Status Report – {region} – {date}</h2>
        <table>
            <tr>
                <th>Run Type</th>
                <th>Status</th>
                <th>Log Time</th>
                <th>Log File</th>
            </tr>
    """

    for run in data.get("runs", []):
        status_class = run["status"].lower()
        status_text = run["status"]

        # hyperlink if available
        if "hyperlink" in run and run["hyperlink"]:
            link = f'<a href="{run["hyperlink"]}">View Log</a>'
        else:
            link = "-"
