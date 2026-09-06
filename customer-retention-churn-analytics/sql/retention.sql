-- Churn rate
SELECT AVG(churned::int) AS churn_rate FROM customers;

-- Risk/value prioritization
SELECT customer_id, avg_order_value, days_since_last_activity,
       orders_90d, sessions_30d
FROM customers
WHERE days_since_last_activity > 60
ORDER BY avg_order_value DESC;

-- Activity buckets
SELECT CASE WHEN days_since_last_activity <= 7 THEN '0-7'
            WHEN days_since_last_activity <= 30 THEN '8-30'
            WHEN days_since_last_activity <= 60 THEN '31-60'
            ELSE '61+' END AS inactivity_bucket,
       COUNT(*) customers, AVG(churned::int) churn_rate
FROM customers GROUP BY 1 ORDER BY 1;
