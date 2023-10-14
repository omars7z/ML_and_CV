import matplotlib.pyplot as plt
import matplotlib.image as pltimg
import numpy as np
'''
def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.144])


img_gray = rgb2gray(img_rgb)
plt.imshow(img_gray, cmap=plt.get_cmap('gray'))
plt.savefig('seasidegray.jpg')
#display the black and white image
plt.show()'''

image = pltimg.imread('colors.webp')
def REG2GRAY(image):
     grayscale = np.mean(image, -1)
     plt.imshow(grayscale, cmap='gray')
     plt.show()

REG2GRAY(image)