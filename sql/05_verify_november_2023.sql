-- GridWise AU: Verify November 2023 electricity data

-- Count only November's NSW observations.
SELECT COUNT(*) AS november_rows
FROM public.price_demand_observations
WHERE region_code = 'NSW1'
  AND settlement_date >= '2023-11-01 00:05:00'
  AND settlement_date <= '2023-12-01 00:00:00';

-- Check the combined total for October and November.
SELECT COUNT(*) AS total_rows
FROM public.price_demand_observations;