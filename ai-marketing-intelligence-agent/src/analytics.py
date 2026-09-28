import pandas as pd
df=pd.read_csv('data/campaigns.csv'); g=df.groupby('campaign')[['impressions','clicks','conversions','spend','revenue']].sum(); g['CTR']=g.clicks/g.impressions; g['CVR']=g.conversions/g.clicks.replace(0,1); g['CAC']=g.spend/g.conversions.replace(0,1); g['ROAS']=g.revenue/g.spend.replace(0,1); g.to_csv('data/campaign_kpis.csv'); print(g.round(3))
