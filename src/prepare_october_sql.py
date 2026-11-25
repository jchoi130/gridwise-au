import pandas as pd

# Read October 2023 from our three-year dataset.
data = pd.read_csv(
    "data/processed/nsw_202310_to_202609.csv",
    nrows=8928
)

# Skip the first 10 records because they're already in PostgreSQL.
data = data.iloc[10:]

# Match our PostgreSQL column names.
data = data.rename(columns={
    "REGION": "region_code",
    "SETTLEMENTDATE": "settlement_date",
    "TOTALDEMAND": "total_demand_mw",
    "RRP": "rrp_aud_per_mwh"
})

# Keep the four columns we're importing.
data = data[[
    "region_code",
    "settlement_date",
    "total_demand_mw",
    "rrp_aud_per_mwh"
]]

# Save the remaining October records.
data.to_csv(
    "data/processed/nsw_october_2023_sql.csv",
    index=False
)

print("Records prepared:", len(data))
print("October CSV created successfully!")