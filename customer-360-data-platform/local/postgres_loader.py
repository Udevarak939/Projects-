import argparse
import os
from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine


def load(csv_path, table, replace=True):
    df = pd.read_csv(csv_path)
    url = os.getenv("POSTGRES_URL", "postgresql+psycopg2://customer360:customer360_dev@localhost:5432/customer360")
    engine = create_engine(url)
    df.to_sql(table, engine, if_exists="replace" if replace else "append", index=False, method="multi", chunksize=5000)
    print(f"Loaded {len(df):,} rows into {table}")

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--input", default="data/processed/customer_360.csv")
    p.add_argument("--table", default="customer_360")
    args = p.parse_args()
    load(args.input, args.table)
