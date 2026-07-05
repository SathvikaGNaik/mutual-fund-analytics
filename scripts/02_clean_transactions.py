from pathlib import Path
import pandas as pd

# ==========================================================
# DAY 2 - TASK 2
# Clean Investor Transactions Dataset
# ==========================================================

print("=" * 60)
print("DAY 2 - CLEAN INVESTOR TRANSACTIONS")
print("=" * 60)

# ----------------------------------------------------------
# Step 1: Load Dataset
# ----------------------------------------------------------

input_file = Path("data/raw/08_investor_transactions.csv")

df = pd.read_csv(input_file)

print("\n✅ Dataset Loaded Successfully")

# ----------------------------------------------------------
# Step 2: Dataset Overview
# ----------------------------------------------------------

print("\n" + "=" * 60)
print("DATASET OVERVIEW")
print("=" * 60)

print(f"Rows    : {df.shape[0]}")
print(f"Columns : {df.shape[1]}")

print("\nColumn Names")
print(df.columns.tolist())

print("\nData Types")
print(df.dtypes)

print("\nFirst 5 Rows")
print(df.head())

# ----------------------------------------------------------
# Step 3: Missing Values
# ----------------------------------------------------------

print("\n" + "=" * 60)
print("MISSING VALUES")
print("=" * 60)

print(df.isnull().sum())

# ----------------------------------------------------------
# Step 4: Unique Transaction Types
# ----------------------------------------------------------

print("\n" + "=" * 60)
print("TRANSACTION TYPES")
print("=" * 60)

print(df["transaction_type"].value_counts())

# Standardize values

df["transaction_type"] = (
    df["transaction_type"]
    .str.strip()
    .str.upper()
)

mapping = {
    "SIP": "SIP",
    "LUMPSUM": "LUMPSUM",
    "REDEMPTION": "REDEMPTION"
}

df["transaction_type"] = (
    df["transaction_type"]
    .replace(mapping)
)

print("\nStandardized Transaction Types")
print(df["transaction_type"].value_counts())

# ----------------------------------------------------------
# Step 5: Date Conversion
# ----------------------------------------------------------

print("\nConverting transaction_date to datetime...")

df["transaction_date"] = pd.to_datetime(df["transaction_date"])

print("✅ Date conversion completed.")

# ----------------------------------------------------------
# Step 6: Amount Validation
# ----------------------------------------------------------

print("\n" + "=" * 60)
print("AMOUNT VALIDATION")
print("=" * 60)

invalid_amount = (df["amount_inr"] <= 0).sum()

print(f"Transactions with amount_inr <= 0 : {invalid_amount}")

# ----------------------------------------------------------
# Step 7: KYC Validation
# ----------------------------------------------------------

print("\n" + "=" * 60)
print("KYC STATUS")
print("=" * 60)

print(df["kyc_status"].value_counts())

allowed_status = {
    "Verified",
    "Pending",
    "Rejected"
}

invalid_kyc = (
    ~df["kyc_status"].isin(allowed_status)
).sum()

print(f"\nInvalid KYC Values : {invalid_kyc}")

# ----------------------------------------------------------
# Step 8: Duplicate Check
# ----------------------------------------------------------

duplicates = df.duplicated().sum()

print("\n" + "=" * 60)
print("DUPLICATE CHECK")
print("=" * 60)

print(f"Duplicate Rows : {duplicates}")

if duplicates > 0:
    df = df.drop_duplicates()

# ----------------------------------------------------------
# Step 9: Save Cleaned Dataset
# ----------------------------------------------------------

output_folder = Path("data/processed")
output_folder.mkdir(exist_ok=True)

output_file = output_folder / "clean_investor_transactions.csv"

df.to_csv(output_file, index=False)

# ----------------------------------------------------------
# Final Summary
# ----------------------------------------------------------

print("\n" + "=" * 60)
print("CLEANING SUMMARY")
print("=" * 60)

print(f"Rows After Cleaning : {len(df)}")
print(f"Missing Values      : {df.isnull().sum().sum()}")
print(f"Duplicate Rows      : {duplicates}")
print(f"Invalid Amounts     : {invalid_amount}")
print(f"Invalid KYC Status  : {invalid_kyc}")

print("\n✅ Cleaned dataset saved successfully.")
print(f"Location : {output_file}")

print("\n" + "=" * 60)
print("DAY 2 - TASK 2 COMPLETED")
print("=" * 60)