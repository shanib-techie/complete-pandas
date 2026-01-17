"""
PROBLEM -> how much column & row 
PROBLEM -> what type of ?
PROBLEM -> MISSINg data

info()
method

1->no. of row& coloum
2->coloum name
3->type?
4->non null 

"""
import pandas as pd

# data = {
#      "name" : ["shanib","gogi","pinku","chotu","gabru","fawda"],
#      "age" : [19,34,56,78,5,77],
#      "class" : [12,11,6,2,11,7],
#      "city" : ["delhi","mp","mumbai","goa","pune","raj"]
# }

# df = pd.DataFrame(data)
df = pd.read_excel("Project-Management-Sample-Data.xlsx")
print(df)
print("\n only jisme sab kuch h")
# df.dropna(inplace=True)
# df.fillna(0,inplace=True)
# print(df)
df["Unnamed: 1"].fillna("game",inplace=True)
print(df)




# print("DATA infomation")
# print(df.info())



# print("some statistic thing :  \n")
# print (df.describe())# numeric ka samaan return krta h



# print("shape : return M X N : ")
# print(df.shape)

# print("total no of coloum : ")
# print(df.columns)