import numpy as np,pandas as pd
rng=np.random.default_rng(7); n=20000
df=pd.DataFrame({'campaign':rng.choice(['Search','Social','Email','Display'],n),'impressions':rng.integers(500,20000,n)})
df['clicks']=rng.binomial(df.impressions,.06); df['conversions']=rng.binomial(df.clicks,.08); df['spend']=df.clicks*rng.uniform(.5,2.5,n); df['revenue']=df.conversions*rng.uniform(25,120,n); df.to_csv('data/campaigns.csv',index=False)
