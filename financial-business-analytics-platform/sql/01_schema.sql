CREATE TABLE dim_date (
  month DATE PRIMARY KEY
);

CREATE TABLE fact_financials (
  month DATE NOT NULL,
  region VARCHAR(30) NOT NULL,
  product VARCHAR(60) NOT NULL,
  channel VARCHAR(30) NOT NULL,
  customer_segment VARCHAR(30) NOT NULL,
  actual_revenue NUMERIC(14,2) NOT NULL,
  budget_revenue NUMERIC(14,2) NOT NULL,
  prior_year_revenue NUMERIC(14,2) NOT NULL,
  cogs NUMERIC(14,2) NOT NULL,
  opex NUMERIC(14,2) NOT NULL
);

CREATE TABLE fact_transactions (
  transaction_id VARCHAR(20) PRIMARY KEY,
  transaction_date DATE NOT NULL,
  region VARCHAR(30) NOT NULL,
  product VARCHAR(60) NOT NULL,
  channel VARCHAR(30) NOT NULL,
  customer_segment VARCHAR(30) NOT NULL,
  orders INTEGER NOT NULL,
  units INTEGER NOT NULL,
  revenue NUMERIC(14,2) NOT NULL,
  cogs NUMERIC(14,2) NOT NULL
);

CREATE INDEX idx_financials_month_region
  ON fact_financials(month, region);

CREATE INDEX idx_transactions_date
  ON fact_transactions(transaction_date);
