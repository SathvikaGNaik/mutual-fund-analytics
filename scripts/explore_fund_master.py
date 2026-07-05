import pandas as pd

# Read the dataset
funds = pd.read_csv("data/raw/01_fund_master.csv")

print("="*60)
print("FUND MASTER INFORMATION")
print("="*60)

print("\nTotal Funds:")
print(len(funds))

print("\nUnique Fund Houses:")
print(funds["fund_house"].unique())

print("\nNumber of Fund Houses:")
print(funds["fund_house"].nunique())

print("\nUnique Categories:")
print(funds["category"].unique())

print("\nUnique Sub Categories:")
print(funds["sub_category"].unique())

print("\nRisk Categories:")
print(funds["risk_category"].unique())

print("\nSample AMFI Codes:")
print(funds["amfi_code"].head(10))