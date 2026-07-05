"""
Load Cleaned CSVs into SQLite
"""

import sqlite3

from scripts.utils.config import (
    DATABASE,
    PROCESSED_DATA,
    RAW_DATA,
)

from scripts.utils.helpers import (
    load_csv,
    print_header,
)


TABLES = {
    "fund_master": RAW_DATA / "01_fund_master.csv",
    "nav_history": PROCESSED_DATA / "clean_nav_history.csv",
    "investor_transactions": PROCESSED_DATA / "clean_investor_transactions.csv",
    "scheme_performance": PROCESSED_DATA / "clean_scheme_performance.csv",
}


def main():

    print_header("LOAD DATABASE")

    conn = sqlite3.connect(DATABASE)

    for table_name, file_path in TABLES.items():

        print(f"\nLoading {table_name}...")

        df = load_csv(file_path)

        df.to_sql(
            table_name,
            conn,
            if_exists="replace",
            index=False,
        )

        print(f"✓ {len(df)} rows inserted.")

    conn.close()

    print_header("DATABASE LOADING COMPLETED")


if __name__ == "__main__":
    main()