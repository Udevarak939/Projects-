from pathlib import Path
import pandas as pd

REQUIRED = {
    "olist_customers_dataset.csv": {"customer_id", "customer_unique_id"},
    "olist_orders_dataset.csv": {"order_id", "customer_id", "order_status"},
    "olist_order_items_dataset.csv": {"order_id", "price", "freight_value"},
    "olist_order_payments_dataset.csv": {"order_id", "payment_type", "payment_value"},
}


def profile(raw_dir="data/raw"):
    root = Path(raw_dir)
    report = []
    for name, required in REQUIRED.items():
        df = pd.read_csv(root / name)
        report.append({"file": name, "rows": len(df), "columns": len(df.columns), "duplicate_rows": int(df.duplicated().sum()), "missing_cells": int(df.isna().sum().sum())})
        missing = required - set(df.columns)
        if missing:
            raise ValueError(f"{name}: missing {sorted(missing)}")
    result = pd.DataFrame(report)
    print(result.to_string(index=False))
    return result


if __name__ == "__main__":
    profile()
