import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load data
df = pd.read_csv("sales_data.csv")
print("DATA PREVIEW:")
print(df.head())

# Step 2: Create Revenue column
df["Revenue"] = df["Quantity"] * df["Price"]

# Step 3: Product-wise revenue
product_sales = df.groupby("Product")["Revenue"].sum()
print("\nPRODUCT SALES:")
print(product_sales)

# Step 4: Region-wise revenue
region_sales = df.groupby("Region")["Revenue"].sum()
print("\nREGION SALES:")
print(region_sales)

# Step 5: Visualization
product_sales.plot(kind="bar", title="Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.show()

region_sales.plot(kind="bar", title="Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Revenue")
plt.show()
