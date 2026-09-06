from datetime import datetime, timedelta, timezone
import random
import pandas as pd

PRODUCTS = [('Laptop',899),('Headphones',149),('Monitor',299),('Keyboard',79),('SSD',119)]

def generate(n=5000, seed=42):
    random.seed(seed)
    start = datetime.now(timezone.utc) - timedelta(hours=24)
    rows=[]
    for i in range(n):
        product, price = random.choice(PRODUCTS)
        qty = random.choices([1,2,3], weights=[.8,.17,.03])[0]
        rows.append({'event_time': start + timedelta(seconds=random.randint(0,86400)),
                     'order_id': f'O{i:07d}', 'customer_id': f'C{random.randint(1,1200):05d}',
                     'product': product, 'quantity': qty,
                     'unit_price': round(price * random.uniform(.85,1.15),2),
                     'status': random.choices(['completed','cancelled'], weights=[.94,.06])[0]})
    return pd.DataFrame(rows).sort_values('event_time')

if __name__ == '__main__':
    generate().to_csv('data/orders.csv', index=False)
    print('Wrote data/orders.csv')
