from pathlib import Path

import pandas as pd
from sqlalchemy import create_engine

from scripts.utils.config import RAW_DATA, DATABASE
from scripts.utils.helpers import print_header


def main():
    print_header("BUILD DIM_DATE")

    nav = pd.read_csv(RAW_DATA / "02_nav_history.csv")
    txn = pd.read_csv(RAW_DATA / "08_investor_transactions.csv")

    nav["date"] = pd.to_datetime(nav["date"])
    txn["transaction_date"] = pd.to_datetime(txn["transaction_date"])

    dates = pd.concat(
        [
            nav["date"],
            txn["transaction_date"]
        ]
    ).drop_duplicates().sort_values()

    dim_date = pd.DataFrame({
        "full_date": dates
    })

    dim_date["day"] = dim_date["full_date"].dt.day
    dim_date["month"] = dim_date["full_date"].dt.month
    dim_date["month_name"] = dim_date["full_date"].dt.month_name()
    dim_date["quarter"] = dim_date["full_date"].dt.quarter
    dim_date["year"] = dim_date["full_date"].dt.year

    engine = create_engine(f"sqlite:///{DATABASE}")

    dim_date.to_sql(
        "dim_date",
        engine,
        if_exists="append",
        index=False
    )

    print(f"Inserted {len(dim_date)} rows into dim_date.")


if __name__ == "__main__":
    main()