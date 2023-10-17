import cv2
import numpy as np

filter = np.array([
    [1, 0, -1],
    [2, 0, -2],
    [1, 0, -1]
])
filter2 = np.array([
    [1, 0, -1],
    [2, 0, -2],
    [1, 0, -1]
])

#or cv2.laplasian()
laplasian = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0],
])


image = cv2.imread('chess_bord.png')
filtered_image2 = cv2.filter2D(image, -1, filter)
filtered_image1 = cv2.filter2D(image, -1, filter2)

print(filtered_image1.max(), filtered_image1.min())
final_image = np.abs(filtered_image1) + np.abs(filtered_image2)
# final_image = filtered_image1 + filtered_image2

cv2.imshow('image', image)
cv2.imshow('filtered_image', final_image)

cv2.waitKey(0)
cv2.destroyWindow()