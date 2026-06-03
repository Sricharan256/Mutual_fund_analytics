CREATE TABLE dim_fund (
    fund_id INTEGER PRIMARY KEY,
    amfi_code INTEGER UNIQUE,
    scheme_name TEXT,
    fund_house TEXT,
    category TEXT
);

CREATE TABLE fact_nav (
    nav_id INTEGER PRIMARY KEY,
    amfi_code INTEGER,
    nav_date DATE,
    nav REAL
);

CREATE TABLE fact_transactions (
    transaction_id INTEGER PRIMARY KEY,
    investor_id INTEGER,
    amfi_code INTEGER,
    transaction_type TEXT,
    amount_inr REAL,
    transaction_date DATE
);

CREATE TABLE fact_performance (
    performance_id INTEGER PRIMARY KEY,
    amfi_code INTEGER,
    return_1yr_pct REAL,
    return_3yr_pct REAL,
    return_5yr_pct REAL,
    sharpe_ratio REAL,
    sortino_ratio REAL
);

CREATE TABLE fact_aum (
    aum_id INTEGER PRIMARY KEY,
    fund_house TEXT,
    aum_crore REAL
);