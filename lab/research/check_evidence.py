#!/usr/bin/env python3
"""Check the notes' arithmetic against supplied frozen evidence; never fetch or fit a model."""
import argparse
import csv
import json
import math
import re
from collections import defaultdict
from decimal import Decimal
from pathlib import Path
from statistics import mean

ANNUAL = {
    "2018": (52, 28.81, 23.67, 17.9, 57.7),
    "2019": (52, 33.46, 26.03, 22.2, 71.2),
    "2020": (52, 27.42, 23.07, 15.9, 82.7),
    "2021": (53, 27.57, 21.27, 22.8, 86.8),
    "2022": (52, 32.31, 19.12, 40.8, 80.8),
    "2023": (52, 30.98, 19.44, 37.2, 82.7),
    "2024": (52, 34.27, 20.41, 40.4, 76.9),
    "2025": (52, 33.19, 15.63, 52.9, 82.7),
    "2026": (46, 26.07, 15.25, 41.5, 82.6),
    "All": (463, 30.50, 20.50, 32.8, 78.2),
}
CURVE = {
    "2026-11": ("3.393", "3.026", "-0.367"),
    "2026-12": ("3.980", "3.370", "-0.610"),
    "2027-01": ("4.391", "3.752", "-0.639"),
    "2027-02": ("3.959", "3.428", "-0.531"),
    "2027-03": ("3.155", "2.763", "-0.392"),
    "2027-04": ("2.942", "2.664", "-0.278"),
    "2027-05": ("2.917", "2.693", "-0.224"),
    "2027-06": ("3.046", "2.852", "-0.194"),
    "2027-07": ("3.255", "3.095", "-0.160"),
}


def check_storage(path):
    with path.open(encoding="utf-8", newline="") as handle:
        raw = list(csv.DictReader(handle))
    dates = [row["week"] for row in raw]
    if dates != sorted(set(dates)) or (dates[0], dates[-1]) != ("2018-01-05", "2026-11-13"):
        raise ValueError("Evidence has different dates from the cited replay")
    groups = defaultdict(list)
    for row in raw:
        parsed = {field: float(row[field]) for field in ("forecast", "baseline", "actual", "low", "high")}
        if not all(math.isfinite(value) for value in parsed.values()) or parsed["low"] > parsed["high"]:
            raise ValueError("Invalid numerical evidence")
        groups[row["week"][:4]].append(parsed)
        groups["All"].append(parsed)
    if set(groups) != set(ANNUAL):
        raise ValueError("Evidence has different calendar-year groups")
    for year, rows in groups.items():
        base = mean(abs(row["baseline"] - row["actual"]) for row in rows)
        model = mean(abs(row["forecast"] - row["actual"]) for row in rows)
        coverage = 100 * mean(row["low"] <= row["actual"] <= row["high"] for row in rows)
        actual = (len(rows), round(base, 2), round(model, 2), round(100 * (1 - model / base), 1), round(coverage, 1))
        if actual != ANNUAL[year]:
            raise ValueError(f"{year}: expected {ANNUAL[year]}, got {actual}")
    closer = sum(abs(row["forecast"] - row["actual"]) < abs(row["baseline"] - row["actual"]) for row in groups["All"])
    ties = sum(abs(row["forecast"] - row["actual"]) == abs(row["baseline"] - row["actual"]) for row in groups["All"])
    if (closer, ties) != (266, 0):
        raise ValueError("Weekly model comparison differs from the reported count")
    by_date = {row["week"]: row for row in raw}
    for week, values in {
        "2018-01-05": ("-359", "-158", "-296.7401"),
        "2018-02-02": ("-119", "-118", "-101.535"),
    }.items():
        actual = tuple(Decimal(by_date[week][key]) for key in ("actual", "baseline", "forecast"))
        if actual != tuple(map(Decimal, values)):
            raise ValueError(f"{week}: weekly example differs from the frozen replay")
    return "Storage: all 10 table rows, weekly comparison counts and two examples agree with the replay."


def check_curve(path):
    source = path.read_text(encoding="utf-8")
    match = re.search(r"(?:globalThis\.)?HH_BUNDLED\s*=\s*", source)
    if not match:
        raise ValueError("No embedded HH_BUNDLED snapshot found")
    bundle, _ = json.JSONDecoder().raw_decode(source[match.end():])
    before, after = (bundle["strips"][day] for day in ("2026-06-30", "2026-09-30"))
    if set(before) & set(after) != set(CURVE):
        raise ValueError("Matched contract set differs from the cited comparison")
    for delivery, expected in CURVE.items():
        a, b = Decimal(str(before[delivery])), Decimal(str(after[delivery]))
        if (a, b, b-a) != tuple(map(Decimal, expected)):
            raise ValueError(f"{delivery}: price pair or difference does not match")
    jan_july = [Decimal(str(strip["2027-01"])) - Decimal(str(strip["2027-07"])) for strip in (before, after)]
    if jan_july != [Decimal("1.136"), Decimal("0.657")]:
        raise ValueError("January premium over July differs from the published calculation")
    return "Curve: all nine matched contracts, price differences and January premiums over July agree."


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--storage-csv", type=Path, required=True)
    parser.add_argument("--curve-html", type=Path, required=True)
    options = parser.parse_args()
    print(check_storage(options.storage_csv))
    print(check_curve(options.curve_html))
    print("This checks saved arithmetic, not first-release vintages, model refits, or live forecast skill.")
