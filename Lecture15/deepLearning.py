from keras.datasets import mnist
import matplotlib.pyplot as plt

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

print(train_images.shape) #60k * 28 *28
print(train_labels.shape) #60k
print(test_images.shape)
print(test_labels.shape)

sample_image = train_images[:25]
sample_title = train_labels[:25]

plt.figure(10, 10)
for i in range(25):
    plt.subplot(5, 5, i+1)
    plt.imshow(sample_image[i], cmap='gray')
    plt.title(sample_title[i])
    plt.axis('off')

plt.show()