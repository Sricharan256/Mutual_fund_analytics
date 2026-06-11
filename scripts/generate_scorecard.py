"""
Bluestock Mutual Fund Analytics

Script: generate_scorecard.py

Purpose:
Generate a consolidated mutual fund scorecard
containing performance and risk metrics.

Author: Sricharan Medaboina
"""
import pandas as pd

performance = pd.read_csv(
    "data/processed/07_scheme_performance_clean.csv"
)

ratios = pd.read_csv(
    "data/processed/sharpe_sortino.csv"
)

alpha_beta = pd.read_csv(
    "data/processed/alpha_beta.csv"
)

dd = pd.read_csv(
    "data/processed/max_drawdown.csv"
)

scorecard = (
    performance
    .merge(ratios, on="amfi_code")
    .merge(alpha_beta, on="amfi_code")
    .merge(dd, on="amfi_code")
)

print(scorecard.columns.tolist())

scorecard["score"] = (
      scorecard["return_3yr_pct"].rank(pct=True) * 30
    + scorecard["sharpe_ratio_y"].rank(pct=True) * 25
    + scorecard["alpha_y"].rank(pct=True) * 20
    + scorecard["expense_ratio_pct"].rank(
          ascending=False,
          pct=True
      ) * 15
    + scorecard["max_drawdown"].rank(
          ascending=False,
          pct=True
      ) * 10
)

scorecard.to_csv(
    "data/processed/fund_scorecard.csv",
    index=False
)

print("Fund Scorecard generated successfully")