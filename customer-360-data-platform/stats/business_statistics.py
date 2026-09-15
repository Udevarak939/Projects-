import argparse
from pathlib import Path
import pandas as pd
from scipy.stats import ttest_ind, chi2_contingency


def run(raw_dir="data/raw"):
    root = Path(raw_dir)
    orders = pd.read_csv(root / "olist_orders_dataset.csv", parse_dates=["order_purchase_timestamp"])
    items = pd.read_csv(root / "olist_order_items_dataset.csv")
    customers = pd.read_csv(root / "olist_customers_dataset.csv")
    orders = orders.merge(customers[["customer_id", "customer_state"]], on="customer_id", how="left")
    revenue = items.groupby("order_id", as_index=False)["price"].sum().rename(columns={"price": "order_revenue"})
    orders = orders.merge(revenue, on="order_id", how="left")
    orders["order_revenue"] = orders["order_revenue"].fillna(0)

    top_states = orders["customer_state"].value_counts().head(2).index.tolist()
    if len(top_states) == 2:
        a = orders.loc[orders.customer_state == top_states[0], "order_revenue"]
        b = orders.loc[orders.customer_state == top_states[1], "order_revenue"]
        stat, p = ttest_ind(a, b, equal_var=False, nan_policy="omit")
        print(f"Welch t-test {top_states[0]} vs {top_states[1]}: statistic={stat:.3f}, p={p:.4g}")

    contingency = pd.crosstab(orders["order_status"], orders["customer_state"])
    chi2, p, dof, _ = chi2_contingency(contingency)
    print(f"Chi-square order status vs state: chi2={chi2:.3f}, dof={dof}, p={p:.4g}")


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--input", default="data/raw")
    args = p.parse_args()
    run(args.input)
