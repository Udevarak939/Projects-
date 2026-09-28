import streamlit as st,pandas as pd
st.title('AI Marketing Intelligence Agent'); df=pd.read_csv('data/campaign_kpis_scored.csv'); st.dataframe(df,use_container_width=True); st.subheader('Evidence-grounded summary');
for _,r in df.iterrows(): st.write(f"**{r['campaign']}** — ROAS {r['ROAS']:.2f}, CTR {r['CTR']:.2%}, CVR {r['CVR']:.2%}" + (' ⚠️ anomaly' if r['anomaly'] else ''))
