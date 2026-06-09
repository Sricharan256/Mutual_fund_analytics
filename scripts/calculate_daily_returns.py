import pandas as pd

nav = pd.read_csv("data/processed/02_nav_history_clean.csv")

nav["date"] = pd.to_datetime(nav["date"])

nav = nav.sort_values(
    ["amfi_code", "date"]
)

nav["daily_return"] = (
    nav.groupby("amfi_code")["nav"]
    .pct_change()
)

nav.to_csv(
    "data/processed/nav_daily_returns.csv",
    index=False
)

print("Daily returns calculated successfully")