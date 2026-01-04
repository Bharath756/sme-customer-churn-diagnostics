# SME Customer Churn Diagnostics & Root Cause Analysis

## Executive Summary
Customer churn is one of the most critical revenue risks for Small and Medium Enterprises (SMEs).
This project focuses on **diagnosing churn behavior**, identifying **early warning signals**, and uncovering **actionable drivers** behind customer attrition.

Rather than jumping directly to prediction, this project answers a more fundamental business question:
> Why are customers leaving, and what signals indicate churn risk early enough to act?

## 1. Business Problem
SMEs often face:
- Limited visibility into churn drivers  
- Reactive retention strategies  
- Delayed intervention after customers disengage  

### Objectives
- Quantify churn rates across customer segments  
- Identify behavioral, transactional, and tenure-based churn drivers  
- Detect early warning indicators of disengagement  
- Translate insights into business actions  

## 2. Dataset Overview
The dataset represents SME customer activity, including:
- Customer tenure and lifecycle attributes  
- Usage and engagement metrics  
- Transactional behavior  
- Service interaction signals  
- Churn flag (target variable)  

## 3. Approach & Methodology
### Data Quality & Preparation
- Missing value analysis  
- Outlier detection  
- Feature consistency checks  
- Target leakage prevention  

### Exploratory & Diagnostic Analysis
- Overall churn distribution  
- Churn by tenure buckets  
- Usage decline patterns  
- Segment-wise churn behavior  

### Early Warning Indicators
- Sustained usage decline  
- Reduced transaction frequency  
- Short tenure with low engagement  
- Sudden interaction pattern shifts  

## 4. Notebook Walkthrough
- `notebooks/01_eda.ipynb` — Churn EDA, driver analysis, and early warning signal identification

## 5. Key Insights
- Churn follows identifiable behavioral patterns  
- Early disengagement is a stronger indicator than demographics  
- A small customer subset drives disproportionate revenue churn  
- Intervention windows exist before churn occurs  

### Business Recommendations
- Implement early-warning churn monitoring dashboards  
- Trigger retention actions on behavioral thresholds  
- Prioritize high-value customers with disengagement signals  

## 6. Tech Stack
Python, Pandas, NumPy, Matplotlib, Seaborn, Jupyter Notebook

## 7. Next Improvements
- Automate data ingestion pipelines  
- Add churn prediction models  
- Integrate explainability (SHAP)  
- Deploy real-time alerts for retention teams  

## Author
Bharath C  
