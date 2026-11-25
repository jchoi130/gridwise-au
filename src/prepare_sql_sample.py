import pandas as pd

# Read only the first 10 observations.
data = pd.read_csv(
    "data/processed/nsw_202310_to_202609.csv",
    nrows=10
)

# Rename the columns to match our PostgreSQL table.
data = data.rename(columns={
    "REGION": "region_code",
    "SETTLEMENTDATE": "settlement_date",
    "TOTALDEMAND": "total_demand_mw",
    "RRP": "rrp_aud_per_mwh",
    "PERIODTYPE": "period_type"
})

# Save a small CSV file for our database test.
data.to_csv("data/processed/nsw_sql_sample.csv", index=False)

print(data)
print("Sample CSV created successfully!")
