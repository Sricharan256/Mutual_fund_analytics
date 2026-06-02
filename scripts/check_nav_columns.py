import pandas as pd

df = pd.read_csv("data/raw/02_nav_history.csv")

print("Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())