# GridWise AU — Relational Schema (Version 1)

**Status:** Proposed database design, before PostgreSQL implementation  
**Scope:** NSW electricity demand and wholesale price observations, with room to add other NEM regions.

## 1. Relational schema

```text
REGIONS(region_code, region_name)

PRICE_DEMAND_OBSERVATIONS(
    region_code,
    settlement_date,
    total_demand_mw,
    rrp_aud_per_mwh,
    period_type
)
```

**Primary keys (PK)**

- `REGIONS`: `region_code`
- `PRICE_DEMAND_OBSERVATIONS`: the combination of `region_code` and `settlement_date` (a **composite primary key**)

**Foreign key (FK)**

- `PRICE_DEMAND_OBSERVATIONS.region_code` references `REGIONS.region_code`.

**Relationship:** One region can have zero or many price-and-demand observations. Each observation belongs to exactly one region (**1 to 0..***).

## 2. Attributes and PostgreSQL data types

### REGIONS

| Attribute | Data type | Key | Meaning |
|---|---|---|---|
| `region_code` | `VARCHAR(4)` | PK | NEM region identifier, e.g. `NSW1` |
| `region_name` | `VARCHAR(80)` | — | Region description, e.g. `New South Wales` |

### PRICE_DEMAND_OBSERVATIONS

| Attribute | Data type | Key | Meaning |
|---|---|---|---|
| `region_code` | `VARCHAR(4)` | PK, FK | Identifies the region; links to `REGIONS` |
| `settlement_date` | `TIMESTAMP` | PK | Timestamp supplied with the AEMO five-minute observation |
| `total_demand_mw` | `NUMERIC` | — | Electricity demand in megawatts (MW) |
| `rrp_aud_per_mwh` | `NUMERIC` | — | Regional wholesale reference price (AUD/MWh); may be negative |
| `period_type` | `VARCHAR(20)` | — | Period classification from the AEMO source |

## 3. Simple example

**REGIONS**

| region_code | region_name |
|---|---|
| NSW1 | New South Wales |
| VIC1 | Victoria |

**PRICE_DEMAND_OBSERVATIONS (example rows for explanation only, not actual observations)**

| region_code | settlement_date | total_demand_mw | rrp_aud_per_mwh | period_type |
|---|---|---:|---:|---|
| NSW1 | 2026-09-01 00:05:00 | 7694.77 | 64.95 | TRADE |

The `region_code` value must already exist in `REGIONS`. The same region cannot have two rows with the same `settlement_date`.

## 4. How this corresponds to the UMLet diagram

- Each table is represented as a box containing attributes.
- `region_code` is the PK of `REGIONS`.
- Both `region_code` and `settlement_date` form the PK of `PRICE_DEMAND_OBSERVATIONS`.
- `region_code` in `PRICE_DEMAND_OBSERVATIONS` is also an FK.
- The relationship line is labeled **1** on the region side and **0..*** on the observation side.

## 5. Design notes

- This is a simple **Version 1**, not the full future Australia-wide system.
- We will review required fields, timestamp and time-zone handling, and constraints when implementing PostgreSQL, especially before expanding beyond NSW.
- This document specifies the database structure; it does **not** create SQL tables.

**Related editable diagram:** `docs/database/gridwise_database_model.uxf`  
**Related exported image:** `docs/database/gridwise_database_model.png`
