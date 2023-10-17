import cv2
import numpy as np

image = cv2.imread('len_std.webp')

cv2.imshow('Original Image', image)

Gaussian = cv2.GaussianBlur(image, (7, 7), 0)
cv2.imshow('Gaussian Blurring', Gaussian)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
median = cv2.medianBlur(gray, 5)
cv2.imshow('Median Blur', median)

equalizer = cv2.equalizeHist(median)
cv2.imshow('Histrogram equalizer', equalizer)

# compare = np.concatenate((image, gray, median, equalizer), axis=1) #side by side comparison

cv2.waitKey(0)
cv2.destroyAllWindows()