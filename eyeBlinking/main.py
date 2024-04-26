import cv2
import numpy as np
import dlib
from eyeBlinking import getBlinkingRatio
# ===================================
font = cv2.FONT_HERSHEY_PLAIN
leftEyePoints = [36, 37, 38, 39, 40, 41]
rightEyePoints = [42, 43, 44, 45, 46, 47]
blinkThreshold = 5.7
# ===================================

# ------------ Choose the camera -------------------
cap = cv2.VideoCapture(0)

# ------------------ Get the face detector -------------------
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("data/faceLandmarks.dat")

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

        # ------------------- Get the blinking ratio ---------------------
        left_eye_ratio = getBlinkingRatio(leftEyePoints, landmarks)
        right_eye_ratio = getBlinkingRatio(rightEyePoints, landmarks)
        blinking_ratio = (left_eye_ratio + right_eye_ratio) / 2

        # -------------------------- Compare the result to the threshold -------------------
        if blinking_ratio > blinkThreshold:
            cv2.putText(frame, "BLINKING", (50, 150), font, 7, (255, 0, 0))

    # ------------------- Show the image -----------------
    cv2.imshow("Frame", frame)
    # ------------- Breaking when entering ESC key -------------
    key = cv2.waitKey(1)
    if key == 27:
        break

# -------------- Exit ------------------
cap.release()
cv2.destroyAllWindows()