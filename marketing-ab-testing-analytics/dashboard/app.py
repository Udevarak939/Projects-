import streamlit as st
import pandas as pd
from pathlib import Path
st.set_page_config(page_title='Campaign Experiment Analytics',layout='wide')
st.title('Real-Time Marketing & A/B Testing Analytics')
p=Path('data/events.csv')
if not p.exists(): st.info('Run: python src/generate_events.py'); st.stop()
df=pd.read_csv(p)
imp=df[df.event.eq('impression')].groupby('variant').size()
pur=df[df.event.eq('purchase')].groupby('variant').size()
rev=df.groupby('variant').revenue.sum(); spend=df.groupby('variant').spend.sum()
for v in ['control','treatment']:
    st.metric(v.title()+' conversion',f"{pur.get(v,0)/max(imp.get(v,1),1):.2%}")
st.metric('Treatment uplift',f"{(pur.get('treatment',0)/max(imp.get('treatment',1),1))/(pur.get('control',0)/max(imp.get('control',1),1))-1:.2%}")
st.subheader('ROAS by channel')
ch=df.groupby('channel').agg(revenue=('revenue','sum'),spend=('spend','sum')); ch['ROAS']=ch.revenue/ch.spend
st.bar_chart(ch.ROAS.sort_values(ascending=False))
