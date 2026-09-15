"""Validate Olist source files before ETL."""
from pathlib import Path
import pandas as pd

EXPECTED = {
    "olist_customers_dataset.csv": ["customer_id", "customer_unique_id", "customer_zip_code_prefix"],
    "olist_orders_dataset.csv": ["order_id", "customer_id", "order_status", "order_purchase_timestamp"],
    "olist_order_items_dataset.csv": ["order_id", "order_item_id", "product_id", "seller_id", "price"],
    "olist_order_payments_dataset.csv": ["order_id", "payment_type", "payment_value"],
    "olist_products_dataset.csv": ["product_id", "product_category_name"],
}


def validate(data_dir: str = "data/raw") -> None:
    root = Path(data_dir)
    if not root.exists():
        raise FileNotFoundError(f"Dataset directory not found: {root}")

    for filename, columns in EXPECTED.items():
        path = root / filename
        if not path.exists():
            print(f"MISSING: {filename}")
            continue
        df = pd.read_csv(path, nrows=1000)
        missing = sorted(set(columns) - set(df.columns))
        print(f"{filename}: sample_rows={len(df)}, columns={len(df.columns)}")
        if missing:
            raise ValueError(f"{filename} missing columns: {missing}")
        print("  schema: OK")


if __name__ == "__main__":
    validate()
