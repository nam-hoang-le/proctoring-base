import cv2
import numpy as np
import dlib
from eye_gazing import get_ver_gaze_ratio


# =================================================
MOUTH_AR_THRESH = 0.7
font = cv2.FONT_HERSHEY_PLAIN
left_eye_points = [36, 37, 38, 39, 40, 41]
right_eye_points = [42, 43, 44, 45, 46, 47]
lower_thres = 0.5
# =================================================

# ------------------ Get the face detector -------------------
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("face_landmarks.dat")

# ---------------------- Choose the webcam ---------------------------
cap = cv2.VideoCapture(0)

# -------------------- Loop the program ----------------------------
while True:
    # ---------------- Read the frame from the camera -----------------
    _, frame = cap.read()

    # ------------------- Flip it ------------------------------
    frame = cv2.flip(frame, 1)

    # ------------------- Change to gray frame ---------------------
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # -------------------- Detect the gray face ----------------
    faces = detector(gray)

    # ------------------- Loop the faces -----------------
    for face in faces:

        # ------------------- Get the landmarks ----------------------------
        landmarks = predictor(gray, face)

        # ---------------------- Get the vertical gaze ratio ----------------------
        left_ver_gaze_ratio = get_ver_gaze_ratio(
            left_eye_points, landmarks, frame, gray
        )
        right_ver_gaze_ratio = get_ver_gaze_ratio(
            right_eye_points, landmarks, frame, gray
        )
        ver_gaze_ratio = (left_ver_gaze_ratio + right_ver_gaze_ratio) / 2
        print(ver_gaze_ratio)

        # ----------------------- Compare the vertical gaze ratio -------------------------
        if  lower_thres < ver_gaze_ratio:
            cv2.putText(frame, "ON SCREEN", (50, 100), font, 2, (0, 0, 255), 3)
        else:
            cv2.putText(frame, "OUT SCREEN", (50, 100), font, 2, (0, 0, 255), 3)

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(0)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()

        
        

