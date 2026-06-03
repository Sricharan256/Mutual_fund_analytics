import pandas as pd

df = pd.read_csv(
    "data/raw/06_industry_folio_count.csv"
)

df = df.drop_duplicates()

df = df.dropna(how="all")

df.to_csv(
    "data/processed/06_industry_folio_count_clean.csv",
    index=False
)