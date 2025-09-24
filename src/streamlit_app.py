import streamlit as st
import cv2
import numpy as np
from detection import detect_faces_and_eyes

st.title("Face and Eye Detection App")


def try_import_webrtc():
    try:
        from streamlit_webrtc import webrtc_streamer, VideoTransformerBase, RTCConfiguration
        import av
        return webrtc_streamer, VideoTransformerBase, RTCConfiguration, av
    except Exception:
        return None, None, None, None


webrtc_streamer, VideoTransformerBase, RTCConfiguration, av = try_import_webrtc()

if webrtc_streamer is not None:
    # WebRTC path (client browser camera)
    RTC_CONFIGURATION = RTCConfiguration(
        {"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
    )

    class FaceEyeTransformer(VideoTransformerBase):
        def transform(self, frame: av.VideoFrame) -> av.VideoFrame:
            img = frame.to_ndarray(format="bgr24")
            annotated = detect_faces_and_eyes(img)
            return av.VideoFrame.from_ndarray(annotated, format="bgr24")

    webrtc_ctx = webrtc_streamer(
        key="face-eye",
        video_transformer_factory=FaceEyeTransformer,
        rtc_configuration=RTC_CONFIGURATION,
        media_stream_constraints={"video": True, "audio": False},
        async_transform=True,
    )

    st.markdown("Click **Start** in the video component to allow camera access in your browser.")
else:
    # Fallback path: server-side OpenCV capture (works when running locally on machine with camera)
    st.warning(
        "streamlit-webrtc is not available. Running fallback server-side camera capture. "
        "This only works when Streamlit is running on the same machine as the camera."
    )

    start = st.button("Start Local Camera")
    stop = st.button("Stop Local Camera")
    camera = None
    frame_placeholder = st.empty()

    if start:
        camera = cv2.VideoCapture(0)
        if not camera.isOpened():
            st.error("Unable to open local camera. Check camera index or permissions.")
        else:
            while True:
                ret, frame = camera.read()
                if not ret:
                    st.warning("No frame captured from the local camera.")
                    break
                annotated = detect_faces_and_eyes(frame)
                # Streamlit expects RGB for display via st.image; convert BGR->RGB
                frame_placeholder.image(cv2.cvtColor(annotated, cv2.COLOR_BGR2RGB))
                if stop:
                    break
            camera.release()
    if stop and camera is not None:
        try:
            camera.release()
        except Exception:
            pass