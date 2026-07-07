"""
Create SQLite Database using schema.sql
"""

import sqlite3

from scripts.utils.config import DATABASE
from scripts.utils.helpers import print_header


def main():

    print_header("CREATE DATABASE")

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    with open("sql/schema.sql", "r", encoding="utf-8") as file:

        schema = file.read()

    cursor.executescript(schema)

    conn.commit()

    conn.close()

    print("Database and tables created successfully.")


if __name__ == "__main__":
    main()