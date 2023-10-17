import pandas as pd
from sklearn.model_selection import train_test_split
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

df = pd.read_csv('iris.csv')

# Input and output
y = df[["variety"]]
x = df.drop(columns=["variety"])
y = pd.get_dummies(y, dtype=int)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, shuffle=True, random_state=12)

# Build model
model = Sequential()
model.add(Dense(6, input_shape=(x_train.shape[1],), activation='sigmoid'))
model.add(Dense(4, activation='relu'))
model.add(Dense(3, activation='softmax'))  # 3 units for the 3 classes

# Optimizer, loss function
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Start training, epochs for repeating better processing
model.fit(x_train, y_train, epochs=100)

y_predict = model.predict(x_test)
