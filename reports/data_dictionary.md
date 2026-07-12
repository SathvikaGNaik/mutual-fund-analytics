# BlueStock Mutual Fund Analytics
# Data Dictionary

---

## Database Overview

The project follows a Star Schema consisting of two dimension tables and four fact tables.

---

# Dimension Table: dim_fund

| Column | Data Type | Description | Source |
|---------|-----------|-------------|--------|
| amfi_code | INTEGER | Unique AMFI Scheme Code | fund_master.csv |
| fund_house | TEXT | Asset Management Company | fund_master.csv |
| scheme_name | TEXT | Mutual Fund Scheme Name | fund_master.csv |
| category | TEXT | Fund Category | fund_master.csv |
| sub_category | TEXT | Fund Sub-category | fund_master.csv |
| plan | TEXT | Direct/Regular Plan | fund_master.csv |
| launch_date | DATE | Scheme Launch Date | fund_master.csv |
| benchmark | TEXT | Benchmark Index | fund_master.csv |
| expense_ratio_pct | REAL | Expense Ratio (%) | fund_master.csv |
| exit_load_pct | REAL | Exit Load (%) | fund_master.csv |
| min_sip_amount | REAL | Minimum SIP Amount | fund_master.csv |
| min_lumpsum_amount | REAL | Minimum Lump Sum Amount | fund_master.csv |
| fund_manager | TEXT | Fund Manager Name | fund_master.csv |
| risk_category | TEXT | Risk Category | fund_master.csv |
| sebi_category_code | TEXT | SEBI Category Code | fund_master.csv |

---

# Dimension Table: dim_date

| Column | Data Type | Description |
|---------|-----------|-------------|
| date_id | INTEGER | Primary Key |
| full_date | DATE | Calendar Date |
| day | INTEGER | Day of Month |
| month | INTEGER | Month Number |
| month_name | TEXT | Month Name |
| quarter | INTEGER | Quarter |
| year | INTEGER | Calendar Year |

---

# Fact Table: fact_nav

| Column | Data Type | Description |
|---------|-----------|-------------|
| nav_id | INTEGER | Primary Key |
| amfi_code | INTEGER | Fund Reference |
| date_id | INTEGER | Date Reference |
| nav | REAL | Net Asset Value |

---

# Fact Table: fact_transactions

| Column | Data Type | Description |
|---------|-----------|-------------|
| transaction_id | INTEGER | Primary Key |
| investor_id | TEXT | Investor ID |
| amfi_code | INTEGER | Fund Reference |
| date_id | INTEGER | Date Reference |
| transaction_type | TEXT | SIP / Lumpsum / Redemption |
| amount_inr | REAL | Transaction Amount |
| state | TEXT | Investor State |
| city | TEXT | Investor City |
| city_tier | TEXT | T30 / B30 |
| age_group | TEXT | Investor Age Group |
| gender | TEXT | Investor Gender |
| annual_income_lakh | REAL | Annual Income (Lakh INR) |
| payment_mode | TEXT | Payment Method |
| kyc_status | TEXT | KYC Verification Status |

---

# Fact Table: fact_performance

| Column | Data Type | Description |
|---------|-----------|-------------|
| performance_id | INTEGER | Primary Key |
| amfi_code | INTEGER | Fund Reference |
| return_1yr_pct | REAL | 1-Year Return (%) |
| return_3yr_pct | REAL | 3-Year Return (%) |
| return_5yr_pct | REAL | 5-Year Return (%) |
| benchmark_3yr_pct | REAL | Benchmark Return (%) |
| alpha | REAL | Alpha |
| beta | REAL | Beta |
| sharpe_ratio | REAL | Sharpe Ratio |
| sortino_ratio | REAL | Sortino Ratio |
| std_dev_ann_pct | REAL | Annual Standard Deviation |
| max_drawdown_pct | REAL | Maximum Drawdown |
| expense_ratio_pct | REAL | Expense Ratio |
| morningstar_rating | INTEGER | Morningstar Rating |

---

# Fact Table: fact_aum

| Column | Data Type | Description |
|---------|-----------|-------------|
| aum_id | INTEGER | Primary Key |
| amfi_code | INTEGER | Fund Reference |
| aum_crore | REAL | Assets Under Management (Crore INR) |