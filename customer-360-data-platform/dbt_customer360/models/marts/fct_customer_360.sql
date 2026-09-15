WITH orders AS (
    SELECT * FROM {{ ref('stg_orders') }}
),
items AS (
    SELECT order_id, SUM(price + COALESCE(freight_value, 0)) AS order_revenue
    FROM {{ source('raw', 'order_items') }}
    GROUP BY order_id
)
SELECT
    c.customer_unique_id,
    o.order_id,
    o.customer_id,
    o.order_status,
    o.purchase_ts,
    o.delivery_days,
    COALESCE(i.order_revenue, 0) AS order_revenue
FROM orders o
JOIN {{ source('raw', 'customers') }} c ON o.customer_id = c.customer_id
LEFT JOIN items i ON o.order_id = i.order_id
