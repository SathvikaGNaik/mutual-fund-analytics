"""
Load fact_transactions table
"""

import pandas as pd
from sqlalchemy import create_engine

from scripts.utils.config import RAW_DATA, DATABASE
from scripts.utils.helpers import print_header


def main():

    print_header("LOAD FACT_TRANSACTIONS")

    engine = create_engine(f"sqlite:///{DATABASE}")

    # Load cleaned transactions
    transactions = pd.read_csv(
        RAW_DATA / "08_investor_transactions.csv"
    )

    transactions["transaction_date"] = pd.to_datetime(
        transactions["transaction_date"]
    )

    # Load date dimension
    dim_date = pd.read_sql(
        "SELECT date_id, full_date FROM dim_date",
        engine
    )

    dim_date["full_date"] = pd.to_datetime(
        dim_date["full_date"]
    )

    # Map transaction date to date_id
    transactions = transactions.merge(
        dim_date,
        left_on="transaction_date",
        right_on="full_date",
        how="left"
    )

    fact_transactions = transactions[
        [
            "investor_id",
            "amfi_code",
            "date_id",
            "transaction_type",
            "amount_inr",
            "state",
            "city",
            "city_tier",
            "age_group",
            "gender",
            "annual_income_lakh",
            "payment_mode",
            "kyc_status",
        ]
    ]

    fact_transactions.to_sql(
        "fact_transactions",
        engine,
        if_exists="append",
        index=False
    )

    print(
        f"Inserted {len(fact_transactions)} rows into fact_transactions."
    )


if __name__ == "__main__":
    main()