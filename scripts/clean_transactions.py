import pandas as pd

df = pd.read_csv(
    "data/raw/08_investor_transactions.csv"
)

print("Before Cleaning:", df.shape)

# Standardize transaction type
df["transaction_type"] = (
    df["transaction_type"]
    .str.strip()
    .str.lower()
)

mapping = {
    "sip": "SIP",
    "lumpsum": "Lumpsum",
    "redemption": "Redemption"
}

df["transaction_type"] = (
    df["transaction_type"].map(mapping)
)

# Validate amount
df = df[df["amount_inr"] > 0]

# Convert date
df["transaction_date"] = pd.to_datetime(
    df["transaction_date"]
)

# Validate KYC Status
print("\nKYC Values Found:")
print(df["kyc_status"].unique())

valid_kyc = [
    "Verified",
    "Pending",
    "Rejected"
]

df = df[
    df["kyc_status"].isin(valid_kyc)
]

# Remove duplicates
df = df.drop_duplicates()

print("After Cleaning:", df.shape)

df.to_csv(
    "data/processed/08_investor_transactions_clean.csv",
    index=False
)

print("File Saved Successfully")