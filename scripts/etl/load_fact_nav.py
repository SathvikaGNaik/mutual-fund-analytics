"""
Load fact_nav table
"""

import pandas as pd
from sqlalchemy import create_engine

from scripts.utils.config import RAW_DATA, DATABASE
from scripts.utils.helpers import print_header


def main():

    print_header("LOAD FACT_NAV")

    engine = create_engine(f"sqlite:///{DATABASE}")

    # Load NAV data
    nav = pd.read_csv(RAW_DATA / "02_nav_history.csv")

    nav["date"] = pd.to_datetime(nav["date"])

    # Load date dimension
    dim_date = pd.read_sql(
        "SELECT date_id, full_date FROM dim_date",
        engine
    )

    dim_date["full_date"] = pd.to_datetime(dim_date["full_date"])

    # Map dates to date_id
    nav = nav.merge(
        dim_date,
        left_on="date",
        right_on="full_date",
        how="left"
    )

    fact_nav = nav[
        [
            "amfi_code",
            "date_id",
            "nav"
        ]
    ]

    fact_nav.to_sql(
        "fact_nav",
        engine,
        if_exists="append",
        index=False
    )

    print(f"Inserted {len(fact_nav)} rows into fact_nav.")


if __name__ == "__main__":
    main()