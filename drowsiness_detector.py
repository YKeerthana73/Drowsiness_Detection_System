import cv2
import dlib
import pyttsx3
from scipy.spatial import distance

# Text-to-speech engine
engine = pyttsx3.init()

# Initialize camera
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Failed to open webcam")
else:
    print("Webcam opened successfully")

  # Use 1 if you have an external webcam

# Load face detector and landmark predictor
face_detector = dlib.get_frontal_face_detector()
landmark_predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# Function to calculate eye aspect ratio
def eye_aspect_ratio(eye):
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])
    ear = (A + B) / (2.0 * C)
    return ear

# Main loop
while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_detector(gray)

    for face in faces:
        landmarks = landmark_predictor(gray, face)

        left_eye = []
        right_eye = []

        for n in range(36, 42):  # Left eye
            x, y = landmarks.part(n).x, landmarks.part(n).y
            left_eye.append((x, y))
            next_point = 36 if n == 41 else n + 1
            x2, y2 = landmarks.part(next_point).x, landmarks.part(next_point).y
            cv2.line(frame, (x, y), (x2, y2), (255, 255, 0), 1)

        for n in range(42, 48):  # Right eye
            x, y = landmarks.part(n).x, landmarks.part(n).y
            right_eye.append((x, y))
            next_point = 42 if n == 47 else n + 1
            x2, y2 = landmarks.part(next_point).x, landmarks.part(next_point).y
            cv2.line(frame, (x, y), (x2, y2), (0, 255, 0), 1)

        left_ear = eye_aspect_ratio(left_eye)
        right_ear = eye_aspect_ratio(right_eye)
        avg_ear = (left_ear + right_ear) / 2.0
        avg_ear = round(avg_ear, 2)

        # Drowsiness threshold
        if avg_ear < 0.25:
            cv2.putText(frame, "DROWSINESS DETECTED", (50, 100),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
            engine.say("Alert! Wake up!")
            engine.runAndWait()

    cv2.imshow("Drowsiness Detector", frame)

    key = cv2.waitKey(1)
    if key == 27:  # ESC key
        break

cap.release()
cv2.destroyAllWindows()
