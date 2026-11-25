-- GridWise AU: Verify October 2023 NSW electricity data

-- Count the October observations stored in PostgreSQL.
SELECT COUNT(*) AS october_rows
FROM public.price_demand_observations
WHERE region_code = 'NSW1'
  AND settlement_date >= '2023-10-01 00:05:00'
  AND settlement_date <= '2023-11-01 00:00:00';