import pandas as pd
import numpy as np


def build_kpis(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df['event_time'] = pd.to_datetime(df['event_time'])
    df['revenue'] = df['quantity'] * df['unit_price']
    return (df.groupby(df['event_time'].dt.floor('15min'))
              .agg(orders=('order_id','nunique'), customers=('customer_id','nunique'),
                   revenue=('revenue','sum'), units=('quantity','sum'))
              .assign(aov=lambda x: x.revenue / x.orders.replace(0, np.nan))
              .reset_index())


def customer_segments(df: pd.DataFrame) -> pd.DataFrame:
    x = df.copy()
    x['revenue'] = x.quantity * x.unit_price
    return (x.groupby('customer_id')
              .agg(orders=('order_id','nunique'), revenue=('revenue','sum'), units=('quantity','sum'))
              .assign(segment=lambda z: pd.qcut(z.revenue.rank(method='first'), 4,
                                                labels=['Bronze','Silver','Gold','Platinum']))
              .reset_index())


def detect_revenue_anomalies(kpis: pd.DataFrame) -> pd.DataFrame:
    x = kpis.copy()
    mean = x.revenue.rolling(8, min_periods=4).mean()
    std = x.revenue.rolling(8, min_periods=4).std().replace(0, np.nan)
    x['z_score'] = (x.revenue - mean) / std
    x['anomaly'] = x.z_score.abs() >= 3
    return x
