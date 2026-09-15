"""PySpark ETL for the Olist Customer 360 platform.

Usage:
  spark-submit spark_etl/olist_etl.py --input data/raw --output data/processed
"""
import argparse
from pyspark.sql import SparkSession, functions as F


def main(input_dir: str, output_dir: str) -> None:
    spark = SparkSession.builder.appName("Customer360-Olist-ETL").getOrCreate()

    customers = spark.read.option("header", True).option("inferSchema", True).csv(f"{input_dir}/olist_customers_dataset.csv")
    orders = spark.read.option("header", True).option("inferSchema", True).csv(f"{input_dir}/olist_orders_dataset.csv")
    items = spark.read.option("header", True).option("inferSchema", True).csv(f"{input_dir}/olist_order_items_dataset.csv")
    payments = spark.read.option("header", True).option("inferSchema", True).csv(f"{input_dir}/olist_order_payments_dataset.csv")

    orders = (orders.dropDuplicates(["order_id"])
              .withColumn("purchase_ts", F.to_timestamp("order_purchase_timestamp"))
              .withColumn("delivered_ts", F.to_timestamp("order_delivered_customer_date"))
              .withColumn("delivery_days", F.datediff("delivered_ts", "purchase_ts")))

    items = (items.dropDuplicates(["order_id", "order_item_id"])
             .withColumn("item_revenue", F.col("price") + F.coalesce(F.col("freight_value"), F.lit(0))))

    order_value = items.groupBy("order_id").agg(
        F.sum("item_revenue").alias("order_revenue"),
        F.countDistinct("product_id").alias("unique_products"),
    )

    customer_360 = (customers.join(orders, "customer_id", "left")
                    .join(order_value, "order_id", "left")
                    .groupBy("customer_unique_id")
                    .agg(
                        F.countDistinct("order_id").alias("orders"),
                        F.sum("order_revenue").alias("revenue"),
                        F.avg("order_revenue").alias("avg_order_value"),
                        F.max("purchase_ts").alias("last_purchase_ts"),
                        F.avg("delivery_days").alias("avg_delivery_days"),
                    )
                    .withColumn("revenue", F.round(F.coalesce("revenue", F.lit(0)), 2))
                    .withColumn("avg_order_value", F.round(F.coalesce("avg_order_value", F.lit(0)), 2)))

    customer_360.write.mode("overwrite").option("header", True).csv(f"{output_dir}/customer_360")
    spark.stop()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="data/raw")
    parser.add_argument("--output", default="data/processed")
    args = parser.parse_args()
    main(args.input, args.output)
