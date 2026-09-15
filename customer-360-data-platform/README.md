# Customer 360 Data & AI Platform

End-to-end e-commerce data engineering and analytics platform built on the real **Brazilian E-Commerce by Olist** dataset. The project demonstrates ingestion, data quality, PySpark ETL, AWS S3/Glue design, Snowflake/dbt modeling, advanced SQL, Power BI-ready marts, and customer analytics/ML.

## Architecture

```text
Olist CSV Dataset
      |
      v
Python ingestion + validation
      |
      v
AWS S3 (raw / silver / gold)
      |
      v
AWS Glue / PySpark ETL
      |
      v
Snowflake Warehouse
      |
      v
DBT staging -> intermediate -> marts
      |
      +------------------+------------------+
      v                  v                  v
Power BI / DAX      SQL Analytics      ML / Forecasting

Local development: PostgreSQL + Docker can be used as the serving database.
```

## Real Dataset

**Brazilian E-Commerce Public Dataset by Olist**: approximately 100K orders across customers, products, sellers, payments, reviews and geolocation. Download the dataset from Kaggle and place the CSV files under `data/raw/`.

Do not commit the downloaded dataset or credentials to GitHub. `.gitignore` excludes local data and secret files.

## What this project demonstrates

- Python, Pandas and NumPy for ingestion, profiling and validation
- PySpark for scalable ETL and feature engineering
- AWS S3 + AWS Glue architecture for cloud data engineering
- Snowflake-ready dimensional warehouse design
- dbt staging, marts and data-quality tests
- Advanced SQL: CTEs, window functions, cohorts and KPI marts
- PostgreSQL for local serving and development
- Power BI/DAX-ready gold tables
- Customer segmentation, churn prediction and anomaly detection
- Time-series revenue analysis and forecasting foundations
- Business requirements and Agile delivery documentation

## Project structure

```text
customer-360-data-platform/
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
├── architecture/
│   └── architecture.md
├── ingestion/
│   ├── download_dataset.py
│   └── validate_data.py
├── spark_etl/
│   └── olist_etl.py
├── sql/
│   ├── schema.sql
│   └── business_queries.sql
├── dbt_customer360/
│   ├── dbt_project.yml
│   ├── profiles.yml.example
│   ├── models/staging/stg_orders.sql
│   ├── models/marts/fct_customer_360.sql
│   ├── models/marts/dim_customer.sql
│   └── models/schema.yml
├── ml/
│   └── customer_models.py
└── docs/
    ├── business_requirements.md
    └── agile_delivery.md
```

## Local quick start

1. Download the Olist dataset from Kaggle and extract its CSV files into `data/raw/`.
2. Create a virtual environment and run `pip install -r requirements.txt`.
3. Run `python ingestion/validate_data.py` to profile and validate the source files.
4. Run `python spark_etl/olist_etl.py --input data/raw --output data/processed`.
5. Load the generated gold CSVs into PostgreSQL or Snowflake.
6. Run the dbt models with a configured Snowflake profile.
7. Run `python ml/customer_models.py --input data/processed/customer_360.csv` for customer scoring.

## Cloud deployment pattern

For AWS, upload `data/raw` to S3, register the raw zone with an AWS Glue crawler, execute the PySpark transformation as a Glue job, and load the gold layer into Snowflake. Credentials should be supplied through AWS IAM roles, environment variables or the relevant secret manager; never hard-code them in source files.

## Important engineering note

The repository contains the **pipeline and reproducible project code**, not the Olist dataset itself. This keeps the GitHub repository lightweight and avoids redistributing a third-party dataset.
