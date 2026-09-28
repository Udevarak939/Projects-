import pandas as pd
df=pd.read_csv('data/customers.csv'); assert df.customer_id.is_unique; assert df.isna().sum().sum()==0; assert (df.spend>=0).all(); print(df.describe())
