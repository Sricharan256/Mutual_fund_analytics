import pandas as pd

df = pd.read_csv(
    "data/raw/10_benchmark_indices.csv"
)

df = df.drop_duplicates()

df = df.dropna(how="all")

df.to_csv(
    "data/processed/10_benchmark_indices_clean.csv",
    index=False
)