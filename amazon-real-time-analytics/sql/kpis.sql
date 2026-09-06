-- Core commerce KPIs
SELECT DATE_TRUNC('hour', event_time) AS hour,
       COUNT(DISTINCT order_id) AS orders,
       COUNT(DISTINCT customer_id) AS customers,
       SUM(quantity * unit_price) AS revenue,
       SUM(quantity * unit_price) / NULLIF(COUNT(DISTINCT order_id),0) AS aov
FROM orders
WHERE status = 'completed'
GROUP BY 1 ORDER BY 1;

-- Product performance
SELECT product, COUNT(DISTINCT order_id) orders,
       SUM(quantity) units,
       SUM(quantity * unit_price) revenue
FROM orders WHERE status='completed'
GROUP BY product ORDER BY revenue DESC;

-- Cancellation rate
SELECT 100.0 * AVG(CASE WHEN status='cancelled' THEN 1 ELSE 0 END) cancellation_rate
FROM orders;
