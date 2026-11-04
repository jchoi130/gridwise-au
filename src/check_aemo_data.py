from pathlib import Path
import pandas as pd

file_path = Path("data/raw/nsw_september_2026.csv")

if not file_path.exists():
    raise FileNotFoundError(f"CSV not found: {file_path}")

df = pd.read_csv(file_path)
required = {"SETTLEMENTDATE", "TOTALDEMAND", "RRP"}

missing_columns = required - set(df.columns)

if missing_columns:
    raise ValueError(
        f"Missing columns: {sorted(missing_columns)}"
    )
df["SETTLEMENTDATE"] = pd.to_datetime(
    df["SETTLEMENTDATE"], errors="coerce"
)

for column in ["TOTALDEMAND", "RRP"]:
    df[column] = pd.to_numeric(
        df[column], errors="coerce"
    )

print("Rows:", len(df))

print("\nMissing values:")
print(
    df[["SETTLEMENTDATE", "TOTALDEMAND", "RRP"]]
    .isna()
    .sum()
)

valid_rows = df.dropna(subset=["SETTLEMENTDATE"])

duplicates = (
    valid_rows["SETTLEMENTDATE"]
    .duplicated()
    .sum()
)

print("\nDuplicate timestamps:", duplicates)

unique_times = (
    valid_rows["SETTLEMENTDATE"]
    .drop_duplicates()
    .sort_values()
)

differences = unique_times.diff().dropna()

unusual_gaps = differences[
    differences != pd.Timedelta(minutes=5)
]

print("Non-5-minute intervals:", len(unusual_gaps))

if not unusual_gaps.empty:
    print("First unusual intervals:")
    print(unusual_gaps.head())

expected_rows = 30 * 24 * 12

print("\nExpected September rows:", expected_rows)
print("Actual rows:", len(df))

print("Earliest timestamp:", unique_times.min())
print("Latest timestamp:", unique_times.max())

print(
    "Wholesale price range (AUD/MWh):",
    df["RRP"].min(), "to", df["RRP"].max()
)

print(
    "Demand range (MW):",
    df["TOTALDEMAND"].min(),
    "to",
    df["TOTALDEMAND"].max()
)