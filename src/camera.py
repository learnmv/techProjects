import cv2

class VideoCamera:
    def __init__(self, device_index: int = 0):
        self.video_capture = cv2.VideoCapture(device_index)

    def release(self):
        try:
            if hasattr(self, 'video_capture') and self.video_capture.isOpened():
                self.video_capture.release()
        except Exception:
            pass

    def __del__(self):
        self.release()

    def get_frame(self):
        if not hasattr(self, 'video_capture'):
            return None
        ret, frame = self.video_capture.read()
        if not ret:
            return None
        return frame