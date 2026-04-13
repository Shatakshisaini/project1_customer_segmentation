import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

np.random.seed(42)
random.seed(42)

n_customers = 1000
n_orders = 15000

# Customer IDs
customer_ids = [f"CUST{str(i).zfill(4)}" for i in range(1, n_customers + 1)]

# Customer demographics
cities = ["Mumbai", "Delhi", "Bangalore", "Hyderabad", "Pune", "Chennai", "Jaipur", "Kolkata", "Ahmedabad", "Surat"]
segments_true = np.random.choice(["Champions", "Loyal", "At Risk", "Hibernating", "New"], 
                                  size=n_customers, p=[0.10, 0.20, 0.15, 0.25, 0.30])

# Date range: Jan 2022 to Dec 2023
start_date = datetime(2022, 1, 1)
end_date = datetime(2023, 12, 31)
date_range = (end_date - start_date).days

orders = []
for i, cust in enumerate(customer_ids):
    seg = segments_true[i]
    if seg == "Champions":
        n = np.random.randint(20, 50)
        avg_spend = np.random.uniform(800, 3000)
        recency_days = np.random.randint(1, 30)
    elif seg == "Loyal":
        n = np.random.randint(10, 25)
        avg_spend = np.random.uniform(400, 1200)
        recency_days = np.random.randint(15, 60)
    elif seg == "At Risk":
        n = np.random.randint(5, 15)
        avg_spend = np.random.uniform(300, 900)
        recency_days = np.random.randint(90, 200)
    elif seg == "Hibernating":
        n = np.random.randint(1, 6)
        avg_spend = np.random.uniform(100, 400)
        recency_days = np.random.randint(200, 365)
    else:  # New
        n = np.random.randint(1, 4)
        avg_spend = np.random.uniform(200, 600)
        recency_days = np.random.randint(1, 45)

    last_order_date = end_date - timedelta(days=recency_days)
    for j in range(n):
        offset = random.randint(0, (last_order_date - start_date).days)
        order_date = start_date + timedelta(days=offset)
        amount = max(50, np.random.normal(avg_spend, avg_spend * 0.3))
        product_cat = np.random.choice(
            ["Electronics", "Clothing", "Home & Kitchen", "Books", "Beauty", "Sports"],
            p=[0.25, 0.22, 0.20, 0.13, 0.12, 0.08]
        )
        orders.append({
            "order_id": f"ORD{str(len(orders)+1).zfill(6)}",
            "customer_id": cust,
            "order_date": order_date.strftime("%Y-%m-%d"),
            "amount": round(amount, 2),
            "product_category": product_cat,
            "city": np.random.choice(cities),
            "payment_method": np.random.choice(["UPI", "Credit Card", "Debit Card", "NetBanking", "COD"],
                                                p=[0.35, 0.25, 0.20, 0.10, 0.10])
        })

df = pd.DataFrame(orders)
df = df.sample(frac=1, random_state=42).reset_index(drop=True)
df.to_csv("/home/claude/projects/project1_customer_segmentation/ecommerce_orders.csv", index=False)
print(f"Dataset created: {len(df)} orders, {n_customers} customers")
print(df.head())
