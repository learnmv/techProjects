import cv2
import numpy as np

def load_cascades():
    face_cascade = cv2.CascadeClassifier('src/models/haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('src/models/haarcascade_eye.xml')
    return face_cascade, eye_cascade

def detect_faces_and_eyes(frame, face_cascade, eye_cascade):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray)

    detections = []
    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)

        detections.append({
            'face': (x, y, w, h),
            'eyes': [(ex, ey, ew, eh) for (ex, ey, ew, eh) in eyes]
        })

    return detections