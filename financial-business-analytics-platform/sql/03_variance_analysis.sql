WITH monthly AS (
  SELECT
    month,
    region,
    product,
    actual_revenue,
    budget_revenue,
    actual_revenue - budget_revenue AS variance
  FROM fact_financials
)
SELECT
  month,
  region,
  product,
  actual_revenue,
  budget_revenue,
  variance,
  ROUND(100.0 * variance / NULLIF(budget_revenue, 0), 2) AS variance_pct,
  CASE
    WHEN variance < 0 THEN 'Unfavorable'
    WHEN variance > 0 THEN 'Favorable'
    ELSE 'On Budget'
  END AS variance_flag
FROM monthly
ORDER BY month, variance ASC;

SELECT
  region,
  SUM(variance) AS total_variance
FROM (
  SELECT
    region,
    actual_revenue - budget_revenue AS variance
  FROM fact_financials
) x
GROUP BY region
ORDER BY total_variance;
