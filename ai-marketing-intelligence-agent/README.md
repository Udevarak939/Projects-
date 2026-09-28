# AI Marketing Intelligence Agent

An end-to-end Data Analyst + AI project that combines campaign analytics, SQL, Python, LLM summarization, KPI reasoning, and automated insight generation.

## Business Problem
Marketing teams often have dashboards but still spend hours interpreting campaign performance. This project converts campaign and funnel data into KPI analysis, anomaly flags, and natural-language business insights.

## End-to-End Architecture
`Campaign CSV/API -> Python validation -> PostgreSQL -> KPI SQL -> anomaly detection -> LLM insight layer -> Streamlit dashboard`

## Analytics
- Impressions, clicks, conversions
- CTR, CVR, CAC, ROAS
- Funnel drop-off
- Channel and cohort comparison
- Week-over-week performance
- Spend/revenue anomalies
- Campaign-level opportunity detection

## AI Layer
- LLM converts KPI tables into concise analyst-style commentary
- Structured prompts enforce KPI definitions and reporting periods
- Evidence-first generation: responses cite the underlying KPI rows used for each insight
- Guardrails prevent unsupported numeric claims
- Optional function-calling pattern for retrieving approved KPI queries

## Dashboard
- Executive campaign scorecard
- Funnel visualization
- Channel comparison
- Anomaly panel
- AI-generated weekly business summary
- Drill-down from insight -> KPI evidence

## Suggested repository structure
```text
ai-marketing-intelligence-agent/
├── data/
├── sql/
│   ├── campaign_kpis.sql
│   └── funnel_analysis.sql
├── src/
│   ├── generate_campaigns.py
│   ├── validate_data.py
│   ├── analytics.py
│   ├── anomaly_detection.py
│   └── llm_insights.py
├── dashboard/
│   └── app.py
├── prompts/
│   └── campaign_summary.txt
├── requirements.txt
└── README.md
```

## Run
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python src/generate_campaigns.py
python src/validate_data.py
python src/analytics.py
python src/anomaly_detection.py
streamlit run dashboard/app.py
```

Configure your approved LLM provider using environment variables; never commit API keys.

## Resume-ready impact
Built an AI marketing analytics agent that transformed campaign KPIs into evidence-grounded natural-language insights, combining PostgreSQL, Python, anomaly detection, LLM prompting, and Streamlit to accelerate recurring performance analysis.


## Dataset
Uses the real **UCI Bank Marketing** dataset. The UCI repository documents 45,211 campaign records from direct marketing campaigns of a Portuguese banking institution, with the target indicating whether a client subscribed to a term deposit. The download script retrieves the dataset at runtime. citeturn0search3
