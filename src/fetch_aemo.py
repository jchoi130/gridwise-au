from pathlib import Path
from io import BytesIO

import pandas as pd
import requests

# AEMO NSW electricity data: September 2026
url = (
    "https://aemo.com.au/aemo/data/nem/priceanddemand/"
    "PRICE_AND_DEMAND_202609_NSW1.csv"
)

# Where we'll save the downloaded CSV
output = Path("data/raw/nsw_september_2026.csv")
output.parent.mkdir(parents=True, exist_ok=True)

print("Downloading September 2026 NSW electricity data...")

# Download the CSV from AEMO
response = requests.get(url, timeout=60)
response.raise_for_status()

# Read the downloaded CSV with Pandas
df = pd.read_csv(BytesIO(response.content))

# Check the required columns exist
required = {"SETTLEMENTDATE", "TOTALDEMAND", "RRP"}

if not required.issubset(df.columns):
    raise ValueError("Unexpected AEMO CSV format")

# Save the original CSV to our computer
output.write_bytes(response.content)

print("\nDownload successful!")
print("Total records:", len(df))

print("\nFirst five rows:")
print(df.head())

print("\nColumn names:")
print(df.columns.tolist())

print("\nSaved to:", output)
