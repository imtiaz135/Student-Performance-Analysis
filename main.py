import pandas as pd
import matplotlib.pyplot as plt
import os
df = pd.read_csv("data/sales_datas.csv")
df["Date"] = pd.to_datetime(df["Date"])
df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
df["Price"] = pd.to_numeric(df["Price"], errors="coerce")
df["Total_Sales"] = pd.to_numeric(df["Total_Sales"], errors="coerce")
df.fillna({
    "Quantity": df["Quantity"].mean(),
    "Price": df["Price"].mean(),
    "Total_Sales": df["Total_Sales"].mean()
}, inplace=True)

df["Month"] = df["Date"].dt.month
monthly_sales = df.groupby("Month")["Total_Sales"].sum()
product_sales = df.groupby("Product")["Total_Sales"].sum()
region_sales = df.groupby("Region")["Total_Sales"].sum()
os.makedirs("visualizations", exist_ok=True)

# Chart 1: Monthly Sales Trend
plt.figure()
monthly_sales.plot(marker='o')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("visualizations/monthly_sales.png")
plt.close()

# Chart 2: Top 5 Products
plt.figure()
product_sales.sort_values(ascending=False).head(5).plot(kind='bar')
plt.title("Top 5 Products by Sales")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("visualizations/top_products.png")
plt.close()

# Chart 3: Regional Sales
plt.figure()
region_sales.plot(kind='bar')
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("visualizations/region_sales.png")
plt.close()

print("Analysis completed. Charts saved in visualizations folder.")
