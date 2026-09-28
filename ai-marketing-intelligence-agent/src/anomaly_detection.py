import pandas as pd
df=pd.read_csv('data/campaign_kpis.csv'); df['roas_z']=(df.ROAS-df.ROAS.mean())/df.ROAS.std(); df['anomaly']=df.roas_z.abs()>2; df.to_csv('data/campaign_kpis_scored.csv'); print(df[['ROAS','roas_z','anomaly']])
