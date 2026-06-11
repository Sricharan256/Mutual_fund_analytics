
"""
Bluestock Mutual Fund Analytics

Script: calculate_sharpe_sortino.py

Purpose:
Calculate Sharpe and Sortino ratios for all mutual fund schemes.

Author: Sricharan Medaboina
"""
import pandas as pd
import numpy as np

nav = pd.read_csv(
    "data/processed/nav_daily_returns.csv"
)

rf = 0.065

results = []

for code in nav["amfi_code"].unique():

    returns = (
        nav[
            nav["amfi_code"] == code
        ]["daily_return"]
        .dropna()
    )

    annual_return = (
        returns.mean() * 252
    )

    annual_std = (
        returns.std() * np.sqrt(252)
    )

    sharpe = (
        annual_return - rf
    ) / annual_std

    downside = returns[
        returns < 0
    ]

    downside_std = (
        downside.std()
        * np.sqrt(252)
    )

    sortino = (
        annual_return - rf
    ) / downside_std

    results.append(
        [
            code,
            sharpe,
            sortino
        ]
    )

ratios = pd.DataFrame(
    results,
    columns=[
        "amfi_code",
        "sharpe_ratio",
        "sortino_ratio"
    ]
)

ratios.to_csv(
    "data/processed/sharpe_sortino.csv",
    index=False
)

print("Sharpe and Sortino calculated")