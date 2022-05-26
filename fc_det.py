import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier(r'C:\Users\hiyak\Downloads\haarcascade_frontalface_default.xml')

image = cv2.imread(r'C:\Users\hiyak\Downloads\yukta.jpeg')
grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(grey, 1.3, 5)

if faces == ():
    print("No Face here!")
else:
    print("found Hiya!")