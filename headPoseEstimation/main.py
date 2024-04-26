import cv2
import mediapipe as mp
from headPoseEstimation import headPoseEstimation
# ================================
font = cv2.FONT_HERSHEY_PLAIN
# ================================

# ---------------- Take the face mesh  and draw it--------------------
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils
drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)

# ------------ Choose the camera -------------------
cap = cv2.VideoCapture(0)

# -------------------- Loop the program ----------------------------
while True:
    # ---------------- Read the frame from the camera -----------------
    _, frame = cap.read()

    # ------------------- Flip it ------------------------------
    frame = cv2.flip(frame, 1)

    # -------------------- Change the frame to RGB -------------------
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # --------------------- To improve performance --------------------
    img.flags.writeable = False  # writeable only moving to the ML models, display image on it

    # --------------------- Get the face mesh of the image -------------
    results = face_mesh.process(img)

    # --------------------- To improve performance --------------------
    img.flags.writeable = True

    # --------------------- Change it back to BGR -----------------------
    img = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    # --------------------- Take the shape of the image -----------------
    ih, iw, ic = img.shape

    # --------------------- Create 2D and 3D list -----------------------
    face_3d = []
    face_2d = []

    # ---------- If there is a detection -----------
    if results.multi_face_landmarks:
        # ----------- Go through all face landmarks detected --------------
        for face_landmarks in results.multi_face_landmarks:
            # ------------------ Get the index and landmark values in every face landmarks -----------------
            x, y, face_2d, face_3d = headPoseEstimation(face_landmarks, face_2d, face_3d, iw, ih)

            # -------------------------- See where the user's head tilting -----------------------
            if x > 15 or x < -15 or y > 15 or y < -15:
                text = "Out screen"
            else:
                text = "On screen"

            # ---------------- Add the text on the frame -------------------
            cv2.putText(frame, text, (20, 50), font, 2, (0, 255, 0), 2)

    # ------------------- Show the image -----------------
    cv2.imshow("Image", frame)

    # ------------- Breaking when entering ESC key -------------
    key = cv2.waitKey(1)
    if key == 27:
        break

# -------------- Exit ------------------
cv2.destroyAllWindows()
cap.release()