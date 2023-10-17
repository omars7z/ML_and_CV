# import cv2
# import numpy as np
# img_rgb = cv2.imread('mario_large_image.jpeg')
# img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
# template = cv2.imread('temp.png', cv2.IMREAD_GRAYSCALE)
# w, h = template.shape[::-1]
# res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
# threshold = 0.8
# loc = np.where( res >= threshold)
# for pt in zip(*loc[::-1]):
#  cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
# cv2.imshow('res.png',img_rgb)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



import cv2
import numpy as np
img_rgb = cv2.imread('mario_large_image.jpeg')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('temp.png',cv2.IMREAD_GRAYSCALE )
w ,h = template.shape[::-1]
res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where(res >= threshold)
for pt in zip(*loc[::-1]):
	cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)

cv2.imshow('Detected', img_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()