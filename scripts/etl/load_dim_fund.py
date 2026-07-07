"""
Load dim_fund table
"""

import pandas as pd
from sqlalchemy import create_engine

from scripts.utils.config import RAW_DATA, DATABASE
from scripts.utils.helpers import print_header


def main():

    print_header("LOAD DIM_FUND")

    engine = create_engine(f"sqlite:///{DATABASE}")

    fund = pd.read_csv(RAW_DATA / "01_fund_master.csv")

    fund["launch_date"] = pd.to_datetime(fund["launch_date"])

    fund.to_sql(
        "dim_fund",
        engine,
        if_exists="append",
        index=False,
    )

    print(f"Inserted {len(fund)} rows into dim_fund.")


if __name__ == "__main__":
    main()