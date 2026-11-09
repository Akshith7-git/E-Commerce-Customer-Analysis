
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

print("E-Commerce Customer Analysis Started!")

# Project directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Output directory
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load CSV dataset
CSV_PATH = os.path.join(BASE_DIR, "ecommerce_customer_analysis_cleaned.csv")

df = pd.read_csv(CSV_PATH)

print("\n========== DATASET OVERVIEW ==========")

print("\nFirst 5 Records:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Information:")
df.info()

print("\nStatistical Summary:")
print(df.describe())

print("\n========== DATA QUALITY ==========")

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Records:")
print(df.duplicated().sum())

print("\nUnique Customers:")
print(df["Customer_ID"].nunique())

print("\nUnique Products:")
print(df["Product_Name"].nunique())

print("\n========== BUSINESS INSIGHTS ==========")

print("\nTotal Revenue:")
print(df["Total_Amount_INR"].sum())

print("\nTotal Orders:")
print(df["Order_ID"].nunique())

print("\nTotal Customers:")
print(df["Customer_ID"].nunique())

print("\nAverage Order Value:")
print(df["Total_Amount_INR"].mean())

print("\nTop 10 Customers:")
top_customers = (
    df.groupby("Customer_ID")["Total_Amount_INR"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)
print(top_customers)

print("\nBest Selling Products:")
best_products = (
    df.groupby("Product_Name")["Quantity"]
    .sum()
    .sort_values(ascending=False)
)
print(best_products)

print("\nSales by Category:")
category_sales = df.groupby("Category")["Total_Amount_INR"].sum()
print(category_sales)

print("\n========== VISUALIZATION ==========")

sns.set_theme(style="whitegrid")

# Category Sales Chart
plt.figure(figsize=(9, 5))
category_sales.sort_values(ascending=False).plot(kind="bar")
plt.title("Sales by Product Category")
plt.xlabel("Category")
plt.ylabel("Revenue (INR)")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "category_sales.png"))
plt.show()

# Monthly Sales Trend
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

monthly_sales = (
    df.groupby(df["Order_Date"].dt.month)["Total_Amount_INR"]
    .sum()
)

plt.figure(figsize=(9, 5))
monthly_sales.plot(kind="line", marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Revenue (INR)")
plt.xticks(range(1, 13))
plt.grid()
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "monthly_sales.png"))
plt.show()

# Customer Spending Distribution
customer_spending = (
    df.groupby("Customer_ID")["Total_Amount_INR"].sum()
)

plt.figure(figsize=(9, 5))
sns.histplot(customer_spending, bins=20, kde=True)
plt.title("Customer Spending Distribution")
plt.xlabel("Total Spending (INR)")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "customer_spending.png"))
plt.show()

# Save Business Insights Report
with open(os.path.join(OUTPUT_DIR, "business_insights.txt"), "w") as file:

    file.write("E-COMMERCE CUSTOMER ANALYSIS\n\n")

    file.write(f"Total Revenue: {df['Total_Amount_INR'].sum():.2f}\n")
    file.write(f"Total Orders: {df['Order_ID'].nunique()}\n")
    file.write(f"Total Customers: {df['Customer_ID'].nunique()}\n")
    file.write(f"Average Order Value: {df['Total_Amount_INR'].mean():.2f}\n")

    file.write("\nTOP 10 CUSTOMERS:\n")
    file.write(top_customers.to_string())

    file.write("\n\nBEST SELLING PRODUCTS:\n")
    file.write(best_products.to_string())

    file.write("\n\nSALES BY CATEGORY:\n")
    file.write(category_sales.to_string())

print("\n========== PROJECT COMPLETED ==========")
print("All analysis completed successfully!")
print("Charts and business insights saved inside outputs folder.")
