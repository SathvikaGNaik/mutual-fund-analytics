import pandas as pd

# Load datasets
fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

# Get unique AMFI codes
fund_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

# Compare
missing = fund_codes - nav_codes

print("=" * 60)
print("AMFI CODE VALIDATION")
print("=" * 60)

print(f"Fund Master Codes : {len(fund_codes)}")
print(f"NAV History Codes : {len(nav_codes)}")

if len(missing) == 0:
    print("\n✅ All AMFI codes are present in nav_history.")
else:
    print("\n❌ Missing AMFI Codes:")
    print(missing)

print("\nValidation Complete.")