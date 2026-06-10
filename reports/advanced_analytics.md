# Day 5 – Advanced Analytics

## Objective

The objective of Day 5 was to perform advanced mutual fund analytics using historical NAV data, investor transaction data, and portfolio holdings. The analysis focused on risk measurement, investor behavior, portfolio concentration, and fund recommendation techniques.

---

## Tasks Completed

### 1. Historical VaR and CVaR Analysis

Calculated Historical Value at Risk (VaR) at the 95% confidence level for all mutual fund schemes using daily return distributions.

* VaR (95%) = 5th percentile of daily returns
* CVaR (Conditional VaR) = Average loss beyond the VaR threshold

**Output:**

* `var_cvar_report.csv`

---

### 2. Rolling 90-Day Sharpe Ratio

Computed rolling 90-day Sharpe Ratios for selected mutual funds.

Formula:

Sharpe Ratio = (Mean Return / Standard Deviation) × √252

This analysis helped evaluate changes in risk-adjusted performance over time.

**Output:**

* `rolling_sharpe_chart.png`

---

### 3. Investor Cohort Analysis

Investors were grouped based on their first transaction year.

Metrics Calculated:

* Average SIP Amount
* Total Investment Amount
* Number of Investors
* Top Fund Preference

**Output:**

* `cohort_analysis.csv`

---

### 4. SIP Continuity Analysis

Analyzed SIP transaction frequency and continuity.

Methodology:

* Selected investors with at least 6 SIP transactions
* Calculated average gap between SIP dates
* Investors with average gaps greater than 35 days were flagged as "At Risk"

**Output:**

* `sip_continuity.csv`

---

### 5. Fund Recommendation System

Developed a simple mutual fund recommendation engine.

Input:

* Risk Appetite (Low / Moderate / High)

Output:

* Top 3 funds ranked by Sharpe Ratio
* Matching risk category
* 3-Year Return
* Fund House

**Script:**

* `recommender.py`

---

### 6. Sector Concentration Analysis (HHI)

Calculated Herfindahl-Hirschman Index (HHI) to measure portfolio concentration.

Formula:

HHI = Σ(weight²)

Interpretation:

* High HHI → Concentrated Portfolio
* Low HHI → Diversified Portfolio

**Output:**

* `hhi_concentration.csv`

---

## Key Insights

1. Funds with lower VaR and CVaR values demonstrated better downside protection.
2. Rolling Sharpe Ratios showed variation across market cycles, indicating changing risk-adjusted performance.
3. Recent investor cohorts contributed a significant share of total investments.
4. Most SIP investors maintained consistent investment behavior with acceptable transaction gaps.
5. Highly concentrated portfolios exhibited greater concentration risk compared to diversified portfolios.

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Jupyter Notebook

---

## Deliverables

### Notebook

* `05_advanced_analytics.ipynb`

### Scripts

* `recommender.py`

### Reports

* `var_cvar_report.csv`
* `cohort_analysis.csv`
* `sip_continuity.csv`
* `rolling_sharpe_chart.png`
* `hhi_concentration.csv`

---

## Conclusion

Day 5 successfully implemented advanced mutual fund analytics covering risk assessment, investor behavior analysis, portfolio concentration measurement, and recommendation systems. The generated insights provide valuable information for investors and fund managers while demonstrating practical applications of data analytics in the mutual fund industry.
