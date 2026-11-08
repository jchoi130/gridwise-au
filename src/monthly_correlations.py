r"""GridWise AU Lesson 07: Compare demand-price correlation across 36 months.

Run from anywhere with:
    .\.venv\Scripts\python.exe src\monthly_correlations.py

Reads the three-year combined CSV created in Lesson 06. Does not download data.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

# Resolve paths from the project folder, even if the terminal is elsewhere.
PROJECT_DIR = Path(__file__).resolve().parents[1]
input_csv = PROJECT_DIR / "data/processed/nsw_202310_to_202609.csv"
chart_file = PROJECT_DIR / "outputs/charts/nsw_monthly_correlations.png"
tables_dir = PROJECT_DIR / "outputs/tables"

if not input_csv.exists():
    raise FileNotFoundError(f"Combined CSV not found: {input_csv}")

df = pd.read_csv(input_csv)
required = {"SETTLEMENTDATE", "TOTALDEMAND", "RRP"}
missing = required - set(df.columns)
if missing:
    raise ValueError(f"Required columns are missing: {sorted(missing)}")

# Convert the raw CSV fields to dates and numbers.
df["SETTLEMENTDATE"] = pd.to_datetime(
    df["SETTLEMENTDATE"], errors="raise"
)
for column in ["TOTALDEMAND", "RRP"]:
    df[column] = pd.to_numeric(df[column], errors="raise")

if df[["SETTLEMENTDATE", "TOTALDEMAND", "RRP"]].isna().any().any():
    raise ValueError("The dataset contains missing required values")

# AEMO timestamps mark interval ends: subtract 5 minutes before hourly grouping.
df["hour"] = (
    df["SETTLEMENTDATE"] - pd.Timedelta(minutes=5)
).dt.floor("h")
hourly = df.groupby("hour")[["TOTALDEMAND", "RRP"]].mean()

# Each month's correlation uses all its hourly observations.
hourly["month"] = hourly.index.to_period("M")
monthly_rows = []
for month, group in hourly.groupby("month"):
    monthly_rows.append({
        "month": str(month),
        "hours": len(group),
        "pearson_r": group["TOTALDEMAND"].corr(group["RRP"]),
    })
monthly = pd.DataFrame(monthly_rows)

# Compare the four Australian meteorological seasons across all three years.
season_names = {
    12: "Summer", 1: "Summer", 2: "Summer",
    3: "Autumn", 4: "Autumn", 5: "Autumn",
    6: "Winter", 7: "Winter", 8: "Winter",
    9: "Spring", 10: "Spring", 11: "Spring",
}
hourly["season"] = [season_names[t.month] for t in hourly.index]
seasonal_rows = []
for season, group in hourly.groupby("season"):
    seasonal_rows.append({
        "season": season,
        "hours": len(group),
        "pearson_r": group["TOTALDEMAND"].corr(group["RRP"]),
    })
seasonal = pd.DataFrame(seasonal_rows)

# Compare three complete October-to-September periods (not calendar years).
hourly["reporting_start"] = [
    t.year if t.month >= 10 else t.year - 1 for t in hourly.index
]
yearly_rows = []
for year, group in hourly.groupby("reporting_start"):
    yearly_rows.append({
        "period": f"Oct {year} - Sep {year + 1}",
        "hours": len(group),
        "pearson_r": group["TOTALDEMAND"].corr(group["RRP"]),
    })
yearly = pd.DataFrame(yearly_rows)

# Save summary tables, NOT the large source dataset.
tables_dir.mkdir(parents=True, exist_ok=True)
monthly.to_csv(tables_dir / "nsw_monthly_correlations.csv", index=False)
seasonal.to_csv(tables_dir / "nsw_seasonal_correlations.csv", index=False)
yearly.to_csv(tables_dir / "nsw_oct_sep_correlations.csv", index=False)

# Visualise how the correlation changes across the 36 individual months.
chart_file.parent.mkdir(parents=True, exist_ok=True)
positions = list(range(len(monthly)))
plt.figure(figsize=(12, 5))
plt.plot(positions, monthly["pearson_r"], marker="o", markersize=4)
plt.axhline(0, color="gray", linestyle="--", linewidth=1)
plt.xticks(positions[::3], monthly["month"].iloc[::3], rotation=40)
plt.ylim(-1.05, 1.05)
plt.xlabel("Month")
plt.ylabel("Demand-price Pearson correlation (r)")
plt.title("NSW: Monthly Hourly Demand vs Wholesale Price Correlation")
plt.grid(alpha=0.2)
plt.tight_layout()
plt.savefig(chart_file, dpi=150)
plt.close()

print("Hours analysed:", len(hourly))
print("Months analysed:", len(monthly))
print("\nCorrelation by month:")
print(monthly.to_string(index=False))
print("\nCorrelation by season (all years pooled):")
print(seasonal.to_string(index=False))
print("\nCorrelation by complete Oct-Sep period:")
print(yearly.to_string(index=False))
print("\nSaved chart:", chart_file)
print("Saved tables to:", tables_dir)
