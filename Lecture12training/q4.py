import cv2
import numpy as np

back_image = cv2.imread('Nine_of_Hearts.webp')
sym_image = cv2.imread('hearts.png')

# Resize sym_image to 50x50 pixels
sym_image = cv2.resize(sym_image, (200, 200))

gray = cv2.cvtColor(back_image, cv2.COLOR_BGR2GRAY)

# Convert sym_image to the same data type and depth as gray
sym_image = cv2.cvtColor(sym_image, cv2.COLOR_BGR2GRAY)

w = sym_image.shape[0]
h = sym_image.shape[1]
print(w)
res = cv2.matchTemplate(gray, sym_image, cv2.TM_CCOEFF_NORMED)

threshold = 0.44

loc = np.where(res >= threshold)

# Draw a rectangle around the matched region.
for pt in zip(*loc[::-1]):
    cv2.rectangle(back_image, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)

# Show the final image with the matched area.
cv2.imshow('Detected', back_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
