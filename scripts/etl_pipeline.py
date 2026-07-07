"""
BlueStock Mutual Fund Analytics
Complete ETL Pipeline

Run:
python scripts/etl_pipeline.py
"""

import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

steps = [
    ("Reset Database", "scripts.etl.reset_database"),
    ("Create Database", "scripts.etl.create_database"),
    ("Load Fund Dimension", "scripts.etl.load_dim_fund"),
    ("Build Date Dimension", "scripts.etl.build_dim_date"),
    ("Load NAV Fact", "scripts.etl.load_fact_nav"),
    ("Load Transactions Fact", "scripts.etl.load_fact_transactions"),
    ("Load Performance Fact", "scripts.etl.load_fact_performance"),
    ("Load AUM Fact", "scripts.etl.load_fact_aum"),
    ("Verify Database", "scripts.etl.check_database"),
]


def run_step(title, module):
    print("\n" + "=" * 70)
    print(title.upper())
    print("=" * 70)

    result = subprocess.run(
        [sys.executable, "-m", module],
        cwd=PROJECT_ROOT,
    )

    if result.returncode != 0:
        raise RuntimeError(f"Pipeline failed at: {title}")


def main():

    print("\n")
    print("=" * 70)
    print("BLUESTOCK MUTUAL FUND ANALYTICS ETL PIPELINE")
    print("=" * 70)

    for title, module in steps:
        run_step(title, module)

    print("\n")
    print("=" * 70)
    print("ETL PIPELINE COMPLETED SUCCESSFULLY")
    print("=" * 70)


if __name__ == "__main__":
    main()