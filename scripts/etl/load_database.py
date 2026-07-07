from sqlalchemy import create_engine
import pandas as pd

from scripts.utils.config import RAW_DATA, DATABASE
from scripts.utils.helpers import print_header

print_header("LOAD STAR SCHEMA")

engine = create_engine(f"sqlite:///{DATABASE}")

# -----------------------------
# Load CSV files
# -----------------------------

fund = pd.read_csv(RAW_DATA / "01_fund_master.csv")

nav = pd.read_csv(RAW_DATA / "02_nav_history.csv")

transactions = pd.read_csv(
    RAW_DATA / "08_investor_transactions.csv"
)

performance = pd.read_csv(
    RAW_DATA / "07_scheme_performance.csv"
)

# -----------------------------
# Dimension : Fund
# -----------------------------

dim_fund = fund[
    [
        "amfi_code",
        "scheme_name",
        "fund_house",
        "category",
        "sub_category",
        "plan",
        "risk_grade",
        "benchmark",
        "sebi_category_code",
    ]
]

dim_fund.to_sql(
    "dim_fund",
    engine,
    if_exists="append",
    index=False,
)

print(f"dim_fund : {len(dim_fund)} rows")