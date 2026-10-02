CREATE OR REPLACE VIEW v_monthly_financial_kpis AS
SELECT
  month,
  SUM(actual_revenue) AS revenue,
  SUM(budget_revenue) AS budget_revenue,
  SUM(actual_revenue - budget_revenue) AS budget_variance,
  ROUND(
    100.0 * SUM(actual_revenue - budget_revenue) / NULLIF(SUM(budget_revenue), 0),
    2
  ) AS budget_variance_pct,
  SUM(cogs) AS cogs,
  SUM(actual_revenue - cogs) AS gross_profit,
  ROUND(
    100.0 * SUM(actual_revenue - cogs) / NULLIF(SUM(actual_revenue), 0),
    2
  ) AS gross_margin_pct,
  SUM(opex) AS opex,
  SUM(actual_revenue - cogs - opex) AS ebitda,
  ROUND(
    100.0 * SUM(actual_revenue - cogs - opex)
      / NULLIF(SUM(actual_revenue), 0),
    2
  ) AS ebitda_margin_pct,
  ROUND(
    100.0 * (SUM(actual_revenue) - SUM(prior_year_revenue))
      / NULLIF(SUM(prior_year_revenue), 0),
    2
  ) AS yoy_growth_pct
FROM fact_financials
GROUP BY month;

CREATE OR REPLACE VIEW v_region_performance AS
SELECT
  region,
  SUM(actual_revenue) AS revenue,
  SUM(budget_revenue) AS budget,
  SUM(actual_revenue - budget_revenue) AS variance,
  ROUND(
    100.0 * SUM(actual_revenue - budget_revenue)
      / NULLIF(SUM(budget_revenue), 0),
    2
  ) AS variance_pct,
  ROUND(
    100.0 * SUM(actual_revenue - cogs)
      / NULLIF(SUM(actual_revenue), 0),
    2
  ) AS gross_margin_pct,
  SUM(actual_revenue - cogs - opex) AS ebitda
FROM fact_financials
GROUP BY region;

CREATE OR REPLACE VIEW v_product_performance AS
SELECT
  product,
  channel,
  customer_segment,
  SUM(actual_revenue) AS revenue,
  SUM(cogs) AS cogs,
  SUM(actual_revenue - cogs) AS gross_profit,
  ROUND(
    100.0 * SUM(actual_revenue - cogs)
      / NULLIF(SUM(actual_revenue), 0),
    2
  ) AS gross_margin_pct
FROM fact_financials
GROUP BY product, channel, customer_segment;
