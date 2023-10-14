import pandas as pd

df = pd.read_csv('diabetes.csv')
'''
print(df.shape)
print(df.head())
print(df["age"].describe())
'''
df.info()
print('*************************************')
print(df.head())
print('*************************************')
df2 = df[["Pregnancies", "Age", "Outcome"]]
print(df2.describe())
print('*************************************')

df2["new_age"] = df["Age"] * 2
print(df2["new_age"].head())
print(df2["new_age"].describe())