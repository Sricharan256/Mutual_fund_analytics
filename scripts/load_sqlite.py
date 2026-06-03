import pandas as pd
from sqlalchemy import create_engine
import os

# Create SQLite database
engine = create_engine(
    "sqlite:///bluestock_mf.db"
)

processed_folder = "data/processed"

# Get all CSV files
files = [
    f for f in os.listdir(processed_folder)
    if f.endswith(".csv")
]

for file in files:

    file_path = os.path.join(
        processed_folder,
        file
    )

    df = pd.read_csv(file_path)

    # Table name from filename
    table_name = file.replace(
        ".csv",
        ""
    )

    df.to_sql(
        table_name,
        engine,
        if_exists="replace",
        index=False
    )

    print(
        f"Loaded {table_name} : {len(df)} rows"
    )

print("\nAll datasets loaded successfully!")