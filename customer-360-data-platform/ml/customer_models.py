import argparse
from pathlib import Path
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, roc_auc_score
from sklearn.preprocessing import StandardScaler

FEATURES = ["order_count", "total_revenue", "average_order_value", "avg_delivery_days"]


def score(path: str) -> pd.DataFrame:
    df = pd.read_csv(path, parse_dates=["first_order_date", "last_order_date"])
    X = df[FEATURES].fillna(df[FEATURES].median()).fillna(0)
    scaled = StandardScaler().fit_transform(X)
    kmeans = KMeans(n_clusters=4, random_state=42, n_init=20)
    df["customer_segment"] = kmeans.fit_predict(scaled)

    # Portfolio-only churn proxy: customer has exactly one order and that order is old.
    cutoff = df["last_order_date"].max() - pd.Timedelta(days=180)
    df["churn_proxy"] = ((df["order_count"] == 1) & (df["last_order_date"] < cutoff)).astype(int)
    y = df["churn_proxy"]
    if y.nunique() == 2:
        model = LogisticRegression(max_iter=1000, class_weight="balanced", random_state=42)
        model.fit(X, y)
        pred = model.predict(X)
        prob = model.predict_proba(X)[:, 1]
        print(classification_report(y, pred, zero_division=0))
        print(f"Training-set ROC-AUC (descriptive, not holdout): {roc_auc_score(y, prob):.3f}")
    else:
        print("Churn proxy has one class; skipping logistic regression.")
    return df


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--input", default="data/processed/customer_360.csv")
    p.add_argument("--output", default="data/gold/customer_scores.csv")
    args = p.parse_args()
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    result = score(args.input)
    result.to_csv(args.output, index=False)
    print(f"Wrote {len(result):,} scored customers to {args.output}")
