-- ==================================================
-- Query 1: Top 5 Fund Houses by AUM
-- ==================================================

SELECT
fund_house,
SUM(aum_crore) AS total_aum
FROM 03_aum_by_fund_house_clean
GROUP BY fund_house
ORDER BY total_aum DESC
LIMIT 5;

-- ==================================================
-- Query 2: Average NAV Across All Funds
-- ==================================================

SELECT
ROUND(AVG(nav),2) AS average_nav
FROM 02_nav_history_clean;

-- ==================================================
-- Query 3: Number of Transactions by State
-- ==================================================

SELECT
state,
COUNT(*) AS total_transactions
FROM 08_investor_transactions_clean
GROUP BY state
ORDER BY total_transactions DESC;

-- ==================================================
-- Query 4: SIP Transaction Count
-- ==================================================

SELECT
COUNT(*) AS sip_transactions
FROM 08_investor_transactions_clean
WHERE transaction_type = 'SIP';

-- ==================================================
-- Query 5: Funds with Expense Ratio Below 1%
-- ==================================================

SELECT
scheme_name,
expense_ratio_pct
FROM 07_scheme_performance_clean
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct;

-- ==================================================
-- Query 6: Top 10 Funds by 5-Year Return
-- ==================================================

SELECT
scheme_name,
return_5yr_pct
FROM 07_scheme_performance_clean
ORDER BY return_5yr_pct DESC
LIMIT 10;

-- ==================================================
-- Query 7: Highest Sharpe Ratio Funds
-- ==================================================

SELECT
scheme_name,
sharpe_ratio
FROM 07_scheme_performance_clean
ORDER BY sharpe_ratio DESC
LIMIT 10;

-- ==================================================
-- Query 8: Average Transaction Amount by State
-- ==================================================

SELECT
state,
ROUND(AVG(amount_inr),2) AS avg_amount
FROM 08_investor_transactions_clean
GROUP BY state
ORDER BY avg_amount DESC;

-- ==================================================
-- Query 9: Fund Count by Category
-- ==================================================

SELECT
category,
COUNT(*) AS fund_count
FROM 01_fund_master_clean
GROUP BY category
ORDER BY fund_count DESC;

-- ==================================================
-- Query 10: Average Returns by Category
-- ==================================================

SELECT
category,
ROUND(AVG(return_3yr_pct),2) AS avg_3yr_return
FROM 07_scheme_performance_clean
GROUP BY category
ORDER BY avg_3yr_return DESC;
