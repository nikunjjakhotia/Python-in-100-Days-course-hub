# Day 56 – Project: Weather Dashboard CLI
# Uses Open-Meteo (free, no API key) + Nominatim geocoding.

import requests
import time
from datetime import datetime


def get_coordinates(city: str) -> tuple:
    """Return (lat, lon, display_name) for a city name."""
    r = requests.get(
        "https://nominatim.openstreetmap.org/search",
        params={"q": city, "format": "json", "limit": 1},
        headers={"User-Agent": "PythonCourse/Day56"},
        timeout=10,
    )
    r.raise_for_status()
    results = r.json()
    if not results:
        raise ValueError(f"City not found: {city}")
    loc = results[0]
    return float(loc["lat"]), float(loc["lon"]), loc["display_name"]


def get_weather(lat: float, lon: float) -> dict:
    """Fetch current + 3-day forecast from Open-Meteo."""
    r = requests.get(
        "https://api.open-meteo.com/v1/forecast",
        params={
            "latitude":          lat,
            "longitude":         lon,
            "current":           "temperature_2m,precipitation,windspeed_10m",
            "daily":             "temperature_2m_max,temperature_2m_min,precipitation_sum",
            "forecast_days":     3,
            "timezone":          "auto",
        },
        timeout=10,
    )
    r.raise_for_status()
    return r.json()


def display_dashboard(city_name: str, data: dict) -> None:
    cur   = data["current"]
    daily = data["daily"]

    print(f"\nWeather Dashboard – {city_name}")
    print("─" * 60)
    print(f"Current:  {cur['temperature_2m']}°C | "
          f"Precipitation: {cur['precipitation']}mm | "
          f"Wind: {cur['windspeed_10m']} km/h\n")

    print(f"{'Date':<14} {'Max°C':>6} {'Min°C':>6} {'Rain(mm)':>10}")
    print("-" * 40)
    for i in range(len(daily["time"])):
        print(f"{daily['time'][i]:<14} "
              f"{daily['temperature_2m_max'][i]:>6.1f} "
              f"{daily['temperature_2m_min'][i]:>6.1f} "
              f"{daily['precipitation_sum'][i]:>10.1f}")


def main():
    import sys
    city = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else input("Enter city: ").strip()
    if not city:
        print("Please provide a city name.")
        return
    try:
        lat, lon, display = get_coordinates(city)
        time.sleep(1)   # Nominatim rate limit: 1 request/second
        weather = get_weather(lat, lon)
        display_dashboard(display, weather)
    except ValueError as e:
        print(e)
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")


if __name__ == "__main__":
    main()
