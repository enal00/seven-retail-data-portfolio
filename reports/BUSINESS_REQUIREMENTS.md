# Business Requirement Document & Portfolio Charter
## Position Target: Data Analyst Associate - Group Service (Seven Retail)

This document maps our end-to-end data project directly to the **Day-to-Day** responsibilities outlined in Seven Retail's job description.

---

### 1. Data Discovery, Exploration & Insights
- **JD Responsibility:** *Conduct data discovery, exploration, and analysis to generate insights for business processes, products, and performance improvements.*
- **Business Question:** Which product categories and customer segments drive the highest profit margins, and where are the operational bottlenecks (e.g., returns, complaints)?
- **Our Solution:** Automated EDA script (`src/eda_analysis.py`) and markdown report (`reports/EDA_REPORT.md`) uncovering revenue patterns across 120,000 transactions and 5,000 products.

### 2. Metric Ownership & Performance Targets
- **JD Responsibility:** *Own and monitor key business metrics, define performance targets, and propose initiatives to drive improvements.*
- **Business Question:** How do we track Average Order Value (AOV), Gross Profit, and Customer Churn Risk across 200+ store locations to trigger corrective actions?
- **Our Solution:** Apache Superset Executive Dashboard tracking core financial and operational KPIs with actionable store-level filtering.

### 3. Scalable ETL Pipelines
- **JD Responsibility:** *Build, optimize, and maintain scalable ETL pipelines to ensure reliable, accurate, and timely data delivery.*
- **Business Question:** How do we ingest raw, uncleaned multi-store transactional data into a pristine, analysis-ready format automatically?
- **Our Solution:** Python ETL & Cleaning pipeline (`src/data_cleaning.py`) handling missing value imputation, datatype casting, and anomaly detection.

### 4. Data Warehouse & Modeling Best Practices
- **JD Responsibility:** *Implement data warehouse management best practices and develop reliable data models to support key business metrics.*
- **Business Question:** How do we structure data storage (PostgreSQL) for optimal query performance and metric calculation?
- **Our Solution:** Clean relational schema with pre-calculated profit metrics and standardized dimensional attributes (`data/supermarket_cleaned.csv`).

### 5. Reporting Frameworks & Dashboards
- **JD Responsibility:** *Develop and standardize reporting frameworks, dashboards, and visualizations to ensure consistent and accessible insights across teams.*
- **Business Question:** How do we present complex retail data so cross-functional teams (Operations, Finance, Marketing) can make rapid, data-driven decisions?
- **Our Solution:** Standardized Apache Superset visual framework (`http://localhost:8088`) structured into Executive, Store Operations, and Customer Insights tabs.

### 6. Data Quality & Governance
- **JD Responsibility:** *Establish data quality processes to maintain data accuracy, consistency, and reliability.*
- **Business Question:** How do we guarantee zero tolerance for corrupt financial records, negative pricing, or duplicate transactions?
- **Our Solution:** Programmatic data validation checks built into our ingestion pipeline ensuring 100% data integrity before reporting.
