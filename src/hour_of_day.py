import pandas as pd
import matplotlib.pyplot as plt

# Read our three years of NSW electricity data.
file_path = "data/processed/nsw_202310_to_202609.csv"
data = pd.read_csv(file_path)

# Find the hour when each 5-minute interval started.
data["SETTLEMENTDATE"] = pd.to_datetime(data["SETTLEMENTDATE"])
start_time = data["SETTLEMENTDATE"] - pd.Timedelta(minutes=5)
data["hour"] = start_time.dt.hour

# Calculate averages for each hour of the day.
hourly_averages = data.groupby("hour")[["TOTALDEMAND", "RRP"]].mean()

print("Average NSW demand (MW) and wholesale price (AUD/MWh) by hour:")
print(hourly_averages.round(2))

# Draw average wholesale price for each hour.
plt.plot(
    hourly_averages.index,
    hourly_averages["RRP"],
    marker="o"
)

plt.title("NSW average wholesale price by hour")
plt.xlabel("Hour of day (0 = midnight)")
plt.ylabel("Average price (AUD/MWh)")

plt.xticks(range(0, 24, 2))
plt.grid(True)
plt.tight_layout()

plt.savefig("outputs/charts/nsw_hourly_prices.png")
plt.show()

