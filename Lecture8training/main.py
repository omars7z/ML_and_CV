import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('diabetes.csv')

print(df.head())
print(df.shape)

print(df[:5])
print(df[-5:])

df_mean = df.mean()
df_median = df.median()
print(df_mean)
print(df_median)

bmi = df['BMI']
def bmi_idx(bmi):
    if bmi < 18:
        return 'Underweight'
    elif 18.5 <= bmi <= 24.9:
        return 'Normal weight'
    elif 25.0 <= bmi <= 29.9:
        return 'Overweight'
    else:
        return 'Obesity'

df['BMI_Category'] = df['BMI'].apply(bmi_idx)
print(df['BMI_Category'])

df_copy = df.to_csv('diabetes_copy.csv', index=False)
df2 = pd.read_csv('diabetes_copy.csv')
print(df2.head())
# print(df.to_csv('diabetes_copy.csv', index=False))

