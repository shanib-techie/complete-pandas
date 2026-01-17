"""sorting data 
SORTING DATA  1 COLUMN sort_value()
df.sort_value(by="column_name",True/false,inplace = true )"""


import pandas as pd

data = {
    "name" : ["shanib","gogi","pinku","chotu","gabru","fawda","bona","haroon","gaawar"],
    "age" : [109,34,56,77,77,77,24,65,65],
       ## # "age" : [109,34,56,77,77,77,24,65,65],##example for multiple value sorting ke liye banai ha
    "salary" : [20000,30000,50000,10000,45000,35000,10000,75000,80000],
    "city" : ["delhi","mp","mumbai","goa","pune","raj","goa","mp","chennai"]
}


df = pd.DataFrame(data)
# df.sort_values(by = "salary" , ascending=True,inplace=True)#one column pass
# df.sort_values(by=["age","salary"],ascending=[True,False],inplace=True)  ##yeh tab kaam ayga jab age bahut logo ki same ho k
print("data is sorting by salary ")
print(df)