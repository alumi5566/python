import pandas as pd

seriese_1 = pd.Series([11,22,33,44], index = ["name", "num1", "num2", "num3"])
# print(seriese_1)
# name    11
# num1    22
# num2    33
# num3    44
# dtype: int64
# print(seriese_1.iloc[0])
# print(seriese_1.iloc[1:3])
# 11
# num1    22
# num2    33
# dtype: int64

data = {
    'name': ["Peter", "John", "Cindy", "CY"],
    "email": ["p@gmail.com", "j@gmail.com", "c@gmail.com", "cy@gmail.com"],
    "grades": [100, 60, 77, 10]
}
df = pd.DataFrame(data)
print(df)
# name        email  grades
# 0  Peter  p@gmail.com     100
# 1   John  j@gmail.com      60
# 2  Cindy  c@gmail.com      77
df = pd.DataFrame(data, index=['one', 'two','three', "four"])
print(df)
#         name        email  grades
# one    Peter  p@gmail.com     100
# two     John  j@gmail.com      60
# three  Cindy  c@gmail.com      77

# print(df.index)
# print(df.columns)
# Index(['one', 'two', 'three', 'four'], dtype='object')
# Index(['name', 'email', 'grades'], dtype='object')

# df.to_csv("csv01.csv")
# df.to_json("json01.json")

# print(df.head(2))
# name        email  grades
# one  Peter  p@gmail.com     100
# two   John  j@gmail.com      60

# print(df.drop(["grades"], axis=1))
# print(df.drop(["two"], axis=0))
# name         email
# one    Peter   p@gmail.com
# two     John   j@gmail.com
# three  Cindy   c@gmail.com
# four      CY  cy@gmail.com
# name         email  grades
# one    Peter   p@gmail.com     100
# three  Cindy   c@gmail.com      77
# four      CY  cy@gmail.com      10

df_na = pd.read_csv("csv01_na.csv")
print(df_na)
print(df_na.fillna("Missing Value"))
# Unnamed: 0   name        email  grades
# 0           1  Peter  p@gmail.com     100
# 1           2   John          NaN      60
# 2           3  Cindy  c@gmail.com      77
# 3           4     CY          NaN      10
# Unnamed: 0   name          email  grades
# 0           1  Peter    p@gmail.com     100
# 1           2   John  Missing Value      60
# 2           3  Cindy    c@gmail.com      77
# 3           4     CY  Missing Value      10
print(df_na.index)
print(df_na.columns)
print("CY")
print(df_na["name"])
print(df_na["name"][1])