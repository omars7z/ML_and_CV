# import keras
# import matplotlib.pyplot as plt
# from keras.datasets import mnist
# from sklearn.preprocessing import OneHotEncoder
# from keras.utils import to_categorical
import numpy as np
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler, StandardScaler

df = pd.read_csv('diabetes.csv')
df.dropna()


pipline = Pipeline([
    ("Scaling", MinMaxScaler()),
    ("Scaling 2", StandardScaler())
])

x = df[['x', 'y']]
x = pipline.fit_transform(x)
x = pd.DataFrame(x, columns=['x', 'y'])
print(x.head())

weighs = np.random.rand(2, 1)
bias = np.random.rand(1)

def sigmoid(y):
    return 1 / (1 + np.exp(-y))


for _,i in x.iterrows():
    x = i.to_numpy().reshape(1, 2)
    y = np.dot(x, weighs) + bias
    sigmoid(y)