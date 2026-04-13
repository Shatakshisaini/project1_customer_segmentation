# 🛒 E-Commerce Customer Segmentation & Churn Analysis

**By Shatakshi Saini** | Data Analyst Portfolio Project

---

## 📌 Overview

End-to-end customer analytics project using **RFM Analysis** and **K-Means Clustering** on ~10,000 e-commerce orders from 1,000 customers across Indian cities (Jan 2022 – Dec 2023).

**Key Results:**
- Segmented customers into 4 actionable groups using K-Means (Silhouette Score: 0.68)
- Identified a high-value at-risk segment (~9% of customers, ~33% of revenue)
- Recommended win-back campaign projected to recover ₹X in annual revenue
- Reduced manual segmentation effort by automating the full RFM pipeline

---

## 🗂️ Project Structure

```
ecommerce-customer-segmentation/
│
├── ecommerce_orders.csv                    # Raw dataset (9,990 orders)
├── Customer_Segmentation_RFM_Analysis.ipynb # Main analysis notebook
├── rfm_segments_output.csv                 # Final segmented output
│
├── charts/
│   ├── eda_overview.png
│   ├── monthly_revenue.png
│   ├── rfm_distributions.png
│   ├── elbow_silhouette.png
│   ├── segmentation_dashboard.png
│   └── churn_analysis.png
│
└── README.md
```

---

## 🔧 Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.10 | Core language |
| Pandas | Data manipulation & RFM aggregation |
| NumPy | Numerical operations |
| Scikit-learn | K-Means clustering, StandardScaler, Silhouette Score |
| Matplotlib | All charts and dashboards |
| Seaborn | Statistical visualisations |

---

## 📊 Methodology

### Step 1 — Data Cleaning
- Removed duplicate order IDs
- Filtered invalid/negative revenue records
- Capped outliers at 99.5th percentile

### Step 2 — RFM Feature Engineering
- **Recency**: Days since last purchase (reference date = day after last order)
- **Frequency**: Total number of orders per customer
- **Monetary**: Total spend per customer

### Step 3 — RFM Scoring (Quintile-based 1–5)
Each customer gets R, F, M scores from 1 (worst) to 5 (best)

### Step 4 — K-Means Clustering
- Used Elbow Method + Silhouette Score to select K=4
- Applied StandardScaler before clustering
- Mapped clusters to business-readable labels

### Step 5 — Churn Analysis
- Identified high-value at-risk customers
- Quantified revenue impact and projected retention gains

---

## 📈 Key Findings

| Segment | Customers | Avg Spend | Avg Recency | Action |
|---------|-----------|-----------|-------------|--------|
| Champions 🏆 | ~10% | Highest | <30 days | Reward & retain |
| Loyal 💚 | ~20% | High | 15-60 days | Upsell |
| At-Risk ⚠️ | ~15% | Medium | 90-200 days | Win-back campaign |
| Hibernating 💤 | ~25% | Low | >200 days | Re-engagement / suppress |

---

## 🚀 How to Run

```bash
# Clone the repo
git clone https://github.com/shatakshi-saini/ecommerce-customer-segmentation.git
cd ecommerce-customer-segmentation

# Install dependencies
pip install pandas numpy matplotlib seaborn scikit-learn

# Run the notebook
jupyter notebook Customer_Segmentation_RFM_Analysis.ipynb
```

---

## 💼 Skills Demonstrated

`Python` `Pandas` `SQL-style aggregation` `Scikit-learn` `K-Means Clustering` `RFM Analysis` `Data Cleaning` `EDA` `Business Insights` `Matplotlib` `Seaborn`

---

*Part of my Data Analyst portfolio. See also: [Sales Performance Dashboard](https://github.com/shatakshi-saini/retail-sales-dashboard)*
