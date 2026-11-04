from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# 1. Read our existing electricity dataset
file_path = Path("data/raw/nsw_september_2026.csv")

if not file_path.exists():
    raise FileNotFoundError(f"CSV not found: {file_path}")

df = pd.read_csv(file_path)

# Convert timestamps into datetime values
df["SETTLEMENTDATE"] = pd.to_datetime(
    df["SETTLEMENTDATE"]
)

# 2. Calculate hourly averages
# AEMO timestamps mark the end of each 5-minute interval
df["hour"] = (
    df["SETTLEMENTDATE"] - pd.Timedelta(minutes=5)
).dt.floor("h")

hourly = df.groupby("hour")[["RRP", "TOTALDEMAND"]].mean()

print("Hourly observations:", len(hourly))
print(hourly.head())

# 3. Create a folder to save our graphs
chart_folder = Path("outputs/charts")
chart_folder.mkdir(parents=True, exist_ok=True)

# 4. Plot electricity prices
plt.figure(figsize=(12, 5))
plt.plot(hourly.index, hourly["RRP"])

plt.axhline(0, linestyle="--", linewidth=1)
plt.title("NSW Wholesale Electricity Prices - September 2026")
plt.xlabel("Date")
plt.ylabel("Price (AUD/MWh)")
plt.xticks(rotation=30)

plt.tight_layout()
plt.savefig(
    chart_folder / "nsw_prices_september_2026.png",
    dpi=150
)
plt.close()

# 5. Plot electricity demand
plt.figure(figsize=(12, 5))
plt.plot(hourly.index, hourly["TOTALDEMAND"])

plt.title("NSW Electricity Demand - September 2026")
plt.xlabel("Date")
plt.ylabel("Electricity Demand (MW)")
plt.xticks(rotation=30)

plt.tight_layout()
plt.savefig(
    chart_folder / "nsw_demand_september_2026.png",
    dpi=150
)
plt.close()

print("Both charts saved to:", chart_folder)
