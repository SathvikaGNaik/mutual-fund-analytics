"""
Day 2 - Task 2
Clean Investor Transactions Dataset
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

    print_header("DAY 2 - CLEAN INVESTOR TRANSACTIONS")

    # --------------------------------------------------
    # Load Dataset
    # --------------------------------------------------

    df = load_csv(RAW_DATA / "08_investor_transactions.csv")

    print(f"\nRows    : {df.shape[0]}")
    print(f"Columns : {df.shape[1]}")

    print("\nColumn Names")
    print(df.columns.tolist())

    print("\nData Types")
    print(df.dtypes)

    print("\nFirst 5 Rows")
    print(df.head())

    # --------------------------------------------------
    # Missing Values
    # --------------------------------------------------

    print_header("Missing Values")

    missing_values(df)

    # --------------------------------------------------
    # Convert Date
    # --------------------------------------------------

    print_header("Convert Date")

    df["transaction_date"] = pd.to_datetime(
        df["transaction_date"]
    )

    print("✅ transaction_date converted to datetime")

    # --------------------------------------------------
    # Standardize Transaction Types
    # --------------------------------------------------

    print_header("Standardize Transaction Types")

    print("Before Standardization")

    print(df["transaction_type"].value_counts())

    df["transaction_type"] = (
        df["transaction_type"]
        .str.strip()
        .str.upper()
    )

    print("\nAfter Standardization")

    print(df["transaction_type"].value_counts())

    # --------------------------------------------------
    # Validate Amount
    # --------------------------------------------------

    print_header("Amount Validation")

    invalid_amount = validate_positive(
        df["amount_inr"]
    )

    print(f"Invalid Amounts (<=0) : {invalid_amount}")

    # --------------------------------------------------
    # Validate KYC
    # --------------------------------------------------

    print_header("KYC Validation")

    print(df["kyc_status"].value_counts())

    allowed_status = {
        "Verified",
        "Pending",
        "Rejected"
    }

    invalid_kyc = (
        ~df["kyc_status"].isin(
            allowed_status
        )
    ).sum()

    print(f"\nInvalid KYC Values : {invalid_kyc}")

    # --------------------------------------------------
    # Duplicate Check
    # --------------------------------------------------

    print_header("Duplicate Check")

    duplicates = validate_duplicates(df)

    print(f"Duplicate Rows : {duplicates}")

    if duplicates:
        df = df.drop_duplicates()

    # --------------------------------------------------
    # Save Clean Dataset
    # --------------------------------------------------

    save_csv(
        df,
        PROCESSED_DATA / "clean_investor_transactions.csv"
    )

    # --------------------------------------------------
    # Final Summary
    # --------------------------------------------------

    print_header("Cleaning Summary")

    print(f"Rows After Cleaning : {len(df)}")
    print(f"Missing Values      : {df.isnull().sum().sum()}")
    print(f"Duplicate Rows      : {duplicates}")
    print(f"Invalid Amounts     : {invalid_amount}")
    print(f"Invalid KYC Status  : {invalid_kyc}")

    print("\n✅ Cleaned dataset saved successfully.")
    print(
        f"Location : {PROCESSED_DATA / 'clean_investor_transactions.csv'}"
    )

    print_header("TASK COMPLETED")


if __name__ == "__main__":
    main()