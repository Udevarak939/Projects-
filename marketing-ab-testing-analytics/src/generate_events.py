import random
import pandas as pd
from datetime import datetime, timedelta, timezone

def generate(n=10000, seed=7):
    random.seed(seed); start=datetime.now(timezone.utc)-timedelta(days=7)
    rows=[]
    for i in range(n):
        variant=random.choice(['control','treatment'])
        event=random.choices(['impression','click','purchase'],[.78,.17,.05])[0]
        channel=random.choice(['search','social','email','display'])
        rows.append({'event_time':start+timedelta(seconds=random.randint(0,604800)),
                     'customer_id':f'C{random.randint(1,4000):05d}','campaign_id':f'CAM{random.randint(1,8):02d}',
                     'variant':variant,'channel':channel,'event':event,
                     'spend':round(random.uniform(.01,3),2) if event!='impression' else round(random.uniform(.001,.2),3),
                     'revenue':round(random.uniform(15,250),2) if event=='purchase' else 0})
    return pd.DataFrame(rows)

if __name__=='__main__':
    generate().to_csv('data/events.csv',index=False)
