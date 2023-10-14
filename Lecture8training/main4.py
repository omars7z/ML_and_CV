# import keras
import matplotlib.pyplot as plt
from keras.datasets import mnist
from sklearn.preprocessing import OneHotEncoder
from keras.utils import to_categorical
import numpy as np
import tensorflow.python

# (x_train, y_train), (x_test, y_test) = keras.datasets.minst.load_data()
(x_train, y_train), (x_test, y_test) = mnist.load_data()

newfig = plt.figure(figsize=(5, 5))
for i in range(newfig):
    r = np.random.randint(0, 50)
    plt.subplot(5, 5, i+1)
    plt.imshow(x_train[r])
plt.show()

for i in range(25):
    r = np.random.random_integers(0, x_train.shape[0]-1)
    plt.subplot(5, 5, i+1)
    plt.axis('off')
    plt.imshow(x_train[r], cmap='gray')

plt.show()


# enc = OneHotEncoder()
# enc.fit_transform()

y = to_categorical(y_train)
print(y)
ptint(y[:5])