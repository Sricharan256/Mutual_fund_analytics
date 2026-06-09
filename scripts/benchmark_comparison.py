import pandas as pd
import matplotlib.pyplot as plt

nav = pd.read_csv(
    "data/processed/nav_daily_returns.csv"
)

scorecard = pd.read_csv(
    "data/processed/fund_scorecard.csv"
)

nav["date"] = pd.to_datetime(
    nav["date"]
)

top5 = (
    scorecard
    .sort_values(
        "score",
        ascending=False
    )
    .head(5)
)

plt.figure(figsize=(15,8))

for code in top5["amfi_code"]:

    temp = nav[
        nav["amfi_code"] == code
    ]

    plt.plot(
        temp["date"],
        temp["nav"],
        label=str(code)
    )

plt.title(
    "Top 5 Funds Benchmark Comparison"
)

plt.legend()

plt.savefig(
    "charts/benchmark_comparison.png",
    bbox_inches="tight"
)

plt.show()

print("Benchmark chart generated")