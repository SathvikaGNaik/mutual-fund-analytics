"""
Day 2 - Task 1
Clean NAV History Dataset
"""

import pandas as pd

from scripts.utils.config import RAW_DATA, PROCESSED_DATA
from scripts.utils.helpers import (
    load_csv,
    save_csv,
    print_header,
    missing_values,
)
from scripts.utils.validator import (
    validate_duplicates,
    validate_positive,
)


def main():

    print_header("DAY 2 - CLEAN NAV HISTORY")

    # --------------------------------------------------
    # Load Dataset
    # --------------------------------------------------

    df = load_csv(RAW_DATA / "02_nav_history.csv")

    print(f"\nRows    : {df.shape[0]}")
    print(f"Columns : {df.shape[1]}")

    print("\nColumn Names")
    print(df.columns.tolist())

    print("\nData Types")
    print(df.dtypes)

    # --------------------------------------------------
    # Missing Values
    # --------------------------------------------------

    print_header("Missing Values")

    missing_values(df)

    # --------------------------------------------------
    # Convert Date
    # --------------------------------------------------

    df["date"] = pd.to_datetime(df["date"])

    # --------------------------------------------------
    # Sort
    # --------------------------------------------------

    df = (
        df
        .sort_values(["amfi_code", "date"])
        .reset_index(drop=True)
    )

    # --------------------------------------------------
    # Validation
    # --------------------------------------------------

    print_header("Validation")

    duplicates = validate_duplicates(df)
    invalid_nav = validate_positive(df["nav"])

    print(f"Duplicate Rows : {duplicates}")
    print(f"Invalid NAV    : {invalid_nav}")

    # --------------------------------------------------
    # Remove duplicates
    # --------------------------------------------------

    if duplicates:
        df = df.drop_duplicates()

    # --------------------------------------------------
    # Forward Fill
    # --------------------------------------------------

    df["nav"] = df["nav"].ffill()

    # --------------------------------------------------
    # Save
    # --------------------------------------------------

    save_csv(
        df,
        PROCESSED_DATA / "clean_nav_history.csv"
    )

    print_header("Completed")

    print("Clean NAV History saved successfully.")


if __name__ == "__main__":
    main()