# 📊 Mutual Fund Analytics Capstone

A complete end-to-end Mutual Fund Analytics project built using Python, SQL, SQLite, and Power BI.

This project demonstrates the complete data analytics lifecycle:
- Data Ingestion
- Data Cleaning (ETL)
- Database Design
- SQL Analysis
- Exploratory Data Analysis (EDA)
- Dashboard Development
- Performance Analytics

---

## 🚀 Technologies Used

- Python 3.14
- Pandas
- NumPy
- SQLite
- SQLAlchemy
- Requests
- Jupyter Notebook
- Plotly
- Matplotlib
- Power BI
- Git & GitHub

---

## 📁 Project Structure

```text
Mutual_Fund_Analytics/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── db/
│
├── scripts/
│   ├── etl/
│   ├── analytics/
│   └── utils/
│
├── sql/
├── dashboard/
├── reports/
├── notebooks/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ✅ Completed

### Day 1
- Project setup
- GitHub repository
- Data ingestion
- Live NAV API integration
- Fund master exploration
- AMFI validation

### Day 2
- Cleaned NAV History
- Cleaned Investor Transactions
- Validated Scheme Performance
- Modular ETL Pipeline
- SQLite Database
- Database Verification

---

## 🔄 ETL Workflow

```text
Raw CSV
    │
    ▼
Cleaning
    │
    ▼
Processed CSV
    │
    ▼
SQLite Database
    │
    ▼
SQL Analysis
    │
    ▼
Dashboard
```

---

## ▶️ Running the Project

Create the database

```bash
python -m scripts.etl.create_database
```

Validate performance dataset

```bash
python -m scripts.etl.clean_performance
```

Load all datasets

```bash
python -m scripts.etl.load_database
```

Verify database

```bash
python -m scripts.etl.check_database
```

---

## 📌 Upcoming Work

- SQL Queries
- Exploratory Data Analysis
- Performance Metrics
- Power BI Dashboard
- Final Report
- Presentation

---

## 👩‍💻 Author

**Sathvika G Naik**

Electronics & Communication Engineering

Mutual Fund Analytics Capstone Project