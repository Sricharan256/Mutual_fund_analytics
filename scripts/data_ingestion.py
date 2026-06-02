import pandas as pd
import os

# Path to raw data folder
data_path = "data/raw"

# Get all CSV files
csv_files = [f for f in os.listdir(data_path) if f.endswith(".csv")]

print(f"Found {len(csv_files)} CSV files\n")

for file in csv_files:
    print("=" * 80)
    print(f"DATASET: {file}")
    print("=" * 80)

    try:
        df = pd.read_csv(os.path.join(data_path, file))

        print("\nSHAPE:")
        print(df.shape)

        print("\nDATA TYPES:")
        print(df.dtypes)

        print("\nFIRST 5 ROWS:")
        print(df.head())

        print("\n")

    except Exception as e:
        print(f"Error reading {file}: {e}")