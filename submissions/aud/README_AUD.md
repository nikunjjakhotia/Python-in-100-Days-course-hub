# AUD Parser Prototype (Phase 1)

This package contains a minimal **AUD-only** parser prototype for ICEDIRECT logs.

## Files
- `ice_status_aud.py` — Python 3.11 script to parse AUD Index and SingleName logs for a specific time **slot**.
- `run_example.cmd` — Example command lines for Windows CMD using your environment’s Python path.

## Requirements
- Python 3.11 (you have it at `D:\apps\python\64\3.11.6\python.exe`).
- Access to daily log folders under `D:\Data\logs\fixlink\YYYY-MM-DD\ICEDIRECT\...` on the server.

## How it works
- For **10:00, 16:00, 16:15**: reads the *EarlyRun* log for each area (Index, SingleName).
- For **16:30**: reads the *FinalRun* log for each area.
- Captures the block whose first timestamp falls within **±3 minutes** of the target slot time (for FinalRun, captures the last end block).
- Determines status:
  - **OK** if: GoodFiles + totals match + 100% + "ending successfully".
  - **NOK** if: any ERROR/BadFiles/Skip/ending with error or success markers missing.
  - **TBC** if: no lines captured in the time window or file not found.
- Prints a one-line result per area with the file path used.

## Run Examples
Edit the date and slot as needed.

```
D:\apps\python\64\3.11.6\python.exe ice_status_aud.py --date 2025-08-20 --slot 10:00 --verbose
D:\apps\python\64\3.11.6\python.exe ice_status_aud.py --date today --slot 16:00
D:\apps\python\64\3.11.6\python.exe ice_status_aud.py --date today --slot 16:15
D:\apps\python\64\3.11.6\python.exe ice_status_aud.py --date today --slot 16:30 --verbose
```

## Notes
- The script tries two EarlyRun filename patterns to accommodate your sample paths:
  - `PriceGeneration_AUDforUS_EarlyRun.log`
  - `PriceGeneration_EURforUS_EarlyRun.log`
  Use whichever actually exists in your environment.
- FinalRun uses: `PriceGeneration_AUDforUS_FinalRun.log`.
- **HOLIDAY** handling is not included yet — we’ll add a small calendar file later.
- This is **Phase 1**: console-only output. Next phases will add state memory + HTML email.
