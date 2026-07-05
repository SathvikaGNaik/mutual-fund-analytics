"""
Create SQLite Database
"""

import sqlite3

from scripts.utils.config import DATABASE
from scripts.utils.helpers import print_header


def main():

    print_header("CREATE DATABASE")

    DATABASE.parent.mkdir(parents=True, exist_ok=True)

    conn = sqlite3.connect(DATABASE)

    print("Database created successfully.")

    print(f"\nLocation:\n{DATABASE}")

    conn.close()

    print("\nConnection closed.")


if __name__ == "__main__":
    main()