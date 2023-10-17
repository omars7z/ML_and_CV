from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense,Flatten
from keras.metrics import F1Score
from sklearn.metrics import ConfusionMatrixDisplay, accuracy_score, precision_score, recall_score, f1_score
import numpy as np

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

print(train_images.shape)
print(train_labels.shape)

model = Sequential()
model.add(Flatten(input_shape=(train_images.shape[1],train_images.shape[2])))
model.add(Dense(128, activation='relu'))
model.add(Dense(10, activation='softmax'))

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
modelVal = model.fit(train_images, train_labels, epochs=1, batch_size=128, validation_split=0.2)

y_predict = model.predict(test_images)

y_pre_arg = np.argmax(y_predict,axis=1)
# print(y_pre_arg[0])
y_true_arg =  np.argmax(test_labels.reshape(-1,1),axis=1)
# print(y_true_arg[0])

#precision_recall_fscore_support( y_predict, y_true, average='macro')

y_accuracy = accuracy_score( y_true_arg,y_pre_arg)
y_precision = precision_score(y_true_arg,y_pre_arg, average='weighted')
y_recall = recall_score(y_true_arg,y_pre_arg, average='weighted')
y_f1 = f1_score(y_true_arg,y_pre_arg, average='weighted')

model.evaluate(y_true_arg, y_pre_arg)

y_confusion = ConfusionMatrixDisplay(y_true_arg, y_pre_arg)

print(y_accuracy)
print(y_precision)
print(y_recall)
print(y_f1)

print(y_confusion)
# model.F1Score(
#     average=None, threshold=None, name='f1_score', dtype=None
# )
 