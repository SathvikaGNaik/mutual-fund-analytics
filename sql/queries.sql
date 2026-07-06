-- =====================================================
-- Mutual Fund Analytics Capstone
-- Author : Sathvika G Naik
-- Database : SQLite
-- Description : Business SQL Queries for Mutual Fund Analysis
-- =====================================================

---------------------------------------------------------
-- Query 1
-- Number of Funds Managed by Each Fund House
---------------------------------------------------------

SELECT
    fund_house,
    COUNT(*) AS total_funds
FROM fund_master
GROUP BY fund_house
ORDER BY total_funds DESC;


---------------------------------------------------------
-- Query 2
-- Top 10 Schemes by 5-Year Return
---------------------------------------------------------

SELECT
    scheme_name,
    fund_house,
    return_5yr_pct
FROM scheme_performance
ORDER BY return_5yr_pct DESC
LIMIT 10;


---------------------------------------------------------
-- Query 3
-- Top 10 Lowest Expense Ratio Schemes
---------------------------------------------------------

SELECT
    scheme_name,
    fund_house,
    expense_ratio_pct
FROM scheme_performance
ORDER BY expense_ratio_pct ASC
LIMIT 10;


---------------------------------------------------------
-- Query 4
-- Average 5-Year Return by Category
---------------------------------------------------------

SELECT
    category,
    ROUND(AVG(return_5yr_pct),2) AS average_return
FROM scheme_performance
GROUP BY category
ORDER BY average_return DESC;


---------------------------------------------------------
-- Query 5
-- Average Return by Risk Grade
---------------------------------------------------------

SELECT
    risk_grade,
    ROUND(AVG(return_5yr_pct),2) AS average_return
FROM scheme_performance
GROUP BY risk_grade
ORDER BY average_return DESC;


---------------------------------------------------------
-- Query 6
-- Transaction Type Distribution
---------------------------------------------------------

SELECT
    transaction_type,
    COUNT(*) AS total_transactions
FROM investor_transactions
GROUP BY transaction_type
ORDER BY total_transactions DESC;


---------------------------------------------------------
-- Query 7
-- Top 10 States by Total Investment
---------------------------------------------------------

SELECT
    state,
    ROUND(SUM(amount_inr),2) AS total_investment
FROM investor_transactions
GROUP BY state
ORDER BY total_investment DESC
LIMIT 10;


---------------------------------------------------------
-- Query 8
-- Payment Mode Distribution
---------------------------------------------------------

SELECT
    payment_mode,
    COUNT(*) AS total_transactions
FROM investor_transactions
GROUP BY payment_mode
ORDER BY total_transactions DESC;


---------------------------------------------------------
-- Query 9
-- Average Investment Amount by City Tier
---------------------------------------------------------

SELECT
    city_tier,
    ROUND(AVG(amount_inr),2) AS average_investment
FROM investor_transactions
GROUP BY city_tier
ORDER BY average_investment DESC;


---------------------------------------------------------
-- Query 10
-- Average Investment Amount by Age Group
---------------------------------------------------------

SELECT
    age_group,
    ROUND(AVG(amount_inr),2) AS average_investment
FROM investor_transactions
GROUP BY age_group
ORDER BY average_investment DESC;


---------------------------------------------------------
-- Query 11
-- Top 10 Funds by Assets Under Management (AUM)
---------------------------------------------------------

SELECT
    scheme_name,
    fund_house,
    aum_crore
FROM scheme_performance
ORDER BY aum_crore DESC
LIMIT 10;


---------------------------------------------------------
-- Query 12
-- Average Expense Ratio by Fund House
---------------------------------------------------------

SELECT
    fund_house,
    ROUND(AVG(expense_ratio_pct),2) AS average_expense_ratio
FROM scheme_performance
GROUP BY fund_house
ORDER BY average_expense_ratio ASC;


---------------------------------------------------------
-- Query 13
-- Highest Sharpe Ratio Funds
---------------------------------------------------------

SELECT
    scheme_name,
    sharpe_ratio
FROM scheme_performance
ORDER BY sharpe_ratio DESC
LIMIT 10;


---------------------------------------------------------
-- Query 14
-- Highest Alpha Funds
---------------------------------------------------------

SELECT
    scheme_name,
    alpha
FROM scheme_performance
ORDER BY alpha DESC
LIMIT 10;


---------------------------------------------------------
-- Query 15
-- Highest Volatility Funds
---------------------------------------------------------

SELECT
    scheme_name,
    std_dev_ann_pct
FROM scheme_performance
ORDER BY std_dev_ann_pct DESC
LIMIT 10;