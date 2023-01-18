import pandas as pd
df=pd.read_csv("students details.csv",usecols=["Roll No","Name","Class"])
print(df)
'''spc=df[["Name","Phone Number"]]
print("The column is:")
print(spc)
print(df.head())'''