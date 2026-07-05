"""
Project Configuration
"""

from pathlib import Path

# Project Root
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# ------------------------
# Data Directories
# ------------------------

DATA = PROJECT_ROOT / "data"

RAW_DATA = DATA / "raw"
PROCESSED_DATA = DATA / "processed"
DATABASE_DIR = DATA / "db"

DATABASE = DATABASE_DIR / "bluestock_mf.db"

# ------------------------
# Other Directories
# ------------------------

SQL_DIR = PROJECT_ROOT / "sql"
REPORTS_DIR = PROJECT_ROOT / "reports"
DASHBOARD_DIR = PROJECT_ROOT / "dashboard"