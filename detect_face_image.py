import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Read the input image
img = cv2.imread('test2.jpg')
cv2.imshow("",img)
cv2.waitKey()

# Convert into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("",gray)
cv2.waitKey()

# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.1, 4)
print('facedetected=',len(faces))

# Draw rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

# Display the output
cv2.imshow('img', img)
cv2.waitKey()