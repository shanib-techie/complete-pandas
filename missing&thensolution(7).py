"""
NaN (not a number )
none (for object data type)
isnull()
true -> missing value
false-> exist hai"""

import pandas as pd


data = {
    "name" : ["shanib","gogi","pinku","chotu","gabru","fawda","bona","haroon","gaawar"],
    "age" : [109,34,56,78,5,77,24,67,65],
    "salary" : [20000,30000,50000,10000,45000,35000,10000,75000,80000],
    "city" : ["delhi","mp","mumbai","goa","pune","raj","goa","mp","chennai"]
}

data_with_miss = {
     "name" : ["shanib","gogi","pinku",None,"gabru","fawda","bona","haroon",None],
    "age" : [109,34,56,None,5,77,24,67,None],
    "salary" : [20000,None,50000,10000,45000,None,10000,75000,None],
    "city" : ["delhi","mp",None,"goa","pune",None,"goa","mp","chennai"]

}

df = pd.DataFrame(data_with_miss)

print(df.isnull()) #return in bool jo none h waha true 
print(df.isnull().sum()) #return how much data are missing in each column


"""NOW, WE STUDY DIFFERENT WAY TO DEAL WITH THIS TYPE OF PROBLEM"""
# df.dropna(inplace = True)
# df.dropna(inplace= True)#aise krne se woh data print hoa jiski koi bhi val missing ni h

# df.fillna(0,inplace= True)#agr starting me 0 krde so missing ki jagah 0 hoga
# df["salary"].fillna(df["salary"].mean(),inplace=True)  ## abb hamne salary wale me .fiilna krke mean kr diya
# df["age"].fillna(df["salary"].mean(),inplace=True)  ##deko mene age me salary.mean kr diya

print(df)



"""ANOTHER WAY TO DEAL WITH MISSING NUMBER  INTERPPOL"""
# 10->20->30->40->   ->60->   

""" NOW BY USING DIFFERENT METHOD WE FILL THE FOLLOWING MISSING VALUE """


dt = { "val" : [1,2,3,None,None,6,7,8,None]}
df = pd.DataFrame(dt)
print("before interpolate",df)
# linear,polymonial,time
df["val"] = df["val"].interpolate(method="linear")
print("after inter",df)






