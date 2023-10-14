import pandas as pd

df = pd.read_csv("diabetes.csv")

print(df.iloc[1, 1])
df.iloc[2, 4] = None
df.iloc[1, 0] = None
df.iloc[0, 6] = None
# df.iloc[1, 2] = -6
df.iloc[5, 0] = -22
df.info()
df.isna()

print(df["Glucose"].head())
df2 = pd.DataFrame(df)
df2["Glucose"] = df2["Glucose"].fillna(-55)
df2 = df2.fillna(-88)
print(df2["Glucose"].head(10))