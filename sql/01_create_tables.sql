-- GridWise AU: Create our first database tables

CREATE TABLE public.regions (
    region_code VARCHAR(4) PRIMARY KEY,
    region_name VARCHAR(80)
);

CREATE TABLE public.price_demand_observations (
    region_code VARCHAR(4),
    settlement_date TIMESTAMP,
    total_demand_mw NUMERIC,
    rrp_aud_per_mwh NUMERIC,
    period_type VARCHAR(20),

    PRIMARY KEY (region_code, settlement_date),
    FOREIGN KEY (region_code)
        REFERENCES public.regions(region_code)
);