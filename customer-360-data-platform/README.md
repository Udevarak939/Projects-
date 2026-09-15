# Customer 360 Data & AI Platform

A reproducible, end-to-end portfolio implementation using the real Brazilian E-Commerce by Olist dataset.

## End-to-end flow
`Olist CSV -> Python validation -> S3 raw -> PySpark/Glue ETL -> Snowflake RAW -> dbt staging/marts -> SQL analytics -> Power BI/DAX -> ML + forecasting`

The repository contains the code, schemas, transformations, analytics and deployment configuration. The third-party Olist CSV data and cloud credentials are intentionally not committed.

## Run locally
```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python ingestion/validate_data.py --input data/raw
python ingestion/profile_data.py
python spark_etl/olist_etl.py --input data/raw --output data/processed
python ml/customer_models.py --input data/processed/customer_360.csv --output data/gold/customer_scores.csv
python forecasting/revenue_forecast.py --input data/raw --output data/gold/monthly_revenue.csv
python stats/business_statistics.py --input data/raw
```

For the Spark job, `spark_etl/olist_etl.py` produces the same local gold table consumed by ML. For a cloud run, use the AWS uploader and Glue-compatible deployment pattern documented in `architecture/architecture.md`.

## AWS/Snowflake run
1. Configure AWS credentials using your normal IAM profile/role and set `S3_BUCKET`.
2. `python cloud/s3_upload.py --local-dir data/raw --bucket $S3_BUCKET --prefix olist/raw`.
3. Run the PySpark transformation in AWS Glue using the same business transformations.
4. Execute `sql/schema.sql` in Snowflake to create `OLIST_DWH.RAW` and `OLIST_DWH.ANALYTICS`.
5. Load Glue output into the Snowflake RAW tables using Snowpipe, COPY INTO, or your approved ingestion mechanism.
6. Copy `dbt_customer360/profiles.yml.example` to `profiles.yml`, configure environment variables, then run `dbt debug`, `dbt run`, and `dbt test`.
7. Connect Power BI to the analytics schema and implement the measures in `dashboard/powerbi/README.md`.

## Project outputs
- `data/processed/customer_360.csv`: customer-level gold table
- `data/gold/customer_scores.csv`: segmentation + churn-proxy scoring
- `data/gold/monthly_revenue.csv`: monthly revenue and rolling trend features

## Important modeling note
The dataset does not contain a true observed churn label. The ML script therefore creates an explicitly named `churn_proxy` for portfolio demonstration. Any model metric printed by the script is generated from the real dataset at runtime; no performance numbers are fabricated or hard-coded.

## Repository structure
```text
architecture/       architecture and security design
cloud/              S3 upload / cloud execution helpers
dashboard/powerbi/  Power BI model + DAX guide
dbt_customer360/   dbt project, sources, staging and marts
docs/               BRD and Agile delivery artifacts
ingestion/          validation and profiling
ml/                 segmentation and churn-proxy model
forecasting/        time-series revenue features
spark_etl/          PySpark transformation
sql/                Snowflake DDL + business queries
stats/              statistical hypothesis analysis
```
