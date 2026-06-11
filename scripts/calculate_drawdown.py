
"""
Bluestock Mutual Fund Analytics

Script: calculate_drawdown.py

Purpose:
Calculate Maximum Drawdown for all mutual fund schemes.

Author: Sricharan Medaboina
"""

import pandas as pd

nav = pd.read_csv(
    "data/processed/nav_daily_returns.csv"
)

results = []

for code in nav["amfi_code"].unique():

    temp = nav[
        nav["amfi_code"] == code
    ]

    running_max = (
        temp["nav"]
        .cummax()
    )

    drawdown = (
        temp["nav"]
        /
        running_max
    ) - 1

    results.append(
        [
            code,
            drawdown.min()
        ]
    )

dd = pd.DataFrame(
    results,
    columns=[
        "amfi_code",
        "max_drawdown"
    ]
)

dd.to_csv(
    "data/processed/max_drawdown.csv",
    index=False
)

print("Maximum Drawdown completed")