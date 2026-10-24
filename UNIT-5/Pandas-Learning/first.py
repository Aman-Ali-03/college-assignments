# Example of Group by 
import numpy as np
import pandas as pd

# Enterprise Sales Dataset
sales_data = {
    "Region": ["East", "East", "West", "West", "East", "West"],
    "Manager": ["Alice", "Alice", "Bob", "Bob", "Charlie", "Charlie"],
    "Sales": [200, 150, 300, 400, 250, 500],
    "Profit": [40, 30, 70, 90, 50, 110],
}
df_sales = pd.DataFrame(sales_data)

# Multi-column GroupBy with custom aggregate metrics
grouped = df_sales.groupby("Region").agg(
    Total_Sales=("Sales", "sum"),
    Average_Profit=("Profit", "mean"),
    Max_Sale=("Sales", "max"),
)
print("=== GroupBy Summary ===")
print(grouped)