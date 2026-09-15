-- Advanced SQL examples for the gold Customer 360 layer.

-- 1. Customer lifetime value ranking
WITH customer_value AS (
    SELECT customer_unique_id,
           COUNT(DISTINCT order_id) AS orders,
           SUM(order_revenue) AS lifetime_value
    FROM fct_customer_orders
    GROUP BY customer_unique_id
)
SELECT *,
       DENSE_RANK() OVER (ORDER BY lifetime_value DESC) AS value_rank
FROM customer_value
ORDER BY lifetime_value DESC;

-- 2. Monthly revenue trend
SELECT DATE_TRUNC('month', purchase_ts) AS month,
       SUM(order_revenue) AS revenue,
       COUNT(DISTINCT order_id) AS orders
FROM fct_customer_orders
GROUP BY 1
ORDER BY 1;

-- 3. Repeat purchase rate
WITH customer_orders AS (
    SELECT customer_unique_id, COUNT(DISTINCT order_id) AS orders
    FROM fct_customer_orders
    GROUP BY 1
)
SELECT 100.0 * SUM(CASE WHEN orders > 1 THEN 1 ELSE 0 END) / COUNT(*) AS repeat_purchase_rate
FROM customer_orders;

-- 4. Delivery SLA performance
SELECT order_status,
       AVG(delivery_days) AS avg_delivery_days,
       PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY delivery_days) AS median_delivery_days
FROM fct_customer_orders
WHERE delivery_days IS NOT NULL
GROUP BY 1;
