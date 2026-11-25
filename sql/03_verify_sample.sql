-- GridWise AU: Verify our first NSW electricity data import

-- Count the observations stored in PostgreSQL.
SELECT COUNT(*) AS total_rows
FROM public.price_demand_observations;

-- Display the observations from earliest to latest.
SELECT *
FROM public.price_demand_observations
ORDER BY settlement_date;