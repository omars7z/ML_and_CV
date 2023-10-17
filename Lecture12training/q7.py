import cv2

eye_classifier = cv2.CascadeClassifier('haarcascade_eye.xml')
face_classifier = cv2.CascadeClassifier('haarcascade-frontalface-default.xml')


cam = cv2.VideoCapture(0)

while True:
    _, frame = cam.read()
    faces = face_classifier.detectMultiScale(frame)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x +w , y+h),(255,255,0),3)
    eye = eye_classifier.detectMultiScale(frame)
    for(x, y, w, h) in eye:
        cv2.circle(frame, (x, y),30,(255,0,255),3)
    cv2.imshow('image', frame)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()