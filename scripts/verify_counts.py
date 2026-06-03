from sqlalchemy import create_engine
import pandas as pd

engine = create_engine(
    "sqlite:///bluestock_mf.db"
)

query = """
SELECT COUNT(*)
FROM nav_history
"""

print(
    pd.read_sql(query, engine)
)