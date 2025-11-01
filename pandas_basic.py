import pandas as pd
# df = pd.read_excel("Project-Management-Sample-Data.xlsx",)#pd.read_ iske bahut tarah ke data add kr sakte h " " ke undr cd daaldo
# df = pd.read_csv(" ") for .csv
# df = pd.read_json(" ") for .json


# #KUD KA DATASET KAISE BANAI 
data = {
    "name" : ["shanib","gogi","pinku","chotu","gabru","fawda"],
    "age" : [109,34,56,78,5,77],
    "city" : ["delhi","mp","mumbai","goa","pune","raj"]

}
df = pd.DataFrame(data)##pd.{DateFrame}(apne data variable ka naam)
print(df)#bus simpli abb terminal me data print ho jaiga=55

# #data ko kisi dusre extension me krne ke liye  aur index ko remove krne ke liya index = true
# df.to_csv("data")
# df.to_excel("data.xlsx", index=False)  ##extension likna bhi must h {data.xlxs}
# # df.to_json("data.json",index=False)##kisi bhi extension me kr skate h
# df.to_html("data.html")                                                                                                                   