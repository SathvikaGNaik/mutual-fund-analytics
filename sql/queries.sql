-- ==========================================================
-- BlueStock Mutual Fund Analytics Capstone
-- Author : Sathvika G Naik
-- Database : SQLite (Star Schema)
-- Description : Analytical SQL Queries
-- ==========================================================


/*===========================================================
Query 1
Top 5 Funds by Assets Under Management (AUM)
===========================================================*/

SELECT
    f.scheme_name,
    f.fund_house,
    a.aum_crore
FROM fact_aum a
JOIN dim_fund f
ON a.amfi_code = f.amfi_code
ORDER BY a.aum_crore DESC
LIMIT 5;



/*===========================================================
Query 2
Average Monthly NAV
===========================================================*/

SELECT
    d.year,
    d.month,
    d.month_name,
    ROUND(AVG(n.nav),2) AS average_nav
FROM fact_nav n
JOIN dim_date d
ON n.date_id = d.date_id
GROUP BY
    d.year,
    d.month,
    d.month_name
ORDER BY
    d.year,
    d.month;



/*===========================================================
Query 3
Monthly Average NAV by Fund
===========================================================*/

SELECT
    f.scheme_name,
    d.year,
    d.month_name,
    ROUND(AVG(n.nav),2) AS average_nav
FROM fact_nav n
JOIN dim_fund f
ON n.amfi_code = f.amfi_code
JOIN dim_date d
ON n.date_id = d.date_id
GROUP BY
    f.scheme_name,
    d.year,
    d.month
ORDER BY
    f.scheme_name,
    d.year,
    d.month;



/*===========================================================
Query 4
Transaction Distribution
===========================================================*/

SELECT
    transaction_type,
    COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY transaction_type
ORDER BY total_transactions DESC;



/*===========================================================
Query 5
Top States by Investment
===========================================================*/

SELECT
    state,
    COUNT(*) AS total_transactions,
    ROUND(SUM(amount_inr),2) AS total_investment
FROM fact_transactions
GROUP BY state
ORDER BY total_investment DESC;



/*===========================================================
Query 6
Average Investment by Age Group
===========================================================*/

SELECT
    age_group,
    ROUND(AVG(amount_inr),2) AS average_investment
FROM fact_transactions
GROUP BY age_group
ORDER BY average_investment DESC;



/*===========================================================
Query 7
Average Investment by City Tier
===========================================================*/

SELECT
    city_tier,
    ROUND(AVG(amount_inr),2) AS average_investment
FROM fact_transactions
GROUP BY city_tier
ORDER BY average_investment DESC;



/*===========================================================
Query 8
Payment Mode Distribution
===========================================================*/

SELECT
    payment_mode,
    COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY payment_mode
ORDER BY total_transactions DESC;



/*===========================================================
Query 9
Funds with Expense Ratio Below 1%
===========================================================*/

SELECT
    scheme_name,
    fund_house,
    expense_ratio_pct
FROM dim_fund
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct ASC;



/*===========================================================
Query 10
Average 5-Year Return by Category
===========================================================*/

SELECT
    f.category,
    ROUND(AVG(p.return_5yr_pct),2) AS average_return
FROM fact_performance p
JOIN dim_fund f
ON p.amfi_code = f.amfi_code
GROUP BY f.category
ORDER BY average_return DESC;



/*===========================================================
Query 11
Top 10 Funds by 5-Year Return
===========================================================*/

SELECT
    f.scheme_name,
    f.fund_house,
    p.return_5yr_pct
FROM fact_performance p
JOIN dim_fund f
ON p.amfi_code = f.amfi_code
ORDER BY p.return_5yr_pct DESC
LIMIT 10;



/*===========================================================
Query 12
Highest Sharpe Ratio Funds
===========================================================*/

SELECT
    f.scheme_name,
    p.sharpe_ratio
FROM fact_performance p
JOIN dim_fund f
ON p.amfi_code = f.amfi_code
ORDER BY p.sharpe_ratio DESC
LIMIT 10;



/*===========================================================
Query 13
Highest Alpha Funds
===========================================================*/

SELECT
    f.scheme_name,
    p.alpha
FROM fact_performance p
JOIN dim_fund f
ON p.amfi_code = f.amfi_code
ORDER BY p.alpha DESC
LIMIT 10;



/*===========================================================
Query 14
Highest Volatility Funds
===========================================================*/

SELECT
    f.scheme_name,
    p.std_dev_ann_pct
FROM fact_performance p
JOIN dim_fund f
ON p.amfi_code = f.amfi_code
ORDER BY p.std_dev_ann_pct DESC
LIMIT 10;



/*===========================================================
Query 15
Highest Rated Funds
===========================================================*/

SELECT
    f.scheme_name,
    p.morningstar_rating
FROM fact_performance p
JOIN dim_fund f
ON p.amfi_code = f.amfi_code
ORDER BY
    p.morningstar_rating DESC,
    p.return_5yr_pct DESC;