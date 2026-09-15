# Customer 360 Architecture

## End-to-end flow

```text
Olist public dataset
       |
       v
Python ingestion + validation
       |
       v
S3 raw zone
       |
       v
AWS Glue / PySpark
       |
       +---- data quality checks
       |
       v
S3 silver/gold
       |
       v
Snowflake warehouse
       |
       v
DBT transformations + tests
       |
       +----------+-----------+
       |          |           |
       v          v           v
   Power BI   SQL marts     ML models
```

## Security

- No credentials are stored in source code.
- Local secrets belong in `.env`, which is ignored by Git.
- AWS workloads should use IAM roles instead of long-lived access keys where possible.
- Snowflake credentials should be supplied through environment variables or a managed secret store.
- Public datasets are kept outside the repository.
