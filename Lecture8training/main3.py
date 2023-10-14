import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.preprocessing import Normalizer
from sklearn import preprocessing
from sklearn.pipeline import Pipeline

import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('diabetes.csv')

df.dropna()

dfbl = df[['BloodPressure']]
'''minmax = MinMaxScaler()
scaled = minmax.fit_transform(dfbl)
# print(scaled)'''


dfbmi = df[['BMI']]
'''# print(dfbmi.shape)
regscaler = StandardScaler()
scaled2 = regscaler.fit_transform(dfbmi)
# print(scaled2)'''


pipline = Pipeline([
    ("Scaling", MinMaxScaler()),
    ("Scaling 2", StandardScaler())
])
dfblpipline = pipline.fit_transform(dfbl)
dfbmipipline = pipline.fit_transform(dfbmi)
print(dfblpipline)
print('     NEXT        ')
print(dfbmipipline)
