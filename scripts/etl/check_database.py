"""
Verify SQLite Database
"""

import sqlite3

from scripts.utils.config import DATABASE
from scripts.utils.helpers import print_header


def main():

    print_header("DATABASE VERIFICATION")

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("""
        SELECT name
        FROM sqlite_master
        WHERE type='table'
    """)

    tables = cursor.fetchall()

    print("\nTables Found:\n")

    for table in tables:

        table_name = table[0]

        cursor.execute(
            f"SELECT COUNT(*) FROM {table_name}"
        )

        rows = cursor.fetchone()[0]

        print(f"{table_name:<30} {rows} rows")

    conn.close()


if __name__ == "__main__":
    main()