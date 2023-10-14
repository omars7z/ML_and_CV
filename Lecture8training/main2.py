import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import Normalizer
from sklearn import preprocessing


import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('diabetes.csv')

dfbl = df[['BloodPressure']]
minmax = MinMaxScaler()
scaled = minmax.fit_transform(dfbl)
print(scaled)
plt.hist(dfbl)
plt.xlabel("X-axis")
plt.ylabel("y-axis")
plt.title('BloodPressure')
plt.show()
plt.xlabel("X-axis")
plt.ylabel("y-axis")
plt.title('BloodPressure MinMax')
plt.hist(scaled)
plt.show()

# dfbmi = df['BMI'].to_numpy().reshape(-1,1)
dfbmi = df[['BMI']]
# print(dfbmi.shape)
regscaler = StandardScaler()
scaled2 = regscaler.fit_transform(dfbmi)
print(scaled2)
plt.hist(dfbmi)
plt.xlabel("X-axis")
plt.ylabel("y-axis")
plt.title('BMI')
plt.show()
plt.xlabel("X-axis")
plt.ylabel("y-axis")
plt.title('BMI Standarad')
plt.hist(scaled2)
plt.show()
'''
dfage = df[['Age']]
scaled3 = Normalizer()
scaled = scaled3.fit_transform(dfage)
print(scaled)
'''

