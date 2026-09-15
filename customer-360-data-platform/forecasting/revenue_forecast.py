import argparse
from pathlib import Path
import pandas as pd


def forecast(raw_dir="data/raw", output="data/gold/monthly_revenue.csv"):
    orders = pd.read_csv(Path(raw_dir) / "olist_orders_dataset.csv", parse_dates=["order_purchase_timestamp"])
    items = pd.read_csv(Path(raw_dir) / "olist_order_items_dataset.csv")
    revenue = items.groupby("order_id", as_index=False)["price"].sum().rename(columns={"price": "revenue"})
    df = orders.merge(revenue, on="order_id", how="left")
    df["revenue"] = df["revenue"].fillna(0)
    monthly = df.set_index("order_purchase_timestamp")["revenue"].resample("MS").sum().reset_index()
    monthly["rolling_3m_revenue"] = monthly["revenue"].rolling(3, min_periods=1).mean()
    monthly["mom_growth"] = monthly["revenue"].pct_change()
    Path(output).parent.mkdir(parents=True, exist_ok=True)
    monthly.to_csv(output, index=False)
    print(f"Wrote {len(monthly)} monthly observations to {output}")
    return monthly


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--input", default="data/raw")
    p.add_argument("--output", default="data/gold/monthly_revenue.csv")
    args = p.parse_args()
    forecast(args.input, args.output)
