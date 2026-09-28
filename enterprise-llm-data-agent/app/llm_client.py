import os
from openai import OpenAI

def generate_insight(question,evidence):
    client=OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))
    response=client.responses.create(model=os.environ.get('OPENAI_MODEL','gpt-5.6-luna'),input=f"You are an enterprise data analyst. Answer only from the evidence below.\nQuestion: {question}\nEvidence: {evidence}\nReturn: finding, KPI evidence, caveat, next investigation.")
    return response.output_text
