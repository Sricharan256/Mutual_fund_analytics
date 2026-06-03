import pandas as pd

df = pd.read_csv(
    "data/raw/01_fund_master.csv"
)

print("Before:", df.shape)

df = df.drop_duplicates()

df = df.dropna(how="all")

print("After:", df.shape)

df.to_csv(
    "data/processed/01_fund_master_clean.csv",
    index=False
)

print("Saved")