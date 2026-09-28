import streamlit as st
from app.agent import analyst_plan
st.title('Enterprise LLM Data Analyst Agent'); q=st.text_input('Ask a business question');
if q: st.json(analyst_plan(q)); st.info('Connect this planner to an approved LLM provider and read-only database tool using environment variables; never commit API keys.')
