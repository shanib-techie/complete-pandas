import pandas as pd

# data = {
#     "name" : ["shanib","gogi","pinku","chotu","gabru","fawda"],
#     "age" : [19,34,56,78,5,77],
#     "city" : ["delhi","mp","mumbai","goa","pune","raj"]

# }

# df = pd.DataFrame(data)
df = pd.read_excel("Project-Management-Sample-Data.xlsx")
print(df)

df.to_html("Project-Management-Sample-Data.html")
# print("display 10 first row")##by default 10 hoti h
# print(df.head(3))
# print("last 3")
# print(df.tail(3))