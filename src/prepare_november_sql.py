import pandas as pd

# Read our three-year NSW electricity dataset.
data = pd.read_csv("data/processed/nsw_202310_to_202609.csv")

# Convert the timestamp column to dates and times.
data["SETTLEMENTDATE"] = pd.to_datetime(data["SETTLEMENTDATE"])

# Keep only November 2023 observations.
november = data[
    data["SETTLEMENTDATE"].between(
        "2023-11-01 00:05:00",
        "2023-12-01 00:00:00"
    )
]

# Rename the columns to match PostgreSQL.
november = november.rename(columns={
    "REGION": "region_code",
    "SETTLEMENTDATE": "settlement_date",
    "TOTALDEMAND": "total_demand_mw",
    "RRP": "rrp_aud_per_mwh"
})

# Keep only the four columns we need.
november = november[[
    "region_code",
    "settlement_date",
    "total_demand_mw",
    "rrp_aud_per_mwh"
]]

# Save the November data as a CSV.
november.to_csv(
    "data/processed/nsw_november_2023_sql.csv",
    index=False
)

print("November records prepared:", len(november))
print("First timestamp:", november["settlement_date"].min())
print("Last timestamp:", november["settlement_date"].max())
print("November CSV created successfully!")
