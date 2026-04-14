# Power BI Dashboard Guide — Customer Segmentation
## Project 1: E-Commerce Customer Segmentation & Churn Analysis

---

## FILES TO LOAD INTO POWER BI

| File | Table Name in Power BI | Purpose |
|------|------------------------|---------|
| `rfm_customers_powerbi.csv` | `Customers` | Main customer RFM table |
| `orders_enriched_powerbi.csv` | `Orders` | Transaction-level data |
| `segment_summary_powerbi.csv` | `SegmentSummary` | Pre-aggregated segment stats |
| `monthly_orders_powerbi.csv` | `MonthlyOrders` | Monthly trend data |

---

## STEP 1 — LOAD DATA

1. Open Power BI Desktop
2. Click **Home → Get Data → Text/CSV**
3. Load each of the 4 files above
4. After loading, rename each table in the right-hand pane to the names above

---

## STEP 2 — SET RELATIONSHIPS (Model View)

Click the **Model** icon (left sidebar) and create these relationships:

```
Customers[customer_id]  →  Orders[customer_id]    (One-to-Many)
Customers[Segment]      →  SegmentSummary[Segment] (Many-to-One)
```

---

## STEP 3 — DAX MEASURES

Create a dedicated **Measures Table** (Home → Enter Data → name it "Measures", leave blank, click Load).

Then click on the Measures table and add each measure below using **New Measure**:

---

### KPI Measures

```dax
Total Revenue = SUM(Orders[amount])

Total Customers = DISTINCTCOUNT(Customers[customer_id])

Avg Order Value = DIVIDE([Total Revenue], COUNTROWS(Orders), 0)

Avg Recency (Days) = AVERAGE(Customers[Recency])

Avg Frequency = AVERAGE(Customers[Frequency])

Avg Monetary = AVERAGE(Customers[Monetary])
```

---

### Segment Measures

```dax
Champions Count =
CALCULATE(
    DISTINCTCOUNT(Customers[customer_id]),
    Customers[Segment] = "Champions"
)

At Risk Count =
CALCULATE(
    DISTINCTCOUNT(Customers[customer_id]),
    Customers[Segment] = "At Risk"
)

At Risk Revenue =
CALCULATE(
    SUM(Customers[Monetary]),
    Customers[Segment] = "At Risk"
)

At Risk Revenue % =
DIVIDE(
    [At Risk Revenue],
    SUM(Customers[Monetary]),
    0
) * 100

High Churn Risk Count =
CALCULATE(
    DISTINCTCOUNT(Customers[customer_id]),
    Customers[Churn_Risk] IN {"High", "Very High"}
)
```

---

### Trend Measures

```dax
MoM Revenue Change =
VAR CurrentMonth = MAX(Orders[month])
VAR CurrentYear  = MAX(Orders[year])
VAR ThisMonth    = CALCULATE([Total Revenue],
                    Orders[month] = CurrentMonth,
                    Orders[year]  = CurrentYear)
VAR LastMonth    = CALCULATE([Total Revenue],
                    Orders[month] = CurrentMonth - 1,
                    Orders[year]  = CurrentYear)
RETURN
DIVIDE(ThisMonth - LastMonth, LastMonth, 0) * 100

YoY Revenue Growth =
VAR Rev2023 = CALCULATE([Total Revenue], Orders[year] = 2023)
VAR Rev2022 = CALCULATE([Total Revenue], Orders[year] = 2022)
RETURN DIVIDE(Rev2023 - Rev2022, Rev2022, 0) * 100
```

---

## STEP 4 — DASHBOARD PAGES TO BUILD

### Page 1: Executive Overview
| Visual | Fields |
|--------|--------|
| Card | Total Revenue |
| Card | Total Customers |
| Card | Avg Order Value |
| Card | At Risk Revenue % |
| Donut Chart | Segment → Customer_Count |
| Clustered Bar | Segment → Total_Revenue |
| Line Chart | year + month_name → Revenue (from Orders) |

### Page 2: Segment Deep Dive
| Visual | Fields |
|--------|--------|
| Matrix | Segment × Avg_Recency, Avg_Frequency, Avg_Monetary |
| Scatter Plot | X=Recency, Y=Frequency, Size=Monetary, Color=Segment |
| Stacked Bar | Segment → Churn_Risk count |
| Table | customer_id, Segment, Churn_Risk, Action_Recommended (from Customers) |
| Slicer | Churn_Risk |
| Slicer | Segment |

### Page 3: Churn Risk Analysis
| Visual | Fields |
|--------|--------|
| KPI Card | At Risk Count |
| KPI Card | At Risk Revenue |
| Gauge | At Risk Revenue % (target = 20%) |
| Bar Chart | Segment → Revenue (sorted by churn risk) |
| Treemap | Segment → Customer_Count |
| Table | Top 20 At-Risk customers by Monetary |

### Page 4: Order Trends
| Visual | Fields |
|--------|--------|
| Line Chart | Monthly revenue by Segment |
| Bar Chart | Product category by revenue |
| Pie Chart | Payment method distribution |
| Bar Chart | City-wise revenue |
| Slicer | Year |
| Slicer | Segment |

---

## STEP 5 — FORMATTING TIPS

- Theme: Use "Executive" or "Accessible City Park" built-in themes
- Segment color mapping:
  - Champions → #1F4E79 (dark blue)
  - Loyal Customers → #2E75B6 (blue)
  - At Risk → #E67E22 (orange)
  - Hibernating → #C0392B (red)
- Add company name "E-Commerce Analytics" in the header text box
- Enable drill-through on customer_id for detail pages

---

## STEP 6 — PUBLISH (optional)

1. Save as `Customer_Segmentation_Dashboard.pbix`
2. File → Publish → My Workspace
3. Copy the published URL and paste it in your GitHub README

---

## DASHBOARD SCREENSHOTS TO TAKE FOR GITHUB

After building, take screenshots and save in the `screenshots/` folder:
- `powerbi_overview.png` — Page 1 full dashboard
- `powerbi_segments.png` — Page 2 segment matrix + scatter
- `powerbi_churn.png` — Page 3 churn analysis
