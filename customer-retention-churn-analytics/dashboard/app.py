import streamlit as st
import pandas as pd
from pathlib import Path
from src.churn_model import train, score_customers
st.set_page_config(page_title='Customer Retention Analytics',layout='wide')
st.title('Real-Time Customer Retention & Churn Analytics')
p=Path('data/customers.csv')
if not p.exists(): st.info('Run: python src/generate_customers.py'); st.stop()
df=pd.read_csv(p)
model,auc=train(df)
out=score_customers(model,df)
c1,c2,c3=st.columns(3)
c1.metric('Customers',f"{len(df):,}")
c2.metric('Churn rate',f"{df.churned.mean():.1%}")
c3.metric('Model ROC-AUC',f"{auc:.2f}")
st.subheader('Highest-value churn risks')
st.dataframe(out[['customer_id','avg_order_value','days_since_last_activity','churn_probability','priority']].head(25),use_container_width=True)
st.subheader('Churn rate by inactivity')
bins=[0,7,30,60,999]; labels=['0-7','8-30','31-60','61+']
df['bucket']=pd.cut(df.days_since_last_activity,bins=bins,labels=labels)
st.bar_chart(df.groupby('bucket',observed=False).churned.mean())
