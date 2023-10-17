import cv2
import numpy as np

image = cv2.imread('pic.webp', cv2.IMREAD_GRAYSCALE)

sobel_x = cv2.Sobel(image, 1, 1, 0, ksize=3)
sobel_y = cv2.Sobel(image, 1, 0, 1, ksize=3)
sobel_final = np.abs(sobel_x) + np.abs(sobel_y)

cv2.imshow('image', image)
cv2.imshow('filtered_image', sobel_final)

cv2.waitKey(0)
cv2.destroyWindow()