import pandas as pd

df = pd.read_csv("data/raw/01_fund_master.csv")

print("Shape:")
print(df.shape)

print("\nFund Houses:")
print(df["fund_house"].unique())

print("\nCategories:")
print(df["category"].unique())

print("\nSub Categories:")
print(df["sub_category"].unique())

print("\nRisk Categories:")
print(df["risk_category"].unique())

print("\nFunds per Category:")
print(df["category"].value_counts())

print("\nFunds per Risk Category:")
print(df["risk_category"].value_counts())

print("\nAMFI Codes:")
print(df[["amfi_code", "scheme_name"]].head(10))        
print(df.columns.tolist())