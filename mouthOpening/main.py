# import the necessary packages
from mouthOpening import mouthAspectRatio
from imutils import face_utils
import numpy as np
import dlib
import cv2

# =================================================
MOUTH_AR_THRESH = 0.7
font = cv2.FONT_HERSHEY_PLAIN
(mStart, mEnd) = (49, 68)
# =================================================


# ------------------ Get the face detector -------------------
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("data/faceLandmarks.dat")

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

        # --------------- Take the mouth points -----------------
        shape = predictor(gray, face)
        shape = face_utils.shape_to_np(shape)
        mouth_points = shape[mStart:mEnd]

        # --------------- Take the mouth ratio --------------------
        mouth_ratio = mouthAspectRatio(mouth_points)
        
        
        # ----------------- Draw text if mouth is open --------------------
        if mouth_ratio > MOUTH_AR_THRESH:
            cv2.putText(frame, "OPEN!", (50, 150), font, 10, (0, 0, 255))

    # ------------------- Show the frame -------------------------
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == 27:  # Esc key
        break


cv2.destroyAllWindows()
cap.release()
