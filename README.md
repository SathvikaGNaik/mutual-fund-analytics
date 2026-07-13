# 📊 Bluestock Mutual Fund Analytics Capstone

An end-to-end Data Analytics Capstone project that analyzes mutual fund performance, investor behaviour, and industry trends using **Python, SQLite, SQL, Jupyter Notebook, and Power BI**.

The project follows a complete analytics pipeline—from data ingestion and cleaning to performance analytics, advanced financial analysis, and interactive dashboards.

---

# Project Objectives

- Build an automated ETL pipeline
- Clean and preprocess mutual fund datasets
- Store processed data in SQLite
- Perform Exploratory Data Analysis (EDA)
- Calculate financial performance metrics
- Develop an interactive Power BI dashboard
- Perform advanced analytics (VaR, Rolling Sharpe Ratio, Cohort Analysis, SIP Continuity, HHI)
- Build a rule-based Mutual Fund Recommendation System

---

# Technology Stack

- Python
- Pandas
- NumPy
- SQLite
- SQL
- Jupyter Notebook
- Matplotlib
- Power BI

---

# Project Structure

```
Mutual_Fund_Analytics/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── db/
│
├── notebooks/
│   ├── 01_data_ingestion.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_eda_analysis.ipynb
│   ├── 04_performance_analytics.ipynb
│   └── 06_advanced_analytics.ipynb
│
├── scripts/
│   ├── data_ingestion.py
│   ├── 01_clean_nav_history.py
│   ├── 02_clean_transactions.py
│   ├── etl_pipeline.py
│   ├── live_nav_fetch.py
│   ├── recommender.py
│   └── ...
│
├── sql/
│   ├── schema.sql
│   └── queries.sql
│
├── dashboard/
│   └── bluestock_mf_dashboard.pbix
│
├── reports/
│   ├── Final_Report.pdf
│   └── Presentation.pptx
│
├── requirements.txt
└── README.md
```

---

# Dataset

The project uses multiple datasets including:

- Fund Master
- NAV History
- Monthly SIP Inflows
- Category Inflows
- Portfolio Holdings
- Investor Transactions
- Benchmark Indices

After preprocessing, cleaned datasets are stored inside:

```
data/processed/
```

---

# ETL Pipeline

The ETL pipeline performs:

- Data ingestion
- Missing value handling
- Duplicate removal
- Data validation
- Category standardization
- Data transformation
- Loading cleaned data into SQLite

Run:

```bash
python scripts/etl_pipeline.py
```

---

# Exploratory Data Analysis

The EDA notebook includes:

- Fund House Distribution
- Category Distribution
- NAV Trend Analysis
- Risk Category Distribution
- AUM Analysis
- Daily Returns Distribution

Notebook:

```
notebooks/03_eda_analysis.ipynb
```

---

# Performance Analytics

Performance metrics computed:

- CAGR
- Annualized Return
- Volatility
- Sharpe Ratio
- Alpha
- Beta
- Maximum Drawdown
- Fund Score

Notebook:

```
notebooks/04_performance_analytics.ipynb
```

---

# Advanced Analytics

Implemented advanced financial analytics including:

- Historical Value at Risk (VaR)
- Conditional Value at Risk (CVaR)
- Rolling Sharpe Ratio
- Investor Cohort Analysis
- SIP Continuity Analysis
- Fund Recommendation System
- Sector Concentration using HHI

Notebook:

```
notebooks/06_advanced_analytics.ipynb
```

---

# Fund Recommendation System

A simple rule-based recommendation engine suggests mutual funds based on an investor's risk appetite.

Run:

```bash
python scripts/recommender.py
```

Example:

```
Available Risk Grades

Moderate
Low
High
Very High
Moderately High

Enter Risk Appetite:
Very High

Top 3 Recommended Funds
```

---

# Power BI Dashboard

The interactive dashboard consists of four pages:

### Industry Overview

- Total AUM
- SIP Inflows
- Folios
- Fund House Comparison

### Fund Performance

- Risk vs Return
- NAV Trend
- Fund Ranking

### Investor Analytics

- Transaction Analysis
- State-wise Investment
- SIP Distribution

### SIP & Market Trends

- SIP vs Market Performance
- Category Inflows
- Monthly Trends

---

# SQL

SQL scripts include:

- Database schema
- Analytical queries
- Ranking queries
- Aggregation queries

Located in:

```
sql/
```

---

# Reports

The project includes:

- Final Project Report (PDF)
- PowerPoint Presentation

Located in:

```
reports/
```

---

# Installation

Clone the repository:

```bash
git clone https://github.com/SathvikaGNaik/mutual-fund-analytics.git
```

Move into the project folder:

```bash
cd mutual-fund-analytics
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the environment:

Windows

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Author

**Sathvika Naik**

Data Analytics Capstone Project

July 2026

---

# License

This project was developed for educational purposes as part of the Bluestock Data Analytics Capstone.
