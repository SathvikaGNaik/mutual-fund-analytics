from pathlib import Path
import pandas as pd

# Path to the raw data folder
data_folder = Path("data/raw")

# Get all CSV files
csv_files = sorted(data_folder.glob("*.csv"))

print(f"Found {len(csv_files)} CSV files.\n")

for file in csv_files:
    print("=" * 60)
    print(f"File: {file.name}")

    df = pd.read_csv(file)

    print("\nShape:")
    print(df.shape)

    print("\nColumns & Data Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\n")