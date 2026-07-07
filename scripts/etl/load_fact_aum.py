"""
Load fact_aum table
"""

import pandas as pd
from sqlalchemy import create_engine

from scripts.utils.config import RAW_DATA, DATABASE
from scripts.utils.helpers import print_header


def main():

    print_header("LOAD FACT_AUM")

    engine = create_engine(f"sqlite:///{DATABASE}")

    performance = pd.read_csv(
        RAW_DATA / "07_scheme_performance.csv"
    )

    fact_aum = performance[
        [
            "amfi_code",
            "aum_crore"
        ]
    ]

    fact_aum.to_sql(
        "fact_aum",
        engine,
        if_exists="append",
        index=False
    )

    print(f"Inserted {len(fact_aum)} rows into fact_aum.")


if __name__ == "__main__":
    main()