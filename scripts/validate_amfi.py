import pandas as pd

# Load datasets
master = pd.read_csv("data/raw/01_fund_master.csv")
nav = pd.read_csv("data/raw/02_nav_history.csv")

# Unique AMFI codes
master_codes = set(master["amfi_code"])
nav_codes = set(nav["amfi_code"])

# Missing codes
missing_codes = master_codes - nav_codes

print("Total AMFI Codes in Fund Master:")
print(len(master_codes))

print("\nTotal AMFI Codes in NAV History:")
print(len(nav_codes))

print("\nMissing Codes:")
print(len(missing_codes))

if len(missing_codes) == 0:
    print("\nSUCCESS: All AMFI codes are present.")
else:
    print("\nMissing AMFI Codes:")
    print(missing_codes)
print(master.columns)
print(nav.columns)