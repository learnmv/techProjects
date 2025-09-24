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

# Show WebRTC status and helpful debug information
try:
    if webrtc_ctx and hasattr(webrtc_ctx, 'state'):
        if webrtc_ctx.state.playing:
            st.success("Camera streaming: browser permission granted and video is playing.")
        else:
            st.info("Camera not streaming. Click the Start button in the video component.")
            st.write("If nothing happens: check your browser's camera permission, open the browser console for errors, and check the app's deployment logs for installation errors (PyAV/ffmpeg).")
    else:
        st.warning("WebRTC context not initialized. The app may be running in fallback mode or streamlit-webrtc failed to import.")
except Exception as e:
    st.error(f"Error checking WebRTC status: {e}")