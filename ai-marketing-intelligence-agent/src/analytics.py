import pandas as pd
df=pd.read_csv('data/raw/bank-full.csv',sep=';'); df['converted']=(df.y=='yes').astype(int)
summary=df.groupby('job').agg(leads=('converted','size'),conversions=('converted','sum'),conversion_rate=('converted','mean'),avg_balance=('balance','mean')).sort_values('conversion_rate',ascending=False)
summary.to_csv('data/campaign_kpis.csv'); print(summary.round(4))
