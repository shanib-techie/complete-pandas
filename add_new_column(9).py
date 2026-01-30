import pandas as pd

data = {
    "name" : ["shanib","gogi","pinku","chotu","gabru","fawda","bona","haroon","gaawar"],
    "age" : [109,34,56,78,5,77,24,67,65],
    "salary" : [20000,30000,50000,10000,45000,35000,10000,75000,80000],
    "city" : ["delhi","mp","mumbai","goa","pune","raj","goa","mp","chennai"]
}
df = pd.DataFrame(data)



#  ADD NEW COLUMN


#   iss tarike se increment bhi kr sakte h perticular column me
df["salary"] = df["salary"]+1500
df["bonus"] = df["salary"]*0.1
df["current income"] = df["salary"] + df["bonus"]
# print(df)

# print("print_only_name_current_income. : ")
# print_only_name_current_income = df[["name","current income"]]### kuch selected data print krna h 
# print(print_only_name_current_income)

#USE AND FIND WHERE INCOME > 55000

# print("\nDATA WHERE AGE > 100 OR INCOM > 50000\n")
where = df[(df["current income"] > 50000) | (df["age"] > 100)]
print("bonus & age 5000 , 100")
selc = df[(df["bonus"] > 5000) | (df["age"] > 100 )]
print(selc)

print(where)




""" ANOTHER FUNCTION THAT ABLE TO ADD NEW COLOUMN WHICH IS insert(loc,"column_name",some_data)"""
# iske faide kisi bhi index pr jakr coloum add kr sakte h
# df.insert(4,"address",["karol bagh","bhopat","andheri","punin","vikas marg","kota","beach","mandir wali gali","thirupati"])
# df.insert(0,"UNIQUE_id",[239,240,241,242,243,244,245,246,247])
# print(df)

"""column me kisi perticular value ko change krna h  df.loc[row_index,"column_name"] = new_value"""
# df.loc[0,"age"] = 19
# print("ABB MERI AGE CHANGE HO GYI NORMAL WALI\n")
# print(df)





""" COLOUMN DROP KRNE KE LIYE BHI HOTA H"""
# df.drop(columns=["UNIQUE_id"],inplace = True)
# df.drop(columns= ["bonus"], inplace = True)

print(df)