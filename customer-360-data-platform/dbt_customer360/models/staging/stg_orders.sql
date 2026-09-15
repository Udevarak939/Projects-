SELECT
    order_id,
    customer_id,
    order_status,
    CAST(order_purchase_timestamp AS TIMESTAMP) AS purchase_ts,
    CAST(order_delivered_customer_date AS TIMESTAMP) AS delivered_ts,
    DATEDIFF('day', CAST(order_purchase_timestamp AS TIMESTAMP), CAST(order_delivered_customer_date AS TIMESTAMP)) AS delivery_days
FROM {{ source('raw', 'orders') }}
WHERE order_id IS NOT NULL
