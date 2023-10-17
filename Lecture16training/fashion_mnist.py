from keras import layers, models
from keras.datasets import fashion_mnist
from keras.models import Sequential
from keras.utils import to_categorical
import matplotlib.pyplot as plt

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

print(train_images.shape)
print(train_labels.shape)

train_images = train_images.astype('float32') / 255.0
test_images = test_images.astype('float32') / 255.0

# train_images = train_images.reshape((60000, 28, 28, 1)).astype('float32') / 255.0
# test_images = test_images.reshape((10000, 28, 28, 1)).astype('float32') / 255.0

train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels) 
# test_labels = to_categorical(test_labels) or loss='sparse_categorical_crossentropy'

model = Sequential()
model.add(layers.Flatten(input_shape=(train_images.shape[1],train_images.shape[2])))
model.add(layers.Dense(128, activation='relu', kernel_regularizer=L1(0.001)))
model.add(layers.Dropout(0.2))
model.add(layers.Dense(10, activation='softmax'))

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
modelVal = model.fit(train_images, train_labels, epochs=10, batch_size=128, validation_split=0.2)

acc = modelVal.history['accuracy']
val_acc = modelVal.history['val_accuracy']


plt.plot( acc, label='Training accuracy')
plt.plot( val_acc, label='Validation accuracy')
plt.title('Training and Validation Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()

plt.show()






