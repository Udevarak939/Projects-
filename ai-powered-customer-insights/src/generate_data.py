import numpy as np, pandas as pd
rng=np.random.default_rng(42)
n=5000
df=pd.DataFrame({'customer_id':np.arange(1,n+1),'orders':rng.poisson(5,n)+1,'spend':rng.gamma(5,80,n),'days_since_order':rng.integers(1,181,n),'support_tickets':rng.poisson(1,n),'sessions':rng.poisson(8,n)+1})
df['churn']=((df.days_since_order>120)&(df.support_tickets>1)).astype(int)
df.to_csv('data/customers.csv',index=False)
