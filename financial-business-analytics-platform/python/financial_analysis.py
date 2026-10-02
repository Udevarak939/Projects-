"""Financial Business Analytics — driver analysis, forecasting, and scenarios."""

from pathlib import Path
import pandas as pd

BASE = Path(__file__).resolve().parents[1]
df = pd.read_csv(BASE / "data" / "financial_actuals.csv", parse_dates=["month"])

# Core finance metrics
df["gross_profit"] = df["actual_revenue"] - df["cogs"]
df["gross_margin_pct"] = df["gross_profit"] / df["actual_revenue"]
df["budget_variance"] = df["actual_revenue"] - df["budget_revenue"]
df["budget_variance_pct"] = df["budget_variance"] / df["budget_revenue"]
df["ebitda"] = df["gross_profit"] - df["opex"]

monthly = (
    df.groupby("month", as_index=False)
      .agg(
          revenue=("actual_revenue", "sum"),
          budget=("budget_revenue", "sum"),
          prior_year=("prior_year_revenue", "sum"),
          cogs=("cogs", "sum"),
          opex=("opex", "sum"),
          ebitda=("ebitda", "sum"),
      )
)

monthly["variance"] = monthly["revenue"] - monthly["budget"]
monthly["variance_pct"] = monthly["variance"] / monthly["budget"]
monthly["yoy_growth_pct"] = monthly["revenue"].pct_change()

# 3-month rolling average used as a simple portfolio forecast baseline.
monthly["forecast_3m_avg"] = monthly["revenue"].rolling(3).mean()

# Scenario model on latest observed month.
latest = monthly.iloc[-1]
base_revenue = float(latest["revenue"])
base_cogs = float(latest["cogs"])
base_opex = float(latest["opex"])

scenarios = pd.DataFrame(
    [
        {"scenario": "Downside", "volume_change": -0.05, "price_change": -0.02, "cogs_change": 0.03},
        {"scenario": "Base", "volume_change": 0.00, "price_change": 0.00, "cogs_change": 0.00},
        {"scenario": "Upside", "volume_change": 0.05, "price_change": 0.02, "cogs_change": -0.02},
    ]
)

scenarios["scenario_revenue"] = base_revenue * (1 + scenarios["volume_change"]) * (
    1 + scenarios["price_change"]
)
scenarios["scenario_cogs"] = base_cogs * (1 + scenarios["cogs_change"])
scenarios["scenario_ebitda"] = scenarios["scenario_revenue"] - scenarios["scenario_cogs"] - base_opex
scenarios["ebitda_delta"] = scenarios["scenario_ebitda"] - (base_revenue - base_cogs - base_opex)

# Driver ranking: identify business areas contributing to total revenue variance.
drivers = (
    df.groupby(["region", "product"], as_index=False)["budget_variance"]
      .sum()
      .sort_values("budget_variance")
)

print("=== Monthly KPI Summary ===")
print(monthly.round(2).to_string(index=False))

print("\n=== Scenario Analysis ===")
print(scenarios.round(2).to_string(index=False))

print("\n=== Variance Drivers ===")
print(drivers.round(2).to_string(index=False))
