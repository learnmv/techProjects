import cv2
import numpy as np
from typing import Optional, Tuple, List

def load_cascades() -> Tuple[cv2.CascadeClassifier, cv2.CascadeClassifier]:
    face_cascade = cv2.CascadeClassifier('src/models/haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('src/models/haarcascade_eye.xml')
    return face_cascade, eye_cascade

def detect_faces_and_eyes(frame: np.ndarray,
                          face_cascade: Optional[cv2.CascadeClassifier] = None,
                          eye_cascade: Optional[cv2.CascadeClassifier] = None) -> np.ndarray:
    """Detect faces and eyes and draw rectangles on the frame, returning the annotated image."""
    if face_cascade is None or eye_cascade is None:
        face_cascade, eye_cascade = load_cascades()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(frame, (x + ex, y + ey), (x + ex + ew, y + ey + eh), (0, 255, 0), 2)

    return frame