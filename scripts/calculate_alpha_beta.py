"""
Bluestock Mutual Fund Analytics

Script: calculate_alpha_beta.py

Purpose:
Calculate Alpha and Beta metrics for all mutual fund schemes
by comparing fund returns with benchmark returns.

Author: Sricharan Medaboina
"""
import pandas as pd
from scipy.stats import linregress

nav = pd.read_csv(
    "data/processed/nav_daily_returns.csv"
)

benchmark = pd.read_csv(
    "data/processed/10_benchmark_indices_clean.csv"
)

nav["date"] = pd.to_datetime(
    nav["date"]
)

benchmark["date"] = pd.to_datetime(
    benchmark["date"]
)

nifty100 = benchmark[
    benchmark["index_name"] == "NIFTY100"
].copy()

nifty100["benchmark_return"] = (
    nifty100["close_value"]
    .pct_change()
)

results = []

for code in nav["amfi_code"].unique():

    fund = nav[
        nav["amfi_code"] == code
    ][["date", "daily_return"]]

    merged = pd.merge(
        fund,
        nifty100[
            ["date", "benchmark_return"]
        ],
        on="date"
    ).dropna()

    if len(merged) > 10:

        slope, intercept, r, p, std = (
            linregress(
                merged["benchmark_return"],
                merged["daily_return"]
            )
        )

        results.append(
            [
                code,
                intercept * 252,
                slope
            ]
        )

alpha_beta = pd.DataFrame(
    results,
    columns=[
        "amfi_code",
        "alpha",
        "beta"
    ]
)

alpha_beta.to_csv(
    "data/processed/alpha_beta.csv",
    index=False
)

print("Alpha Beta completed")