import pandas as pd

df = pd.read_csv(
    "data/raw/07_scheme_performance.csv"
)

print("Before Cleaning:", df.shape)

# Convert returns to numeric

return_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

for col in return_cols:

    df[col] = pd.to_numeric(
        df[col],
        errors="coerce"
    )

# Find rows where returns are invalid

anomalies = df[
    df[return_cols].isnull().any(axis=1)
]

print("\nInvalid Return Records:")
print(anomalies.shape)

# Expense ratio validation

expense_anomalies = df[
    (df["expense_ratio_pct"] < 0.1)
    |
    (df["expense_ratio_pct"] > 2.5)
]

print("\nExpense Ratio Anomalies:")
print(expense_anomalies.shape)

# Remove duplicates

df = df.drop_duplicates()

print("\nAfter Cleaning:", df.shape)

df.to_csv(
    "data/processed/07_scheme_performance_clean.csv",
    index=False
)

print("\nFile Saved Successfully")