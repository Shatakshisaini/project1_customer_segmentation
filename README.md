# 🛒 E-Commerce Customer Segmentation & Churn Analysis

**By Shatakshi Saini** | Data Analyst Portfolio Project

---

## 📌 Overview

End-to-end customer analytics using **RFM Analysis** and **K-Means Clustering** on ~10,000 e-commerce orders from 1,000 customers (Jan 2022 – Dec 2023).

**Key Results:**
- Segmented 1,000 customers into 4 groups using K-Means (Silhouette Score: 0.68)
- Identified at-risk segment: ~9% of customers holding ~33% of revenue
- Win-back campaign projected to recover ~₹2.87L annually
- Built interactive dashboards in Power BI and Tableau

---

## 🗂️ Project Structure

```
├── ecommerce_orders.csv                      # Raw dataset (9,990 orders)
├── rfm_segments_output.csv                   # Segmented output
├── Customer_Segmentation_RFM_Analysis.ipynb  # Python notebook
├── powerbi/
│   ├── rfm_customers_powerbi.csv
│   ├── orders_enriched_powerbi.csv
│   ├── segment_summary_powerbi.csv
│   ├── monthly_orders_powerbi.csv
│   └── POWERBI_SETUP_GUIDE.md               # DAX measures + page layouts
├── tableau/
│   ├── rfm_customers_tableau.csv
│   ├── orders_enriched_tableau.csv
│   ├── segment_summary_tableau.csv
│   ├── monthly_orders_tableau.csv
│   └── TABLEAU_SETUP_GUIDE.md               # Calculated fields + build steps
└── screenshots/                             # Add after building dashboards
```

---

## 🔧 Tech Stack

| Tool | Purpose |
|------|---------|
| Python · Pandas · Scikit-learn | RFM pipeline + K-Means clustering |
| Matplotlib · Seaborn | Python visualisations (6 charts) |
| Power BI | 4-page interactive business report |
| Tableau | Public scatter + churn dashboard |

---

## 📈 Segments Found

| Segment | Customers | Revenue Share | Churn Risk | Action |
|---------|-----------|--------------|------------|--------|
| Champions | ~10% | ~35% | Low | Reward & retain |
| Loyal | ~20% | ~30% | Low | Upsell |
| At Risk | ~15% | ~20% | High | Win-back campaign |
| Hibernating | ~25% | ~15% | Very High | Re-engage / suppress |

---

## 📊 Power BI Dashboard

See `powerbi/POWERBI_SETUP_GUIDE.md` — includes all DAX measures and page-by-page build instructions.

**Live report:** *(Paste your published Power BI URL here)*

---

## 📊 Tableau Dashboard

See `tableau/TABLEAU_SETUP_GUIDE.md` — includes all calculated fields and dashboard layout.

**Live dashboard:** *(Paste your Tableau Public URL here)*

---

## 🚀 Run the Python Notebook

```bash
pip install pandas numpy matplotlib seaborn scikit-learn jupyter
jupyter notebook Customer_Segmentation_RFM_Analysis.ipynb
```

---

`Python` `Pandas` `K-Means` `RFM` `Power BI` `DAX` `Tableau` `EDA` `Scikit-learn`

*See also: [Sales Performance Dashboard](https://github.com/shatakshi-saini/retail-sales-dashboard)*
