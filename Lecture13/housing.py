import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split

df = pd.read_csv('housing.csv')
scalar = MinMaxScaler()
num = scalar.fit_transform(df)

df.DataFrame(data=num, columns=df.columns)

x = df[['RM'], ['LSTAT'], ['PTRATIO']]
y = df[['MEDV']]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.15)

model = Sequential([
    Dense(20, input_shape=(3, ), activation='relu'),
    Dense(10, activation='relu'),
    Dense(5, activation='relu'),
    Dense(1, activation='linear')
])

model.compile(optimizer='adam', loss='MSE', metrics=['accuracy'])
#loss='MSE' because regression not classification
model.fit(x_train, y_train, epochs=200)