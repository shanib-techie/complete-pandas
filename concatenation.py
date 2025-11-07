import pandas as pd

jan_sales = pd.DataFrame({
    "Month": ["Jan", "Jan"],
    "Product": ["Laptop", "Mouse"],
    "Sales": [50000, 1200]
})

feb_sales = pd.DataFrame({
    "Month": ["Feb", "Feb"],
    "Product": ["Laptop", "Keyboard"],
    "Sales": [60000, 2500]
})

# Concatenate row-wise
all_sales = pd.concat([jan_sales, feb_sales], ignore_index=True)
print(all_sales)











product_info = pd.DataFrame({
    "Product": ["Laptop", "Mouse", "Keyboard"],
    "Category": ["Electronics", "Accessories", "Accessories"]
})

sales_data = pd.DataFrame({
    "Sales_Jan": [50000, 1200, 2500],
    "Sales_Feb": [60000, 1500, 2700]
})

# Column-wise concatenate
merged_data = pd.concat([product_info, sales_data], axis=1)
print(merged_data)











df1 = pd.DataFrame({
    "A": [1, 2],
    "B": [3, 4]
})

df2 = pd.DataFrame({
    "B": [5, 6],
    "C": [7, 8]
})

result = pd.concat([df1, df2], ignore_index=True)
print(result)


"""     A  B    C
0  1.0  3  NaN
1  2.0  4  NaN
2  NaN  5  7.0
3  NaN  6  8.0
"""