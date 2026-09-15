"""Customer analytics models for the gold Customer 360 dataset."""
import argparse
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, roc_auc_score


def segment_customers(df: pd.DataFrame) -> pd.DataFrame:
    features = df[["orders", "revenue", "avg_order_value", "avg_delivery_days"]].fillna(0).clip(lower=0)
    scaled = StandardScaler().fit_transform(features)
    model = KMeans(n_clusters=4, random_state=42, n_init=10)
    df = df.copy()
    df["segment"] = model.fit_predict(scaled)
    return df


def churn_model(df: pd.DataFrame) -> None:
    # Proxy target for portfolio modeling: one order and low value indicates low engagement.
    df = df.dropna(subset=["orders", "revenue", "avg_order_value"]).copy()
    df["churn_proxy"] = ((df["orders"] <= 1) & (df["revenue"] < df["revenue"].median())).astype(int)
    X = df[["orders", "revenue", "avg_order_value", "avg_delivery_days"]].fillna(0)
    y = df["churn_proxy"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)
    probabilities = model.predict_proba(X_test)[:, 1]
    print(classification_report(y_test, model.predict(X_test)))
    print(f"ROC-AUC: {roc_auc_score(y_test, probabilities):.3f}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    args = parser.parse_args()
    data = pd.read_csv(args.input)
    data = segment_customers(data)
    churn_model(data)
