# Mutual Fund Analytics Data Dictionary

## 01_fund_master_clean.csv

| Column        | Data Type | Description                   |
| ------------- | --------- | ----------------------------- |
| amfi_code     | INTEGER   | Unique AMFI scheme code       |
| scheme_name   | TEXT      | Mutual fund scheme name       |
| fund_house    | TEXT      | Asset Management Company      |
| category      | TEXT      | Fund category                 |
| sub_category  | TEXT      | Fund sub-category             |
| expense_ratio | REAL      | Expense ratio charged by fund |
| risk_grade    | TEXT      | Risk classification           |
| fund_manager  | TEXT      | Name of fund manager          |

---

## 02_nav_history_clean.csv

| Column    | Data Type | Description      |
| --------- | --------- | ---------------- |
| amfi_code | INTEGER   | Mutual fund code |
| date      | DATE      | NAV date         |
| nav       | REAL      | Net Asset Value  |

---

## 03_aum_by_fund_house_clean.csv

| Column     | Data Type | Description                      |
| ---------- | --------- | -------------------------------- |
| fund_house | TEXT      | Fund house name                  |
| quarter    | TEXT      | Reporting quarter                |
| aum_crore  | REAL      | Assets Under Management in Crore |

---

## 04_monthly_sip_inflows_clean.csv

| Column              | Data Type | Description                 |
| ------------------- | --------- | --------------------------- |
| month               | TEXT      | Reporting month             |
| sip_inflow_crore    | REAL      | SIP inflow amount           |
| active_sip_accounts | INTEGER   | Active SIP accounts         |
| sip_aum_crore       | REAL      | SIP Assets Under Management |

---

## 05_category_inflows_clean.csv

| Column           | Data Type | Description       |
| ---------------- | --------- | ----------------- |
| category         | TEXT      | Fund category     |
| month            | TEXT      | Reporting month   |
| net_inflow_crore | REAL      | Net inflow amount |

---

## 06_industry_folio_count_clean.csv

| Column            | Data Type | Description        |
| ----------------- | --------- | ------------------ |
| category          | TEXT      | Equity/Debt/Hybrid |
| folio_count_crore | REAL      | Total folio count  |

---

## 07_scheme_performance_clean.csv

| Column            | Data Type | Description       |
| ----------------- | --------- | ----------------- |
| amfi_code         | INTEGER   | Scheme code       |
| scheme_name       | TEXT      | Mutual fund name  |
| return_1yr_pct    | REAL      | 1 Year Return (%) |
| return_3yr_pct    | REAL      | 3 Year Return (%) |
| return_5yr_pct    | REAL      | 5 Year Return (%) |
| alpha             | REAL      | Alpha value       |
| beta              | REAL      | Beta value        |
| sharpe_ratio      | REAL      | Sharpe ratio      |
| sortino_ratio     | REAL      | Sortino ratio     |
| expense_ratio_pct | REAL      | Expense ratio (%) |
| risk_grade        | TEXT      | Risk category     |

---

## 08_investor_transactions_clean.csv

| Column             | Data Type | Description             |
| ------------------ | --------- | ----------------------- |
| investor_id        | INTEGER   | Investor identifier     |
| transaction_date   | DATE      | Transaction date        |
| amfi_code          | INTEGER   | Mutual fund code        |
| transaction_type   | TEXT      | SIP/Lumpsum/Redemption  |
| amount_inr         | REAL      | Transaction amount      |
| state              | TEXT      | Investor state          |
| city               | TEXT      | Investor city           |
| city_tier          | TEXT      | Tier classification     |
| age_group          | TEXT      | Investor age group      |
| gender             | TEXT      | Investor gender         |
| annual_income_lakh | REAL      | Annual income           |
| payment_mode       | TEXT      | Payment method          |
| kyc_status         | TEXT      | KYC verification status |

---

## 09_portfolio_holdings_clean.csv

| Column     | Data Type | Description                 |
| ---------- | --------- | --------------------------- |
| amfi_code  | INTEGER   | Fund code                   |
| stock_name | TEXT      | Stock held by fund          |
| sector     | TEXT      | Industry sector             |
| weight_pct | REAL      | Portfolio weight percentage |

---

## 10_benchmark_indices_clean.csv

| Column      | Data Type | Description         |
| ----------- | --------- | ------------------- |
| date        | DATE      | Index date          |
| index_name  | TEXT      | Benchmark index     |
| close_value | REAL      | Closing index value |
