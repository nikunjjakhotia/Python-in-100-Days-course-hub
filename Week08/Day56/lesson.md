# Day 56 – Project: Weather Dashboard CLI

## What You're Building
A command-line weather dashboard that fetches current conditions and a 3-day forecast for any city, then displays them in a formatted table.

---

## Learning Objectives
- Integrate everything from Week 8 into one complete program
- Handle missing API keys gracefully
- Format and display structured data in the terminal

---

## API Used
**Open-Meteo** — free, no API key required: `https://api.open-meteo.com/v1/forecast`

Geocoding to convert city names to coordinates:  
**Nominatim (OpenStreetMap)** — free, no key: `https://nominatim.openstreetmap.org/search`

---

## Project Spec

```
$ python weather.py London

Weather Dashboard – London, England, United Kingdom
────────────────────────────────────────────────────
Current:  18°C | Precipitation: 0.2mm | Wind: 14 km/h

3-Day Forecast:
  Date          Max°C   Min°C   Rain(mm)
  2026-04-26    19      12      0.5
  2026-04-27    17      11      2.1
  2026-04-28    21      13      0.0
```

---

## Implementation Guide

### Step 1 – Geocode the city
```python
def get_coordinates(city: str) -> tuple[float, float, str]:
    """Returns (lat, lon, display_name) or raises ValueError."""
```

### Step 2 – Fetch weather
```python
def get_weather(lat: float, lon: float) -> dict:
    """Calls Open-Meteo and returns raw JSON."""
```

### Step 3 – Parse & display
```python
def display_dashboard(city_name: str, weather: dict) -> None:
    """Formats and prints the dashboard."""
```

### Step 4 – Main entry point
```python
if __name__ == "__main__":
    import sys
    city = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else input("Enter city: ")
    ...
```

---

## Stretch Goals
- Add emoji weather icons based on WMO weather code
- Cache the last response in a `.json` file (skip the API call if < 10 min old)
- Support `--units imperial` flag for °F / mph

---

## Exercises
See `exercises.py`
