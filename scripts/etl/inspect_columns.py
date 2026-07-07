import pandas as pd

from scripts.utils.config import RAW_DATA

# Load datasets
fund = pd.read_csv(RAW_DATA / "01_fund_master.csv")
performance = pd.read_csv(RAW_DATA / "07_scheme_performance.csv")
transactions = pd.read_csv(RAW_DATA / "08_investor_transactions.csv")
nav = pd.read_csv(RAW_DATA / "02_nav_history.csv")

print("=" * 60)
print("FUND MASTER")
print("=" * 60)
print(fund.columns.tolist())

print("\n" + "=" * 60)
print("SCHEME PERFORMANCE")
print("=" * 60)
print(performance.columns.tolist())

print("\n" + "=" * 60)
print("INVESTOR TRANSACTIONS")
print("=" * 60)
print(transactions.columns.tolist())

print("\n" + "=" * 60)
print("NAV HISTORY")
print("=" * 60)
print(nav.columns.tolist())