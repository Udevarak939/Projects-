# Amazon Real-Time E-Commerce Analytics

Portfolio project simulating an Amazon-scale real-time commerce analytics workflow. It demonstrates SQL, Python, streaming concepts, customer analytics, KPI monitoring, anomaly detection, and business recommendations.

## Business Questions
- Which products and categories drive revenue?
- What are conversion, average order value, and cancellation rates?
- Which customers are high-value or at risk?
- Which events indicate demand or revenue anomalies?
- How can inventory and promotions be prioritized?

## Architecture
Event generator -> Kafka -> Spark Structured Streaming -> PostgreSQL -> analytics SQL -> Streamlit dashboard

The repository includes a lightweight local mode so the analytics can be demonstrated without external services.

## Step-by-Step
1. Create a Python 3.11 environment.
2. Install `pip install -r requirements.txt`.
3. Run `python src/generate_orders.py` to create realistic order events.
4. Run `python src/analytics.py` to calculate revenue, AOV, conversion, cancellations, customer segments, and anomaly flags.
5. Load the generated CSV into PostgreSQL using `sql/schema.sql` and `sql/kpis.sql`.
6. Run `streamlit run dashboard/app.py`.
7. For streaming architecture, start Kafka/Postgres with `docker compose up -d` and adapt the event generator to publish to Kafka.

## Portfolio Highlights
- Windowed KPI calculations
- Customer segmentation and RFM-style scoring
- Revenue anomaly detection using rolling statistics
- Reproducible synthetic data generation
- SQL-first analytics layer
- Dashboard-ready outputs

## Suggested Resume Bullet
Built an end-to-end Amazon-style real-time commerce analytics pipeline using Python, SQL, Kafka/Spark concepts, PostgreSQL and Streamlit to monitor revenue, conversion, customer value, cancellations and demand anomalies.