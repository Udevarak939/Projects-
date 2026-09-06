import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(page_title='Amazon Real-Time Analytics', layout='wide')
st.title('Amazon-Style Real-Time Commerce Analytics')
path = Path('data/orders.csv')
if not path.exists():
    st.info('Run: python src/generate_orders.py')
    st.stop()
df = pd.read_csv(path, parse_dates=['event_time'])
df['revenue'] = df.quantity * df.unit_price
completed = df[df.status.eq('completed')]
c1,c2,c3,c4 = st.columns(4)
c1.metric('Revenue', f"${completed.revenue.sum():,.0f}")
c2.metric('Orders', f"{completed.order_id.nunique():,}")
c3.metric('AOV', f"${completed.revenue.sum()/max(completed.order_id.nunique(),1):,.2f}")
c4.metric('Cancellation', f"{100*df.status.eq('cancelled').mean():.1f}%")
series = completed.set_index('event_time').resample('15min').revenue.sum()
st.line_chart(series)
st.subheader('Product Revenue')
st.bar_chart(completed.groupby('product').revenue.sum().sort_values(ascending=False))
