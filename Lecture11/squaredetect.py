import cv2

image = cv2.imread('pic.webp')

classifier = cv2.CascadeClassifier('haarcascade_eye.xml')
faces = classifier.detectMultiScale(image)

for(x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 255), thickness=2)

cv2.imshow('face_1', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

