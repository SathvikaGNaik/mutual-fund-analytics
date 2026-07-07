"""
Reset SQLite Database
Drops all existing tables so the schema can be recreated.
"""

import sqlite3

from scripts.utils.config import DATABASE
from scripts.utils.helpers import print_header


def main():
    print_header("RESET DATABASE")

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    tables = [
        "fact_nav",
        "fact_transactions",
        "fact_performance",
        "fact_aum",
        "dim_date",
        "dim_fund",

        # Old tables (cleanup)
        "fund_master",
        "nav_history",
        "investor_transactions",
        "scheme_performance"
    ]

    for table in tables:
        cursor.execute(f"DROP TABLE IF EXISTS {table};")

    conn.commit()
    conn.close()

    print("All tables removed successfully.")


if __name__ == "__main__":
    main()