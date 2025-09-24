import streamlit as st
from camera import VideoCamera
from detection import detect_faces_and_eyes

st.title("Face and Eye Detection App")

camera = None

start = st.button("Start Video")
stop = st.button("Stop Video")

stframe = st.empty()

if start:
    if camera is None:
        camera = VideoCamera()
    while True:
        frame = camera.get_frame()
        if frame is None:
            st.warning("No frame captured from the camera.")
            break
        img = detect_faces_and_eyes(frame)
        stframe.image(img, channels="BGR")

if stop and camera is not None:
    camera.release()