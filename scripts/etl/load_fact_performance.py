"""
Load fact_performance table
"""

import pandas as pd
from sqlalchemy import create_engine

from scripts.utils.config import RAW_DATA, DATABASE
from scripts.utils.helpers import print_header


def main():

    print_header("LOAD FACT_PERFORMANCE")

    engine = create_engine(f"sqlite:///{DATABASE}")

    performance = pd.read_csv(
        RAW_DATA / "07_scheme_performance.csv"
    )

    fact_performance = performance[
        [
            "amfi_code",
            "return_1yr_pct",
            "return_3yr_pct",
            "return_5yr_pct",
            "benchmark_3yr_pct",
            "alpha",
            "beta",
            "sharpe_ratio",
            "sortino_ratio",
            "std_dev_ann_pct",
            "max_drawdown_pct",
            "expense_ratio_pct",
            "morningstar_rating",
        ]
    ]

    fact_performance.to_sql(
        "fact_performance",
        engine,
        if_exists="append",
        index=False
    )

    print(f"Inserted {len(fact_performance)} rows into fact_performance.")


if __name__ == "__main__":
    main()