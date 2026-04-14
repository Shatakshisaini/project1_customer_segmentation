# Tableau Dashboard Guide — Customer Segmentation
## Project 1: E-Commerce Customer Segmentation & Churn Analysis

---

## FILES TO LOAD INTO TABLEAU

| File | Sheet Name in Tableau | Purpose |
|------|-----------------------|---------|
| `rfm_customers_tableau.csv` | Customers | Main RFM + segment data |
| `orders_enriched_tableau.csv` | Orders | Order-level transactions |
| `segment_summary_tableau.csv` | Segment Summary | Pre-aggregated stats |

---

## STEP 1 — CONNECT DATA

1. Open Tableau Desktop (or Tableau Public — free)
2. Click **Connect → Text File**
3. Load `rfm_customers_tableau.csv` first
4. Then drag `orders_enriched_tableau.csv` onto the canvas
5. Join on: `Customers.[customer_id]` = `Orders.[customer_id]`  (Inner Join)

---

## STEP 2 — CALCULATED FIELDS

In any worksheet: **Analysis → Create Calculated Field**

---

### Basic KPIs

```
[Total Revenue]
SUM([Amount])

[Avg Order Value]
SUM([Amount]) / COUNTD([Order Id])

[Customer Count]
COUNTD([Customer Id])

[Revenue per Customer]
SUM([Amount]) / COUNTD([Customer Id])
```

---

### Segment Calculations

```
[Is At Risk]
[Segment] = "At Risk"

[Is High Churn Risk]
[Churn Risk] = "High" OR [Churn Risk] = "Very High"

[At Risk Revenue]
IF [Segment] = "At Risk" THEN [Monetary] ELSE 0 END

[Segment Order]
CASE [Segment]
  WHEN "Champions"       THEN 1
  WHEN "Loyal Customers" THEN 2
  WHEN "At Risk"         THEN 3
  WHEN "Hibernating"     THEN 4
END

[RFM Tier]
IF [Rfm Total] >= 12 THEN "High Value"
ELSEIF [Rfm Total] >= 8 THEN "Mid Value"
ELSE "Low Value"
END
```

---

### Trend Calculations

```
[Month-Year Label]
STR(YEAR([Date Str])) + "-" + 
RIGHT("0" + STR(MONTH([Date Str])), 2)

[Revenue vs Avg]
SUM([Amount]) - WINDOW_AVG(SUM([Amount]))

[Running Total Revenue]
RUNNING_SUM(SUM([Amount]))
```

---

### Color / Formatting

```
[Segment Color]
CASE [Segment]
  WHEN "Champions"       THEN "#1F4E79"
  WHEN "Loyal Customers" THEN "#2E75B6"
  WHEN "At Risk"         THEN "#E67E22"
  WHEN "Hibernating"     THEN "#C0392B"
END

[Churn Risk Color]
CASE [Churn Risk]
  WHEN "Low"       THEN "Green"
  WHEN "High"      THEN "Orange"
  WHEN "Very High" THEN "Red"
END
```

---

## STEP 3 — WORKSHEETS TO BUILD

### Sheet 1: Segment Overview Bar
- Rows: `Segment` (sorted by Segment Order)
- Columns: `SUM(Monetary)`
- Color: `Segment`
- Label: Customer count + Revenue
- Sort: Descending by Monetary

### Sheet 2: RFM Scatter Plot
- Columns: `AVG(Recency)`
- Rows: `AVG(Frequency)`
- Size: `AVG(Monetary)`
- Color: `Segment`
- Detail: `Customer Id`
- Tooltip: Customer ID, Segment, Recency, Frequency, Monetary

### Sheet 3: Monthly Revenue Line
- Columns: `MONTH(Date Str)` → set to continuous
- Rows: `SUM(Amount)`
- Color: `YEAR(Date Str)`
- Mark type: Line

### Sheet 4: Revenue Share Donut
- Use a Pie mark
- Angle: `SUM(Monetary)`
- Color: `Segment`
- To make donut: duplicate axis, set inner to white

### Sheet 5: Churn Risk Heatmap
- Rows: `Segment`
- Columns: `Churn Risk`
- Color: `COUNTD(Customer Id)`
- Label: Count

### Sheet 6: Top 20 At-Risk Customers
- Filter: `Segment = "At Risk"`
- Rows: `Customer Id`
- Columns: `Monetary`, `Recency`, `Frequency`
- Sort by Monetary descending
- Show top 20

### Sheet 7: Category Revenue Bar
- Rows: `Product Category`
- Columns: `SUM(Amount)`
- Color: `Segment`
- Mark: Stacked Bar

---

## STEP 4 — BUILD THE DASHBOARD

1. Click the **+** icon at the bottom to create a new Dashboard
2. Set size: **1366 x 768** (standard desktop) or **Automatic**
3. Drag these sheets in:

```
┌──────────────────────────────────────────┐
│  TITLE: Customer Segmentation Dashboard  │
├────────┬────────┬────────┬───────────────┤
│ KPI 1  │ KPI 2  │ KPI 3  │  KPI 4       │
│ Rev    │ Custs  │ AOV    │ At Risk %     │
├────────┴────────┴────────┴───────────────┤
│  Segment Bar (left) │ Revenue Donut (rt) │
├──────────────────────────────────────────┤
│       RFM Scatter Plot                   │
├──────────────────────┬───────────────────┤
│  Monthly Line Chart  │  Churn Heatmap    │
└──────────────────────┴───────────────────┘
```

4. Add a **Segment filter** (dashboard action) — clicking a segment filters all sheets
5. Add a **Year filter** for 2022 / 2023 toggle

---

## STEP 5 — SAVE AND PUBLISH

### Tableau Public (free):
1. Server → Tableau Public → Save to Tableau Public
2. Copy the public URL
3. Add it to your GitHub README:
   ```
   [View Dashboard on Tableau Public](YOUR_URL_HERE)
   ```

### Save locally:
- File → Save As → `Customer_Segmentation_Dashboard.twbx`
- This packages the data inside — safe to commit to GitHub

---

## SCREENSHOTS TO TAKE FOR GITHUB

- `tableau_overview.png` — Full dashboard view
- `tableau_scatter.png` — RFM scatter plot close-up
- `tableau_churn.png` — Churn heatmap
