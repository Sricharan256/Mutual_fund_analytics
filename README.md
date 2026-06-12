# Bluestock Mutual Fund Analytics Platform

## Project Overview

The Bluestock Mutual Fund Analytics Platform is an end-to-end data analytics solution developed to analyze mutual fund performance, investor behavior, industry trends, and portfolio risk. The project combines ETL pipelines, SQLite database management, exploratory data analysis, performance analytics, advanced risk metrics, and Power BI dashboard visualization to provide actionable insights for investors and financial analysts.

The platform enables users to understand mutual fund growth trends, evaluate fund performance, monitor investment risk, and analyze investor participation through data-driven decision-making.

---

# Problem Statement

The mutual fund industry generates large volumes of data related to fund performance, assets under management, investor transactions, portfolio holdings, and benchmark indices. Analyzing this information manually is time-consuming and often results in fragmented insights.

This project aims to develop a centralized analytics platform that automates data processing, performs advanced analytics, and presents insights through interactive dashboards.

---

# Objectives

* Build an automated ETL pipeline for mutual fund datasets.
* Store processed data in SQLite.
* Perform Exploratory Data Analysis (EDA).
* Calculate performance metrics such as CAGR, Sharpe Ratio, Sortino Ratio, Alpha, and Beta.
* Implement advanced risk analytics including VaR and CVaR.
* Develop a mutual fund recommendation engine.
* Create an interactive Power BI dashboard.
* Generate actionable business insights.

---

# Technologies Used

* Python
* Pandas
* NumPy
* SQLite
* Matplotlib
* Jupyter Notebook
* Power BI Desktop
* Git & GitHub

---

# Project Architecture

```text
Raw CSV Files
      │
      ▼
 ETL Pipeline
      │
      ▼
 Cleaned Datasets
      │
      ▼
 SQLite Database
      │
      ├────────────► EDA Analysis
      │
      ├────────────► Performance Analytics
      │
      ├────────────► Advanced Analytics
      │
      ▼
 Power BI Dashboard
      │
      ▼
 Business Insights
```

---

# Dataset Description

The project uses ten cleaned datasets:

| Dataset                            | Description                  |
| ---------------------------------- | ---------------------------- |
| 01_fund_master_clean.csv           | Mutual fund scheme details   |
| 02_nav_history_clean.csv           | Historical NAV records       |
| 03_aum_by_fund_house_clean.csv     | AUM by AMC                   |
| 04_monthly_sip_inflows_clean.csv   | Monthly SIP inflows          |
| 05_category_inflows_clean.csv      | Category-wise inflows        |
| 06_industry_folio_count_clean.csv  | Industry folio statistics    |
| 07_scheme_performance_clean.csv    | Fund performance metrics     |
| 08_investor_transactions_clean.csv | Investor transaction records |
| 09_portfolio_holdings_clean.csv    | Portfolio holdings           |
| 10_benchmark_indices_clean.csv     | Benchmark index performance  |

---

# Project Structure

```text
mutual_fund_analytics/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── 03_eda_analysis.ipynb
│   ├── 04_performance_analytics.ipynb
│   └── 05_advanced_analytics.ipynb
│
├── scripts/
│   ├── data_ingestion.py
│   ├── clean_transactions.py
│   ├── load_sqlite.py
│   ├── calculate_cagr.py
│   ├── calculate_alpha_beta.py
│   ├── calculate_sharpe_sortino.py
│   ├── calculate_drawdown.py
│   ├── recommender.py
│   └── run_pipeline.py
│
├── sql/
│   ├── schema.sql
│   └── queries.sql
│
├── dashboard/
│   ├── bluestock_mf_dashboard.pbix
│   └── bluestock_mf_dashboard.pdf
│
├── reports/
│   ├── Final_Report.pdf
│   ├── Presentation.pptx
│   ├── var_cvar_report.csv
│   ├── cohort_analysis.csv
│   ├── sip_continuity.csv
│   └── rolling_sharpe_chart.png
│
├── charts/
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

# Installation

## Clone Repository

```bash
git clone <repository-url>
cd mutual_fund_analytics
```

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Git Bash

```bash
source venv/Scripts/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# How to Run

### Run ETL Pipeline

```bash
python scripts/run_pipeline.py
```

### Run Performance Analytics

```bash
python scripts/calculate_cagr.py
python scripts/calculate_alpha_beta.py
python scripts/calculate_sharpe_sortino.py
```

### Run Fund Recommendation Engine

```bash
python scripts/recommender.py
```

---

# Performance Analytics

Implemented metrics:

* CAGR
* Alpha
* Beta
* Sharpe Ratio
* Sortino Ratio
* Maximum Drawdown

Generated outputs:

* cagr.csv
* alpha_beta.csv
* sharpe_sortino.csv
* max_drawdown.csv

---

# Advanced Analytics

Implemented analytics:

* Historical VaR (95%)
* Conditional VaR (CVaR)
* Rolling 90-Day Sharpe Ratio
* Investor Cohort Analysis
* SIP Continuity Analysis
* Sector HHI Concentration Analysis
* Fund Recommendation Engine

Generated outputs:

* var_cvar_report.csv
* cohort_analysis.csv
* sip_continuity.csv
* rolling_sharpe_chart.png

---

# Dashboard Overview

### Page 1 – Industry Overview

* Total AUM
* SIP Inflows
* Total Folios
* Total Schemes
* Industry AUM Trend

### Page 2 – Fund Performance

* Return vs Risk Analysis
* Fund Scorecard
* NAV vs Benchmark Comparison

### Page 3 – Investor Analytics

* State-wise Investments
* Transaction Type Analysis
* Age Group Analysis
* Monthly Transaction Trends

### Page 4 – SIP & Market Trends

* SIP Growth Trend
* Category Inflows
* Market Benchmark Comparison

---

# Key Findings

1. Mutual fund industry AUM demonstrated strong growth during the analysis period.
2. SIP contributions remained a major driver of industry expansion.
3. Moderate-risk funds generated strong risk-adjusted returns.
4. Working-age investors represented the largest investor segment.
5. Diversified portfolios exhibited lower concentration risk than highly concentrated portfolios.

---

# Deliverables

* Final_Report.pdf
* Presentation.pptx
* bluestock_mf_dashboard.pbix
* bluestock_mf_dashboard.pdf
* 05_advanced_analytics.ipynb
* README.md
* GitHub Repository

---

# Version

Current Release: **v1.0**

This version includes:

* ETL Pipeline
* SQLite Integration
* EDA Analysis
* Performance Analytics
* Advanced Analytics
* Interactive Dashboard
* Final Documentation

---

# Future Enhancements

* Machine Learning-based recommendation engine
* Real-time NAV integration
* Predictive analytics and forecasting
* Streamlit web application
* Portfolio optimization models

---

# Team Members

* Sricharan Medaboina
* Prashanth Reddy
* Sri Satya Thanuj Vummidi
* Praveen Kolluri

---

# License

This project was developed for educational and academic purposes only.
