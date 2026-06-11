# Bluestock Mutual Fund Analytics Platform

## Overview

The Bluestock Mutual Fund Analytics Platform is a comprehensive data analytics project that analyzes mutual fund performance, investor behavior, industry growth trends, and portfolio risk. The project integrates ETL processes, performance analytics, advanced risk metrics, and Power BI dashboard visualization to provide meaningful insights for investors and financial analysts.

---

## Problem Statement

Mutual fund investors often face challenges in evaluating fund performance, understanding investment risks, tracking industry trends, and selecting suitable investment options. This project aims to develop a centralized analytics platform that simplifies mutual fund analysis through data-driven insights and interactive visualizations.

---

## Objectives

* Build an automated ETL pipeline for mutual fund datasets.
* Store processed data in SQLite.
* Perform Exploratory Data Analysis (EDA).
* Calculate fund performance metrics.
* Implement advanced risk analytics.
* Develop a mutual fund recommendation engine.
* Create an interactive Power BI dashboard.
* Generate actionable business insights.

---

## Technologies Used

* Python
* Pandas
* NumPy
* SQLite
* Matplotlib
* Jupyter Notebook
* Power BI

---

## Project Architecture

Raw CSV Files

↓

ETL Pipeline

↓

Processed Datasets

↓

SQLite Database

↓

EDA & Analytics

↓

Advanced Analytics

↓

Power BI Dashboard

↓

Business Insights

---

## Dataset Description

### Processed Files

* 01_fund_master_clean.csv
* 02_nav_history_clean.csv
* 03_aum_by_fund_house_clean.csv
* 04_monthly_sip_inflows_clean.csv
* 05_category_inflows_clean.csv
* 06_industry_folio_count_clean.csv
* 07_scheme_performance_clean.csv
* 08_investor_transactions_clean.csv
* 09_portfolio_holdings_clean.csv
* 10_benchmark_indices_clean.csv

---

## Project Structure

mutual_fund_analytics/

├── data/

│ ├── raw/

│ └── processed/

├── scripts/

├── notebooks/

├── dashboard/

├── reports/

├── requirements.txt

└── README.md

---

## Setup Instructions

### Clone Repository

```bash
git clone <repository-url>
cd mutual_fund_analytics
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Project

Run the pipeline:

```bash
python scripts/run_pipeline.py
```

Run the recommendation engine:

```bash
python scripts/recommender.py
```

---

## Performance Analytics

Implemented Metrics:

* CAGR
* Alpha
* Beta
* Sharpe Ratio
* Sortino Ratio
* Maximum Drawdown

Generated Outputs:

* cagr.csv
* alpha_beta.csv
* sharpe_sortino.csv
* max_drawdown.csv

---

## Advanced Analytics

Implemented Analytics:

* Historical VaR (95%)
* CVaR
* Rolling 90-Day Sharpe Ratio
* Investor Cohort Analysis
* SIP Continuity Analysis
* Sector HHI Concentration Analysis
* Fund Recommendation Engine

Generated Outputs:

* var_cvar_report.csv
* cohort_analysis.csv
* sip_continuity.csv
* rolling_sharpe_chart.png

---

## Power BI Dashboard

### Page 1 – Industry Overview

* Total AUM
* SIP Inflows
* Folios
* Schemes
* Industry AUM Trend

### Page 2 – Fund Performance

* Return vs Risk Analysis
* Fund Scorecard
* NAV vs Benchmark Comparison

### Page 3 – Investor Analytics

* State-wise Investments
* Transaction Type Analysis
* Age Group Analysis

### Page 4 – SIP & Market Trends

* SIP Growth Trend
* Category Inflows
* Market Benchmark Comparison

---

## Key Findings

* Mutual fund industry AUM demonstrated strong growth.
* SIP contributions remained a major driver of industry expansion.
* Moderate-risk funds generated strong risk-adjusted returns.
* Working-age investors represented the highest participation group.
* Diversified portfolios exhibited lower concentration risk.

---

## Deliverables

* Final_Report.pdf
* Bluestock_MF_Presentation.pptx
* Power BI Dashboard (.pbix)
* Advanced_Analytics.ipynb
* README.md
* GitHub Repository

---

## Future Enhancements

* Machine Learning-based recommendation engine.
* Real-time NAV integration.
* Predictive analytics and forecasting.
* Cloud deployment of dashboards.

---

## Team Members

* Sricharan Medaboina
* Team Members

---

## License

This project was developed for educational and academic purposes only.
