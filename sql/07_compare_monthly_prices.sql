-- GridWise AU: Compare monthly NSW wholesale electricity prices

SELECT
    TO_CHAR(settlement_date - INTERVAL '5 minutes', 'YYYY-MM') AS month,
    COUNT(*) AS total_records,
    ROUND(AVG(rrp_aud_per_mwh), 2) AS average_price
FROM public.price_demand_observations
WHERE region_code = 'NSW1'
GROUP BY TO_CHAR(settlement_date - INTERVAL '5 minutes', 'YYYY-MM')
ORDER BY month;