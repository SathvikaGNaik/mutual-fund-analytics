"""
Day 2 - Task 3
Validate Scheme Performance Dataset
"""

from scripts.utils.config import RAW_DATA, PROCESSED_DATA
from scripts.utils.helpers import (
    load_csv,
    save_csv,
    print_header,
    dataset_overview,
    missing_values,
    validation_summary,
)
from scripts.utils.validator import (
    validate_duplicates,
    validate_positive,
    validate_range,
)


def main():

    print_header("DAY 2 - SCHEME PERFORMANCE")

    # --------------------------------------------------
    # Load Dataset
    # --------------------------------------------------

    df = load_csv(
        RAW_DATA / "07_scheme_performance.csv"
    )

    dataset_overview(df)

    # --------------------------------------------------
    # Missing Values
    # --------------------------------------------------

    print_header("Missing Values")

    missing_values(df)

    # --------------------------------------------------
    # Validations
    # --------------------------------------------------

    duplicates = validate_duplicates(df)

    invalid_expense = validate_positive(
        df["expense_ratio_pct"]
    )

    invalid_beta = validate_positive(
        df["beta"]
    )

    invalid_aum = validate_positive(
        df["aum_crore"]
    )

    invalid_rating = validate_range(
        df["morningstar_rating"],
        1,
        5,
    )

    # --------------------------------------------------
    # Save
    # --------------------------------------------------

    save_csv(
        df,
        PROCESSED_DATA /
        "clean_scheme_performance.csv"
    )

    # --------------------------------------------------
    # Summary
    # --------------------------------------------------

    validation_summary(
        Duplicates=duplicates,
        Invalid_Expense_Ratio=invalid_expense,
        Invalid_Beta=invalid_beta,
        Invalid_AUM=invalid_aum,
        Invalid_Ratings=invalid_rating,
    )

    print("\n✅ Dataset validated successfully.")
    print("Saved to processed folder.")


if __name__ == "__main__":
    main()