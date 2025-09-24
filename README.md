# Face and Eye Detection Streamlit Application

This project is a Streamlit web application that implements face and eye detection using OpenCV. It captures video from the webcam and processes each frame to detect faces and eyes in real-time.

## Project Structure

```
face-eye-streamlit-app
├── src
│   ├── streamlit_app.py        # Main entry point for the Streamlit application
│   ├── detection.py            # Contains face and eye detection logic
│   ├── camera.py               # Manages camera input and video capture
│   ├── utils.py                # Utility functions for image processing
│   └── models
│       ├── haarcascade_frontalface_default.xml  # Haar cascade model for face detection
│       └── haarcascade_eye.xml  # Haar cascade model for eye detection
├── requirements.txt            # Python dependencies for the project
├── .gitignore                  # Files and directories to ignore by Git
├── .streamlit
│   └── config.toml            # Configuration settings for the Streamlit application
├── Dockerfile                  # Instructions to build a Docker image for the application
├── Procfile                    # Command to run the Streamlit application on deployment platforms
└── README.md                   # Documentation for the project
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd face-eye-streamlit-app
   ```

2. **Install dependencies:**
   It is recommended to create a virtual environment before installing the dependencies.
   ```
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```
   streamlit run src/streamlit_app.py
   ```

## Usage

- Once the application is running, it will open in your default web browser.
- Allow access to your webcam when prompted.
- The application will display the video feed with rectangles drawn around detected faces and eyes.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.