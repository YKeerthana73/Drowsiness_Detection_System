# 💤 Drowsiness Detection System

This project is a real-time drowsiness detection system using computer vision. It monitors a person’s eye activity via webcam and raises alerts if signs of drowsiness (like prolonged eye closure) are detected. This can help prevent accidents caused by fatigue, especially in driving scenarios.

---

## ✅ Features

- Real-time face and eye detection using Dlib and OpenCV
- Calculates Eye Aspect Ratio (EAR) to detect eye closure
- Displays a visual alert on screen
- Triggers an audio alert to wake up the user

---

## 🛠️ Requirements

Install the following Python libraries before running the project:

```bash
pip install opencv-python dlib pyttsx3 scipy
```
## 📥 Download the `.dat` Model File

To use this project, you must download and set up the required Dlib model:

### Step 1: Download the file
```bash
curl -O http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2
```
### 📥 Step 2: Extract the file

Use the following command to extract the `.bz2` file:

```bash
bzip2 -d shape_predictor_68_face_landmarks.dat.bz2
```
### 📁 Step 3: Move the `.dat` file to your project folder

Make sure it’s placed in the same directory as your Python script (`drowsiness_detector.py`):

```bash
mv shape_predictor_68_face_landmarks.dat ./Drowsiness_Detection_System/
```
This .dat file is essential for detecting facial landmarks such as eye positions for drowsiness detection.

## Run the Drowsiness Detection Script

To start the system, simply run the Python script:

```bash
python drowsiness_detector.py
```
## Test the system
When you run the script, the system will use your webcam to detect face landmarks and track eye movement. If drowsiness (i.e., prolonged eye closure) is detected, the system will display an alert on screen and play an audio alert.
