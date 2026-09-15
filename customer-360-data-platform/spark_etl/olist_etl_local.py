import argparse
from pathlib import Path
import pandas as pd


def load_customer_360(input_dir: str, output_file: str) -> pd.DataFrame:
    root = Path(input_dir)
    customers = pd.read_csv(root / "olist_customers_dataset.csv")
    orders = pd.read_csv(root / "olist_orders_dataset.csv", parse_dates=["order_purchase_timestamp", "order_delivered_customer_date"])
    items = pd.read_csv(root / "olist_order_items_dataset.csv")
    payments = pd.read_csv(root / "olist_order_payments_dataset.csv")
    reviews = pd.read_csv(root / "olist_order_reviews_dataset.csv")

    orders["delivery_days"] = (orders["order_delivered_customer_date"] - orders["order_purchase_timestamp"]).dt.total_seconds() / 86400
    items_by_order = items.groupby("order_id", as_index=False).agg(revenue=("price", "sum"), freight_value=("freight_value", "sum"))
    pay_by_order = payments.groupby("order_id", as_index=False).agg(payment_value=("payment_value", "sum"))
    review_by_order = reviews.groupby("order_id", as_index=False).agg(review_score=("review_score", "mean"))

    base = orders.merge(customers, on="customer_id", how="left")
    base = base.merge(items_by_order, on="order_id", how="left")
    base = base.merge(pay_by_order, on="order_id", how="left")
    base = base.merge(review_by_order, on="order_id", how="left")
    base["revenue"] = base["revenue"].fillna(0)
    base["freight_value"] = base["freight_value"].fillna(0)
    base["payment_value"] = base["payment_value"].fillna(0)

    completed = base["order_status"].eq("delivered")
    agg = base.groupby(["customer_id", "customer_unique_id", "customer_city", "customer_state"], dropna=False).agg(
        order_count=("order_id", "nunique"),
        completed_order_count=("order_id", lambda s: s[base.loc[s.index, "order_status"].eq("delivered")].nunique()),
        total_revenue=("revenue", "sum"),
        total_freight=("freight_value", "sum"),
        first_order_date=("order_purchase_timestamp", "min"),
        last_order_date=("order_purchase_timestamp", "max"),
        avg_delivery_days=("delivery_days", "mean"),
        avg_review_score=("review_score", "mean"),
    ).reset_index()
    agg["average_order_value"] = agg["total_revenue"] / agg["order_count"].replace(0, pd.NA)
    primary_payment = payments.groupby(["order_id", "payment_type"], as_index=False)["payment_value"].sum()
    primary_payment = primary_payment.sort_values(["order_id", "payment_value"], ascending=[True, False]).drop_duplicates("order_id")
    pay_customer = orders[["order_id", "customer_id"]].merge(primary_payment[["order_id", "payment_type"]], on="order_id", how="left")
    primary = pay_customer.groupby("customer_id")["payment_type"].agg(lambda x: x.mode().iat[0] if not x.mode().empty else pd.NA).rename("primary_payment_type")
    agg = agg.join(primary, on="customer_id")
    agg.to_csv(output_file, index=False)
    return agg


if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Build reproducible local Customer 360 gold table")
    p.add_argument("--input", default="data/raw")
    p.add_argument("--output", default="data/processed/customer_360.csv")
    args = p.parse_args()
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    df = load_customer_360(args.input, args.output)
    print(f"Wrote {len(df):,} customer records to {args.output}")
