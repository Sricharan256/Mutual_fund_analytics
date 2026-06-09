# Performance Analytics Report

## Project Title

Mutual Fund Analytics Platform – Day 4 Performance Analytics

## Objective

The objective of this phase is to evaluate the performance of mutual fund schemes using various financial metrics. The analysis includes daily return calculations, CAGR computation, risk-adjusted performance measures, benchmark comparison, drawdown analysis, and creation of a composite fund scorecard.

---

## Datasets Used

### 1. NAV History

File: `02_nav_history_clean.csv`

Contains daily NAV values for 40 mutual fund schemes from 2022–2026.

### 2. Scheme Performance

File: `07_scheme_performance_clean.csv`

Contains return metrics, expense ratio, alpha, beta, Sharpe ratio, and risk indicators.

### 3. Benchmark Indices

File: `10_benchmark_indices_clean.csv`

Contains historical values for NIFTY50 and NIFTY100 benchmark indices.

---

# Methodology

## 1. Daily Return Calculation

Daily return measures the percentage change in NAV between consecutive trading days.

Formula:

Daily Return = (NAV_t / NAV_(t-1)) - 1

Python Method:

* Sort NAV data by fund and date.
* Group by AMFI code.
* Apply percentage change calculation.

Output File:

`nav_daily_returns.csv`

---

## 2. CAGR Calculation

Compound Annual Growth Rate (CAGR) measures the annualized growth rate of a fund over a period.

Formula:

CAGR = (Ending NAV / Beginning NAV)^(1/n) - 1

Where:

* Ending NAV = Latest NAV
* Beginning NAV = Initial NAV
* n = Number of years

Output File:

`cagr.csv`

---

## 3. Sharpe Ratio

Sharpe Ratio measures risk-adjusted returns.

Formula:

Sharpe Ratio = (Rp - Rf) / Std(Rp)

Where:

* Rp = Annualized Portfolio Return
* Rf = Risk-Free Rate (6.5%)
* Std(Rp) = Annualized Standard Deviation

Interpretation:

* Higher Sharpe Ratio indicates better risk-adjusted performance.
* Negative Sharpe Ratio indicates underperformance relative to risk-free rate.

Output File:

`sharpe_sortino.csv`

---

## 4. Sortino Ratio

Sortino Ratio measures downside risk-adjusted performance.

Formula:

Sortino Ratio = (Rp - Rf) / Downside Deviation

Where:

* Only negative returns are considered in the denominator.
* Provides a more accurate measure of harmful volatility.

Output File:

`sharpe_sortino.csv`

---

## 5. Alpha and Beta

Alpha and Beta were computed using linear regression against the NIFTY100 benchmark.

### Beta

Measures sensitivity of fund returns relative to benchmark returns.

Interpretation:

* Beta > 1 : More volatile than benchmark
* Beta < 1 : Less volatile than benchmark

### Alpha

Measures excess return beyond benchmark expectations.

Formula:

Alpha = Intercept × 252

Output File:

`alpha_beta.csv`

---

## 6. Maximum Drawdown

Maximum Drawdown measures the largest decline from a historical peak.

Formula:

Drawdown = NAV / Running_Max - 1

Interpretation:

* Lower drawdown indicates better downside protection.
* Higher drawdown indicates greater risk.

Output File:

`max_drawdown.csv`

---

## 7. Fund Scorecard

A composite score was developed to rank all mutual funds.

Scoring Weights:

| Metric                     | Weight |
| -------------------------- | ------ |
| 3 Year Return              | 30%    |
| Sharpe Ratio               | 25%    |
| Alpha                      | 20%    |
| Expense Ratio (Inverse)    | 15%    |
| Maximum Drawdown (Inverse) | 10%    |

Formula:

Score =
30% × Return Rank +
25% × Sharpe Rank +
20% × Alpha Rank +
15% × Expense Ratio Rank +
10% × Drawdown Rank

Output File:

`fund_scorecard.csv`

---

## 8. Benchmark Comparison

The top five funds based on scorecard rankings were compared against benchmark indices.

Benchmarks:

* NIFTY50
* NIFTY100

Metrics Evaluated:

* NAV Growth
* Relative Performance
* Tracking Error

Output Chart:

`benchmark_comparison.png`

---

# Deliverables

## Source Code

* calculate_daily_returns.py
* calculate_cagr.py
* calculate_sharpe_sortino.py
* calculate_alpha_beta.py
* calculate_drawdown.py
* generate_scorecard.py
* benchmark_comparison.py

## Output Files

* nav_daily_returns.csv
* cagr.csv
* sharpe_sortino.csv
* alpha_beta.csv
* max_drawdown.csv
* fund_scorecard.csv

## Visualizations

* benchmark_comparison.png

## Notebook

* Performance_Analytics.ipynb

---

# Key Insights

1. Daily returns showed a realistic distribution with moderate volatility.
2. CAGR analysis highlighted long-term fund growth trends.
3. Several funds achieved Sharpe Ratios above 1, indicating strong risk-adjusted performance.
4. Alpha analysis identified funds consistently outperforming the benchmark.
5. Maximum Drawdown revealed the resilience of top-performing funds during market corrections.
6. The composite scorecard enabled objective ranking of all schemes.
7. Benchmark comparison demonstrated the relative performance of top-ranked funds against NIFTY indices.

---

# Conclusion

The performance analytics framework successfully evaluated mutual fund performance using return, risk, and benchmark-based metrics. The generated scorecard provides a data-driven approach for ranking mutual funds and identifying high-quality investment opportunities.
