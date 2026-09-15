# Power BI implementation guide

Connect Power BI Desktop to the Snowflake `OLIST_DWH.ANALYTICS` schema or to the local PostgreSQL gold table.

## Recommended pages
1. Executive Overview: revenue, orders, customers, AOV, average delivery days, review score.
2. Customer 360: customer segments, repeat customers, CLV distribution, geography.
3. Operations: delivery time, late-delivery rate, order status, freight cost.
4. Product & Seller: category revenue, seller performance, freight contribution.

## Core DAX measures
```DAX
Total Revenue = SUM(Customer_360[TOTAL_REVENUE])
Total Orders = SUM(Customer_360[ORDER_COUNT])
Total Customers = DISTINCTCOUNT(Customer_360[CUSTOMER_UNIQUE_ID])
Average Order Value = DIVIDE([Total Revenue], [Total Orders])
Repeat Customer Rate =
DIVIDE(
    CALCULATE([Total Customers], Customer_360[ORDER_COUNT] > 1),
    [Total Customers]
)
Average Delivery Days = AVERAGE(Customer_360[AVG_DELIVERY_DAYS])
Average Review Score = AVERAGE(Customer_360[AVG_REVIEW_SCORE])
```

Do not publish a `.pbix` file containing credentials. Save credentials in the Power BI data-source configuration, not in Git.
