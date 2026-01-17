"""
1-> square braket
2-> boolean condtions



selecting coloums
1-> a series ; sirf ek coloum print krna h
2-> dataframe multiple coloumn"""

"""filtering row
 based on single condition
 filtered_row = df[df["salary"] > 5000].
 
combine multiple condition
filterd_row = df[(df["column"] > val) & (df["coloum2"] <val2)]
""" 


# coloum = df["column name"] #for single coloumn
# subset = df["column1","column2","column3"......"coloumn_n"]

import pandas as pd
data = {
    "name" : ["shanib","gogi","pinku","chotu","gabru","fawda"],
    "age" : [109,34,56,78,5,77],
    "salary" : [3000,400,220,100,40,100],
    "city" : ["delhi","mp","mumbai","goa","pune","raj"]

}
df =pd.DataFrame(data)

print(df)

"""  PRINT SOME SUBSET """  ##simply [["coloumn name"]]
print("return only name")
# names = df[["name"]]
# print(names)


# print("name & age & salary")

combine = df[["name","age","salary"]]
print(combine)  




""" CONDITIONAL STATEMENT"""
#  select those salary > 100

# sts = df[df["salary"]>100]
# print(sts)


# select those salary > 100 or age <75

stsa = df[(df["salary"]> 100) &  (df["age"] <75)]
print(stsa)
