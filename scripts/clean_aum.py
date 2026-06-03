import pandas as pd

df = pd.read_csv(
    "data/raw/03_aum_by_fund_house.csv"
)

print(df.shape)

df = df.drop_duplicates()

df = df.dropna(how="all")

df.to_csv(
    "data/processed/03_aum_by_fund_house_clean.csv",
    index=False
)