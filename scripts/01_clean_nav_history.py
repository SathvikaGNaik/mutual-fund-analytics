from pathlib import Path
import pandas as pd

# ==========================================================
# DAY 2 - TASK 1
# Clean NAV History Dataset
# ==========================================================

print("=" * 60)
print("DAY 2 - CLEAN NAV HISTORY DATASET")
print("=" * 60)

# ----------------------------------------------------------
# Step 1: Load Dataset
# ----------------------------------------------------------

input_file = Path("data/raw/02_nav_history.csv")

nav_df = pd.read_csv(input_file)

print("\n✅ Dataset Loaded Successfully")

# ----------------------------------------------------------
# Step 2: Basic Information
# ----------------------------------------------------------

print("\n" + "=" * 60)
print("DATASET OVERVIEW")
print("=" * 60)

print(f"\nRows    : {nav_df.shape[0]}")
print(f"Columns : {nav_df.shape[1]}")

print("\nColumn Names:")
print(nav_df.columns.tolist())

print("\nData Types (Before Cleaning):")
print(nav_df.dtypes)

print("\nFirst 5 Rows:")
print(nav_df.head())

# ----------------------------------------------------------
# Step 3: Missing Values
# ----------------------------------------------------------

print("\n" + "=" * 60)
print("MISSING VALUE CHECK")
print("=" * 60)

print(nav_df.isnull().sum())

# ----------------------------------------------------------
# Step 4: Convert Date Column
# ----------------------------------------------------------

print("\nConverting 'date' column to datetime...")

nav_df["date"] = pd.to_datetime(nav_df["date"])

print("✅ Date conversion completed.")

# ----------------------------------------------------------
# Step 5: Sort Data
# ----------------------------------------------------------

print("\nSorting by AMFI Code and Date...")

nav_df = nav_df.sort_values(
    by=["amfi_code", "date"]
).reset_index(drop=True)

print("✅ Sorting completed.")

# ----------------------------------------------------------
# Step 6: Duplicate Check
# ----------------------------------------------------------

duplicates = nav_df.duplicated().sum()

print("\n" + "=" * 60)
print("DUPLICATE CHECK")
print("=" * 60)

print(f"Duplicate Rows Found : {duplicates}")

if duplicates > 0:
    nav_df = nav_df.drop_duplicates()
    print("Duplicates removed.")
else:
    print("No duplicate rows found.")

# ----------------------------------------------------------
# Step 7: Validate NAV Values
# ----------------------------------------------------------

print("\n" + "=" * 60)
print("NAV VALIDATION")
print("=" * 60)

invalid_nav = (nav_df["nav"] <= 0).sum()

print(f"Invalid NAV Values (<=0): {invalid_nav}")

if invalid_nav == 0:
    print("✅ All NAV values are valid.")
else:
    print("⚠ Invalid NAV values detected.")

# ----------------------------------------------------------
# Step 8: Check Date Range
# ----------------------------------------------------------

print("\n" + "=" * 60)
print("DATE RANGE")
print("=" * 60)

print(f"Earliest Date : {nav_df['date'].min().date()}")
print(f"Latest Date   : {nav_df['date'].max().date()}")

# ----------------------------------------------------------
# Step 9: Dataset Statistics
# ----------------------------------------------------------

print("\n" + "=" * 60)
print("NAV STATISTICS")
print("=" * 60)

print(nav_df["nav"].describe())

# ----------------------------------------------------------
# Step 10: Forward Fill
# ----------------------------------------------------------
# Bluestock PDF asks for forward filling.
# Since there are NO missing NAV values in this dataset,
# ffill() will not change anything.
# We still include it to satisfy the project requirement.

nav_df["nav"] = nav_df["nav"].ffill()

print("\nForward fill applied (no changes because no missing NAV values).")

# ----------------------------------------------------------
# Step 11: Save Cleaned Dataset
# ----------------------------------------------------------

output_folder = Path("data/processed")
output_folder.mkdir(parents=True, exist_ok=True)

output_file = output_folder / "clean_nav_history.csv"

nav_df.to_csv(output_file, index=False)

print("\n" + "=" * 60)
print("CLEANING SUMMARY")
print("=" * 60)

print(f"Original Rows : 46000")
print(f"Final Rows    : {len(nav_df)}")
print(f"Duplicates Removed : {duplicates}")
print(f"Missing Values : {nav_df.isnull().sum().sum()}")
print(f"Invalid NAV    : {invalid_nav}")

print("\n✅ Cleaned dataset saved successfully.")
print(f"Location : {output_file}")

print("\n" + "=" * 60)
print("DAY 2 - TASK 1 COMPLETED")
print("=" * 60)