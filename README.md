# SME Customer Churn Diagnostics

## 📌 Business Problem
Small and Medium Enterprise (SME) customers exhibit higher churn rates, directly impacting recurring revenue and long-term profitability.  
This project aims to **diagnose the key drivers of SME customer churn** and demonstrate how data-driven insights can support targeted retention strategies.

---

## 🎯 Objective
- Identify behavioral and contractual factors associated with customer churn
- Quantify churn patterns using exploratory analysis
- Validate insights using an interpretable baseline predictive model
- Translate analytical findings into business-relevant insights

---

## 📊 Dataset
- **Source:** IBM Telco Customer Churn Dataset (public)
- **Adaptation:** Variables reframed to approximate SME energy customers
- **Size:** ~7,000 customers with demographic, pricing, contract, and service attributes

> Note: The focus of this project is analytical reasoning and insight generation rather than industry-specific raw data.

---

## 🔍 Key Analyses Performed

### 1. Churn Overview
- Overall churn rate calculation
- Comparison of churned vs retained customers

### 2. Tenure & Contract Analysis
- Churn likelihood vs customer tenure
- Contract types associated with higher churn
- Early-lifecycle churn risk identification

### 3. Pricing & Payment Sensitivity
- Monthly charge distributions by churn status
- Payment method impact on churn
- Pricing-related churn signals

### 4. Service & Feature Analysis
- Relationship between number of subscribed services and churn
- Identification of low-engagement, high-risk customers

---

## 🤖 Churn Modeling (Explainable Baseline)

### Modeling Approach
- **Model:** Logistic Regression
- **Reason:** Interpretability, stability, and business explainability
- **Target Variable:** Binary churn flag

### Features Used
- Tenure
- Monthly charges
- Contract type
- Payment method
- Service count

### Model Evaluation
- Train/Test split with stratification
- Metrics: Precision, Recall, F1-score, ROC AUC
- **ROC AUC:** ~0.83

> An ROC AUC of ~0.83 indicates strong separation between churned and retained customers even with a simple baseline model.

### Class Imbalance Consideration
Churn is a minority class (~25–30%), explaining lower recall for churned customers and highlighting the need for threshold tuning in production settings.

---

## 💡 Key Business Insights
- Churn risk is highest early in the customer lifecycle
- Month-to-month contracts show significantly higher churn
- Higher monthly charges correlate with increased churn probability
- Customers with fewer subscribed services are more likely to churn

---

## 🚀 Next Steps
- Experiment with tree-based models (Random Forest, XGBoost)
- Tune decision thresholds for retention-focused recall
- Add SHAP for feature-level explainability
- Simulate retention interventions and cost impact

---

## 🛠 Tools & Technologies
- Python
- Pandas, NumPy
- Matplotlib
- Scikit-learn
- Jupyter Notebook

---

## 📁 Repository Structure
sme-customer-churn-diagnostics/
│
├── data/
│ └── raw/
│ └── telco_customer_churn.csv
│
├── notebooks/
│ └── 01_eda.ipynb
│
├── README.md
└── LICENSE

---

## 📌 Summary
This project demonstrates an end-to-end churn diagnostics workflow — from business problem framing to analytical insights and explainable modeling — aligned with real-world SME retention decision-making.
