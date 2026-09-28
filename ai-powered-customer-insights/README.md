# AI-Powered Customer Insights & Analytics

An end-to-end Data Analyst project that combines SQL, Python, machine learning, explainable AI, and business intelligence to turn customer behavior into retention and revenue actions.

## Business Problem
Identify high-value customers, churn risk, behavioral segments, and the drivers behind declining engagement so business teams can prioritize actions.

## End-to-End Architecture
`CSV/SQL sources -> Python validation -> PostgreSQL -> feature engineering -> ML scoring -> SHAP explanations -> KPI layer -> Streamlit dashboard`

## Key Analytics
- Customer Lifetime Value (CLV)
- Recency, Frequency, Monetary (RFM)
- Cohort retention
- Revenue and order trends
- Churn-risk scoring
- Segment-level KPI analysis
- Driver analysis using SHAP

## AI/ML
- Gradient Boosting / Logistic Regression baseline
- Probability-based churn risk
- SHAP-based feature explanations
- Threshold-based customer action buckets
- Model evaluation with precision, recall, F1 and ROC-AUC

## Dashboard
The Streamlit app surfaces:
- Executive KPI cards
- Revenue and retention trends
- Customer segments
- High-risk customer list
- Top churn drivers
- Action recommendations

## Suggested repository structure
```text
ai-powered-customer-insights/
├── data/
├── sql/
│   └── customer_kpis.sql
├── src/
│   ├── generate_data.py
│   ├── validate_data.py
│   ├── feature_engineering.py
│   ├── train_model.py
│   └── explain_model.py
├── dashboard/
│   └── app.py
├── notebooks/
├── requirements.txt
└── README.md
```

## Run
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python src/generate_data.py
python src/validate_data.py
python src/feature_engineering.py
python src/train_model.py
python src/explain_model.py
streamlit run dashboard/app.py
```

## Resume-ready impact
Built an end-to-end AI-assisted customer analytics platform combining SQL, Python, ML, SHAP, and Streamlit to segment customers, score churn risk, explain model drivers, and convert behavioral signals into retention actions.


## Dataset
Uses the real **UCI Bank Marketing** dataset. The UCI repository documents 45,211 campaign records from direct marketing campaigns of a Portuguese banking institution, with the target indicating whether a client subscribed to a term deposit. The download script retrieves the dataset at runtime. citeturn0search3
