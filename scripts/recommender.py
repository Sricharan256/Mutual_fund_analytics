"""
Bluestock Mutual Fund Analytics

Script: recommender.py

Purpose:
Recommend top mutual fund schemes based on
investor risk appetite and Sharpe Ratio rankings.

Author: Sricharan Medaboina
"""
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

performance = pd.read_csv(
    BASE_DIR / "data" / "processed" / "07_scheme_performance_clean.csv"
)

print("Available Risk Grades:")
print(performance["risk_grade"].value_counts())

risk = input(
    "\nEnter Risk Appetite (Low/Moderate/High): "
)

risk_mapping = {
    "Low": ["Low"],
    "Moderate": ["Moderate"],
    "High": ["High", "Very High", "Moderately High"]
}

selected_grades = risk_mapping.get(
    risk,
    [risk]
)

recommendations = (
    performance[
        performance["risk_grade"]
        .isin(selected_grades)
    ]
    .sort_values(
        "sharpe_ratio",
        ascending=False
    )
    .head(3)
)

print("\n=== Top 3 Recommended Funds ===\n")

print(
    recommendations[
        [
            "scheme_name",
            "fund_house",
            "risk_grade",
            "sharpe_ratio",
            "return_3yr_pct"
        ]
    ]
)