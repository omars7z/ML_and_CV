# import cv2
# import numpy as np
#
# lena = cv2.imread('len_std.webp')
# m = np.zeros(shape=(lena.shape[0], lena.shape[1]), )

import cv2
import numpy as np

# Load the colored image
original_image = cv2.imread('len_std.webp')  # Replace 'your_image.jpg' with your image file path

# original_image=np.resize(original_image,new_shape=(512,512,3))
height, width, channels = original_image.shape

blank_image = np.ones((height, width, 3), np.uint8) * 255  # White background

circle_mask = np.zeros((height, width), dtype=np.uint8)
circle_center = (width // 2, height // 2)
circle_radius = min(width, height) // 2
cv2.circle(circle_mask, circle_center, circle_radius, (255, 255, 255), -1)

result_image = cv2.bitwise_and(original_image, original_image, mask=circle_mask)

cv2.imshow('Image Inside Circle', result_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
