import pandas as pd

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
