import os
from openai import OpenAI

def summarize(kpi_table):
    client=OpenAI(api_key=os.environ['OPENAI_API_KEY'])
    prompt='Summarize the campaign KPI table. Use only supplied numbers. Identify anomalies and next questions.\n'+kpi_table
    return client.responses.create(model=os.getenv('OPENAI_MODEL','gpt-5.6-luna'),input=prompt).output_text
