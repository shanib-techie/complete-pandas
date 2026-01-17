"""pd.merge(df1,df2, on = "column_name",how = "type of join")"""





import pandas as pd

emp = pd.DataFrame({
    "emp_id": [1, 2, 3, 4],
    "name": ["Amit", "Ravi", "Sneha", "Tina"]
})

salary = pd.DataFrame({
    "emp_id": [2, 3, 4, 5],
    "salary": [50000, 60000, 70000, 55000]
})

merged = pd.merge(emp, salary, on="emp_id")
print(merged)




"""🔹 2. how parameter — join type decide karta hai

Tu how= likh ke bata sakta hai kis type ka join chahiye:

Join Type	Code	Description
Inner Join	how='inner'	Sirf matching keys wale rows
Left Join	how='left'	Left DataFrame ke sab rows + matching right rows
Right Join	how='right'	Right DataFrame ke sab rows + matching left rows
Outer Join	how='outer'	Dono ke sab rows, non-matching me NaN"""