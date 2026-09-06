import random
import pandas as pd

def generate(n=3000,seed=11):
    random.seed(seed); rows=[]
    for i in range(n):
        sessions=random.randint(0,35); orders=random.randint(0,12)
        aov=round(random.uniform(20,400),2); inactive=random.randint(1,120)
        tickets=random.randint(0,6)
        churned=int(inactive>75 and sessions<8)
        rows.append({'customer_id':f'C{i:05d}','sessions_30d':sessions,'orders_90d':orders,
                     'avg_order_value':aov,'days_since_last_activity':inactive,
                     'support_tickets':tickets,'churned':churned})
    return pd.DataFrame(rows)

if __name__=='__main__': generate().to_csv('data/customers.csv',index=False)
