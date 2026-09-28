SELECT COUNT(*) AS customers, SUM(orders) AS orders, ROUND(SUM(spend),2) AS revenue, ROUND(AVG(spend),2) AS avg_customer_value, ROUND(AVG(days_since_order),1) AS avg_days_since_order FROM customers;
