import pandas as pd

df = pd.read_csv(
    "data/raw/05_category_inflows.csv"
)

df = df.drop_duplicates()

df = df.dropna(how="all")

df.to_csv(
    "data/processed/05_category_inflows_clean.csv",
    index=False
)