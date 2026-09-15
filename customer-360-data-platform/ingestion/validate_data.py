import argparse
from pathlib import Path
import pandas as pd

EXPECTED = {
    "olist_customers_dataset.csv": ["customer_id", "customer_unique_id", "customer_zip_code_prefix", "customer_city", "customer_state"],
    "olist_orders_dataset.csv": ["order_id", "customer_id", "order_status", "order_purchase_timestamp", "order_approved_at", "order_delivered_carrier_date", "order_delivered_customer_date", "order_estimated_delivery_date"],
    "olist_order_items_dataset.csv": ["order_id", "order_item_id", "product_id", "seller_id", "price", "freight_value"],
    "olist_order_payments_dataset.csv": ["order_id", "payment_sequential", "payment_type", "payment_installments", "payment_value"],
    "olist_order_reviews_dataset.csv": ["review_id", "order_id", "review_score"],
    "olist_products_dataset.csv": ["product_id", "product_category_name"],
    "olist_sellers_dataset.csv": ["seller_id", "seller_zip_code_prefix", "seller_city", "seller_state"],
    "olist_geolocation_dataset.csv": ["geolocation_zip_code_prefix", "geolocation_lat", "geolocation_lng", "geolocation_city", "geolocation_state"],
    "product_category_name_translation.csv": ["product_category_name", "product_category_name_english"],
}


def validate(raw_dir: str) -> None:
    root = Path(raw_dir)
    missing = []
    for filename, columns in EXPECTED.items():
        path = root / filename
        if not path.exists():
            missing.append(filename)
            continue
        df = pd.read_csv(path, nrows=5)
        absent = [c for c in columns if c not in df.columns]
        if absent:
            raise ValueError(f"{filename}: missing columns {absent}")
        print(f"OK {filename}: {len(df.columns)} columns")
    if missing:
        raise FileNotFoundError("Missing Olist files: " + ", ".join(missing))
    print("Source validation passed.")


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--input", default="data/raw")
    args = p.parse_args()
    validate(args.input)
