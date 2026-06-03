import pandas as pd

df = pd.read_csv(
    "data/raw/09_portfolio_holdings.csv"
)

df = df.drop_duplicates()

df = df.dropna(how="all")

df.to_csv(
    "data/processed/09_portfolio_holdings_clean.csv",
    index=False
)