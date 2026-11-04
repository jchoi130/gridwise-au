from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

# Step 1: Read our existing CSV
file_path = Path("data/raw/nsw_september_2026.csv")

if not file_path.exists():
    raise FileNotFoundError(f"Could not find CSV: {file_path}")

df = pd.read_csv(file_path)

# Step 2: Check and convert our data
required = {"SETTLEMENTDATE", "TOTALDEMAND", "RRP"}
missing = required - set(df.columns)

if missing:
    raise ValueError(f"Missing columns: {sorted(missing)}")

df["SETTLEMENTDATE"] = pd.to_datetime(
    df["SETTLEMENTDATE"], errors="coerce"
)

for column in ["TOTALDEMAND", "RRP"]:
    df[column] = pd.to_numeric(
        df[column], errors="coerce"
    )

df = df.dropna(
    subset=["SETTLEMENTDATE", "TOTALDEMAND", "RRP"]
)

# Step 3: Calculate hourly averages
df["hour"] = (
    df["SETTLEMENTDATE"] - pd.Timedelta(minutes=5)
).dt.floor("h")

hourly = df.groupby("hour")[["TOTALDEMAND", "RRP"]].mean()

# Step 4: Calculate Pearson correlation
correlation = hourly["TOTALDEMAND"].corr(hourly["RRP"])

print("Hourly observations:", len(hourly))
print(f"Demand vs price Pearson correlation: {correlation:.3f}")

# Step 5: Create our scatter plot
output = Path(
    "outputs/charts/nsw_demand_vs_price_september_2026.png"
)
output.parent.mkdir(parents=True, exist_ok=True)

plt.figure(figsize=(9, 6))
plt.scatter(
    hourly["TOTALDEMAND"],
    hourly["RRP"],
    alpha=0.5,
    s=16
)

plt.axhline(0, linestyle="--", linewidth=1)
plt.title("NSW: Hourly Demand vs Wholesale Price - September 2026")
plt.xlabel("Average electricity demand (MW)")
plt.ylabel("Average wholesale price (AUD/MWh)")
plt.grid(alpha=0.2)
plt.tight_layout()

plt.savefig(output, dpi=150)
plt.close()

print("Chart saved to:", output)