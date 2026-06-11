import os

os.system("python scripts/data_ingestion.py")
os.system("python scripts/clean_transactions.py")
os.system("python scripts/load_sqlite.py")
os.system("python scripts/calculate_cagr.py")
os.system("python scripts/calculate_alpha_beta.py")
os.system("python scripts/calculate_sharpe_sortino.py")

print("Pipeline Completed")