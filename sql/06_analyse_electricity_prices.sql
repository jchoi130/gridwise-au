-- GridWise AU: Analyse NSW wholesale electricity prices

-- Calculate November 2023's average wholesale price.
SELECT ROUND(AVG(rrp_aud_per_mwh), 2) AS average_price
FROM public.price_demand_observations
WHERE region_code = 'NSW1'
  AND settlement_date >= '2023-11-01 00:05:00'
  AND settlement_date <= '2023-12-01 00:00:00';


-- Calculate October 2023's average wholesale price.
SELECT ROUND(AVG(rrp_aud_per_mwh), 2) AS average_price
FROM public.price_demand_observations
WHERE region_code = 'NSW1'
  AND settlement_date >= '2023-10-01 00:05:00'
  AND settlement_date <= '2023-11-01 00:00:00';