# Financial Business Analytics Platform

End-to-end financial analytics project designed around a real-world Financial Business Analyst workflow: ingest transaction data, validate and transform it, calculate finance KPIs, investigate variances, forecast revenue and operating expense, run what-if scenarios, and publish executive-ready insights.

## Business problem

A multi-region digital business needs a repeatable view of financial performance across products, regions, channels, and customer segments. Finance and business leaders need answers to:

- Are actual results tracking to budget and forecast?
- What explains revenue, gross-margin, and operating-expense variance?
- Which products, regions, and channels are driving growth or pressure?
- How do pricing, volume, and cost assumptions change next-quarter outlook?
- Which metrics should executives review weekly?

## End-to-end architecture

```
CSV / simulated ERP extracts
        |
        v
Python data ingestion + validation
        |
        v
PostgreSQL analytical schema
        |
        +--> SQL KPI layer
        |      - Revenue
        |      - Gross Profit / Margin
        |      - Opex
        |      - EBITDA
        |      - Budget variance
        |      - YoY growth
        |
        +--> Python analytics
        |      - Driver analysis
        |      - Forecasting
        |      - Scenario modeling
        |
        v
Power BI / Tableau executive dashboard
        |
        v
Business recommendations
```

## Data model

**Dimensions**
- `dim_date`
- `dim_product`
- `dim_region`
- `dim_channel`
- `dim_customer_segment`

**Facts**
- `fact_financials`: actuals, budget, prior-year, units, revenue, COGS, opex
- `fact_transactions`: order-level revenue transactions

## Key KPIs

| KPI | Definition |
|---|---|
| Revenue | Gross sales less discounts/refunds |
| Gross Profit | Revenue - COGS |
| Gross Margin % | Gross Profit / Revenue |
| Operating Expense | Sales + marketing + G&A + other operating costs |
| EBITDA | Gross Profit - Operating Expense |
| Budget Variance | Actual - Budget |
| Budget Variance % | (Actual - Budget) / Budget |
| YoY Growth % | (Current period - prior period) / prior period |
| Average Order Value | Revenue / Orders |
| Revenue per Customer | Revenue / Active Customers |

## Project workflow

1. Generate realistic monthly financial and transaction data.
2. Validate schema, nulls, duplicate business keys, negative values, and reconciliation totals.
3. Load clean data into PostgreSQL.
4. Build SQL views for monthly, regional, product, and channel performance.
5. Use Python for variance-driver analysis and rolling forecasts.
6. Run base/upside/downside scenarios.
7. Publish a finance executive dashboard with drill-downs.
8. Document findings as a concise business review.

## Repository structure

```
financial-business-analytics-platform/
├── README.md
├── data/
│   ├── financial_actuals.csv
│   └── transactions.csv
├── sql/
│   ├── 01_schema.sql
│   ├── 02_kpi_views.sql
│   └── 03_variance_analysis.sql
├── python/
│   └── financial_analysis.py
└── dashboard/
    └── dashboard_spec.md
```

## Example business questions answered

- Which region caused the largest unfavorable revenue variance?
- Was margin pressure caused by lower prices, lower volume, or higher COGS?
- Which products are growing while remaining above margin targets?
- What is the next 3-month revenue outlook?
- What would happen to EBITDA under +5% volume, -2% price, or +3% COGS scenarios?

## Analyst deliverables

- Reconciled finance-ready dataset
- Reusable SQL KPI layer
- Variance bridge / driver analysis
- Rolling revenue forecast
- Scenario model
- Executive dashboard specification
- Management-ready findings

> The data in this repository is synthetic and is intended for portfolio demonstration only.
