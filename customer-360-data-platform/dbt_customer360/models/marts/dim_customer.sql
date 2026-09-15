SELECT
    customer_unique_id,
    COUNT(DISTINCT order_id) AS order_count,
    SUM(order_revenue) AS lifetime_revenue,
    AVG(order_revenue) AS average_order_value,
    MAX(purchase_ts) AS last_purchase_ts,
    AVG(delivery_days) AS average_delivery_days
FROM {{ ref('fct_customer_360') }}
GROUP BY customer_unique_id
