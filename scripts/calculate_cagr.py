import pandas as pd

nav = pd.read_csv(
    "data/processed/nav_daily_returns.csv"
)

nav["date"] = pd.to_datetime(
    nav["date"]
)

results = []

for code in nav["amfi_code"].unique():

    temp = nav[
        nav["amfi_code"] == code
    ]

    start_nav = temp.iloc[0]["nav"]
    end_nav = temp.iloc[-1]["nav"]

    years = (
        temp["date"].max()
        -
        temp["date"].min()
    ).days / 365

    cagr = (
        (end_nav / start_nav)
        ** (1 / years)
    ) - 1

    results.append(
        [code, cagr]
    )

cagr_df = pd.DataFrame(
    results,
    columns=[
        "amfi_code",
        "cagr"
    ]
)

cagr_df.to_csv(
    "data/processed/cagr.csv",
    index=False
)

print("CAGR calculation completed")