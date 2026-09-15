import sys
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from pyspark.sql import functions as F

args = getResolvedOptions(sys.argv, ["JOB_NAME", "RAW_S3", "GOLD_S3"])
sc = SparkContext()
glue_context = GlueContext(sc)
spark = glue_context.spark_session
job = Job(glue_context)
job.init(args["JOB_NAME"], args)

raw = args["RAW_S3"].rstrip("/")
gold = args["GOLD_S3"].rstrip("/")
customers = spark.read.option("header", True).csv(f"{raw}/olist_customers_dataset.csv")
orders = spark.read.option("header", True).csv(f"{raw}/olist_orders_dataset.csv")
items = spark.read.option("header", True).csv(f"{raw}/olist_order_items_dataset.csv")
payments = spark.read.option("header", True).csv(f"{raw}/olist_order_payments_dataset.csv")
reviews = spark.read.option("header", True).csv(f"{raw}/olist_order_reviews_dataset.csv")

orders = orders.withColumn("order_purchase_timestamp", F.to_timestamp("order_purchase_timestamp")) \
    .withColumn("order_delivered_customer_date", F.to_timestamp("order_delivered_customer_date"))
orders = orders.withColumn("delivery_days", F.datediff("order_delivered_customer_date", "order_purchase_timestamp"))
items = items.withColumn("price", F.col("price").cast("double")).withColumn("freight_value", F.col("freight_value").cast("double"))
items_agg = items.groupBy("order_id").agg(F.sum("price").alias("revenue"), F.sum("freight_value").alias("freight_value"))
pay_agg = payments.withColumn("payment_value", F.col("payment_value").cast("double")).groupBy("order_id").agg(F.sum("payment_value").alias("payment_value"))
review_agg = reviews.withColumn("review_score", F.col("review_score").cast("double")).groupBy("order_id").agg(F.avg("review_score").alias("review_score"))

base = orders.join(customers, "customer_id", "left").join(items_agg, "order_id", "left").join(pay_agg, "order_id", "left").join(review_agg, "order_id", "left")
base = base.fillna({"revenue": 0.0, "freight_value": 0.0, "payment_value": 0.0})
customer_360 = base.groupBy("customer_id", "customer_unique_id", "customer_city", "customer_state").agg(
    F.countDistinct("order_id").alias("order_count"),
    F.countDistinct(F.when(F.col("order_status") == "delivered", F.col("order_id"))).alias("completed_order_count"),
    F.round(F.sum("revenue"), 2).alias("total_revenue"),
    F.round(F.sum("freight_value"), 2).alias("total_freight"),
    F.min("order_purchase_timestamp").alias("first_order_date"),
    F.max("order_purchase_timestamp").alias("last_order_date"),
    F.round(F.avg("delivery_days"), 2).alias("avg_delivery_days"),
    F.round(F.avg("review_score"), 2).alias("avg_review_score")
).withColumn("average_order_value", F.round(F.col("total_revenue") / F.col("order_count"), 2))

customer_360.write.mode("overwrite").option("header", True).csv(f"{gold}/customer_360")
job.commit()
