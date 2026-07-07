import sqlite3

conn = sqlite3.connect("data/db/bluestock_mf.db")
cursor = conn.cursor()

cursor.execute("PRAGMA table_info(dim_fund)")

for row in cursor.fetchall():
    print(row)

conn.close()