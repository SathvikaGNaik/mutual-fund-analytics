"""
Common helper functions
"""

import pandas as pd


def print_header(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


def load_csv(file_path):
    """Load CSV file"""
    return pd.read_csv(file_path)


def save_csv(df, output_path):
    """Save DataFrame"""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)


def dataset_overview(df):
    """Print basic dataset information"""

    print(f"\nRows    : {df.shape[0]}")
    print(f"Columns : {df.shape[1]}")

    print("\nColumn Names")
    print(df.columns.tolist())

    print("\nData Types")
    print(df.dtypes)

    print("\nFirst 5 Rows")
    print(df.head())


def missing_values(df):
    """Display missing values"""

    print(df.isnull().sum())


def validation_summary(**kwargs):
    """Print validation summary"""

    print_header("Validation Summary")

    for key, value in kwargs.items():
        print(f"{key:<25}: {value}")