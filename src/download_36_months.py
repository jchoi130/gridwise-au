r"""GridWise AU Lesson 06: download and validate 36 months of NSW AEMO data.

Run from your gridwise-au repository root with:
    .\.venv\Scripts\python.exe src\download_36_months.py

Raw CSVs and the combined dataset are intentionally kept out of Git by .gitignore.
"""

from io import BytesIO
from pathlib import Path

import pandas as pd
import requests

BASE_URL = "https://www.aemo.com.au/aemo/data/nem/priceanddemand"
MONTHS = pd.period_range("2023-10", "2026-09", freq="M")
RAW_DIR = Path("data/raw")
PROCESSED_DIR = Path("data/processed")
RAW_DIR.mkdir(parents=True, exist_ok=True)
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

all_months = []

with requests.Session() as session:
    for period in MONTHS:
        month = period.strftime("%Y%m")
        filename = f"PRICE_AND_DEMAND_{month}_NSW1.csv"
        raw_file = RAW_DIR / filename

        if raw_file.exists():
            print(f"Reading saved file: {month}")
            content = raw_file.read_bytes()
        else:
            print(f"Downloading from AEMO: {month}")
            url = f"{BASE_URL}/{filename}"
            response = session.get(url, timeout=60)
            response.raise_for_status()
            content = response.content

        df = pd.read_csv(BytesIO(content))
        required = {"REGION", "SETTLEMENTDATE", "TOTALDEMAND", "RRP"}
        missing = required - set(df.columns)
        if missing:
            raise ValueError(f"{month}: missing columns {sorted(missing)}")

        if not (df["REGION"] == "NSW1").all():
            raise ValueError(f"{month}: unexpected market region")

        df["SETTLEMENTDATE"] = pd.to_datetime(
            df["SETTLEMENTDATE"],
            format="%Y/%m/%d %H:%M:%S",
            errors="raise",
        )
        for column in ["TOTALDEMAND", "RRP"]:
            df[column] = pd.to_numeric(df[column], errors="raise")

        if df[["TOTALDEMAND", "RRP"]].isna().any().any():
            raise ValueError(f"{month}: missing demand or price values")

        df = df.sort_values("SETTLEMENTDATE")
        expected_rows = period.days_in_month * 24 * 12
        first_time = period.start_time + pd.Timedelta(minutes=5)
        expected_times = pd.date_range(
            first_time, periods=expected_rows, freq="5min"
        )
        actual_times = pd.DatetimeIndex(df["SETTLEMENTDATE"])
        if len(df) != expected_rows or not actual_times.equals(expected_times):
            raise ValueError(f"{month}: unexpected row count or timestamp gaps")

        # Only save a newly downloaded raw file after validation succeeds.
        if not raw_file.exists():
            raw_file.write_bytes(content)

        all_months.append(
            df[["REGION", "SETTLEMENTDATE", "TOTALDEMAND", "RRP"]]
        )
        print(f"  OK: {len(df):,} five-minute observations")

combined = pd.concat(all_months, ignore_index=True)
output = PROCESSED_DIR / "nsw_202310_to_202609.csv"
combined.to_csv(output, index=False)

print("\nAll 36 months validated!")
print(f"Total observations: {len(combined):,}")
print(f"Earliest timestamp: {combined['SETTLEMENTDATE'].min()}")
print(f"Latest timestamp: {combined['SETTLEMENTDATE'].max()}")
print(f"Combined CSV saved to: {output}")