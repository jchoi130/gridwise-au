-- GridWise AU: Find monthly wholesale electricity price extremes

SELECT
    TO_CHAR(settlement_date - INTERVAL '5 minutes', 'YYYY-MM') AS month,
    ROUND(MIN(rrp_aud_per_mwh), 2) AS lowest_price,
    ROUND(MAX(rrp_aud_per_mwh), 2) AS highest_price,
    ROUND(AVG(rrp_aud_per_mwh), 2) AS average_price
FROM public.price_demand_observations
WHERE region_code = 'NSW1'
GROUP BY TO_CHAR(settlement_date - INTERVAL '5 minutes', 'YYYY-MM')
ORDER BY month;