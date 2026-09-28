import streamlit as st, pandas as pd
st.set_page_config(page_title='AI Customer Insights',layout='wide'); st.title('AI-Powered Customer Insights')
df=pd.read_csv('data/customers.csv'); c1,c2,c3=st.columns(3); c1.metric('Customers',len(df)); c2.metric('Revenue',f"${df.spend.sum():,.0f}"); c3.metric('Churn Risk',f"{df.churn.mean():.1%}")
st.dataframe(df.sort_values('days_since_order',ascending=False).head(50),use_container_width=True)
