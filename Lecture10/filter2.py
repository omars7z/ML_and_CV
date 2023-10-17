import cv2
import numpy as np

filter = np.ones((9, 9))

filter /= np.sum(filter)

#or cv2.laplasian()
laplasian = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0],
])


image = cv2.imread('pic.webp', cv2.IMREAD_GRAYSCALE)
print(image[0:100, 0:100])
filtered_image2 = cv2.filter2D(image, -1, laplasian)
# filtered_image2 = cv2.Laplacian(image, -1, filtered_image2)
print(image[0:100, 0:100])

# filtered_image1 = cv2.filter2D(image, -1, filter)
# print(filtered_image1.shape)

cv2.imshow('image', image)
cv2.imshow('filtered_image', filtered_image2)

cv2.waitKey(0)
cv2.destroyWindow()