-- GridWise AU: Count high wholesale price observations by month

SELECT
    TO_CHAR(settlement_date - INTERVAL '5 minutes', 'YYYY-MM') AS month,
    COUNT(*) AS high_price_records
FROM public.price_demand_observations
WHERE region_code = 'NSW1'
  AND rrp_aud_per_mwh > 300
GROUP BY TO_CHAR(settlement_date - INTERVAL '5 minutes', 'YYYY-MM')
ORDER BY month;