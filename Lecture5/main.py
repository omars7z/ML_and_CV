import pandas as pd

colums = ['A', 'B']
rows = [
    [1, 2],
    [3, 4],
    [5, 6],
]
df = pd.DataFrame(columns=colums, data=rows)
df['A'] = ["1", None, "6"]
# print(df["A"].head())
print('***********************')
# print(df.head())
print(df["A"].head())
print(df.describe())
# print(df.info("A"))
print(df.info)
