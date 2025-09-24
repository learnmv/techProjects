import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase, RTCConfiguration
import av
import cv2
import numpy as np
from detection import detect_faces_and_eyes

st.title("Face and Eye Detection App")

# Optional: set ST app to use a custom TURN/STUN server if needed for deployment
RTC_CONFIGURATION = RTCConfiguration(
    {
        "iceServers": [
            {"urls": ["stun:stun.l.google.com:19302"]}
        ]
    }
)


class FaceEyeTransformer(VideoTransformerBase):
    def __init__(self):
        self.frame_skip = 0

    def transform(self, frame: av.VideoFrame) -> av.VideoFrame:
        img = frame.to_ndarray(format="bgr24")
        # process frame with detection (returns annotated image)
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