"""
df["column name"].mean()
df["columnname"].sum()
df["column name"].max()"""

import pandas as pd

data = {
    "name" : ["shanib","gogi","pinku","chotu","gabru","fawda","bona","haroon","gaawar"],
    "age" : [109,34,56,78,5,77,24,67,65],
    "salary" : [20000,30000,50000,10000,45000,35000,10000,75000,80000],
    "city" : ["delhi","mp","mumbai","goa","pune","raj","goa","mp","chennai"]
}

df = pd.DataFrame(data)
max_salary = df["salary"].max()
print(max_salary)
max_row = df[df["salary"] == max_salary]
print(max_row)
