import cv2
import numpy as np
import dlib
from eyeBlinking.eye_blinking import get_blinking_ratio
from eyeGazing.eye_gazing import get_hor_gaze_ratio, get_ver_gaze_ratio

cap = cv2.VideoCapture(0)

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("face_landmarks.dat")

font = cv2.FONT_HERSHEY_PLAIN

while True:
    _, frame = cap.read()
    # flip the camera
    frame = cv2.flip(frame, 1)
    new_frame = np.zeros((500, 500, 3), np.uint8)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = detector(gray)
    for face in faces:
        #x, y = face.left(), face.top()
        #x1, y1 = face.right(), face.bottom()
        #cv2.rectangle(frame, (x, y), (x1, y1), (0, 255, 0), 2)

        landmarks = predictor(gray, face)

        # Detect blinking
        left_eye_ratio = get_blinking_ratio([36, 37, 38, 39, 40, 41], landmarks)
        right_eye_ratio = get_blinking_ratio([42, 43, 44, 45, 46, 47], landmarks)
        blinking_ratio = (left_eye_ratio + right_eye_ratio) / 2

        if blinking_ratio > 5.7:
            cv2.putText(frame, "BLINKING", (50, 150), font, 7, (255, 0, 0))

        left_eyes_points = [36, 37, 38, 39, 40, 41]
        right_eyes_points = [42, 43, 44, 45, 46, 47]

		# Gaze detection
        hor_gaze_ratio_left_eye = get_hor_gaze_ratio(left_eyes_points, landmarks, frame, gray)
        hor_gaze_ratio_right_eye = get_hor_gaze_ratio(right_eyes_points, landmarks, frame, gray)
        hor_gaze_ratio = (hor_gaze_ratio_left_eye + hor_gaze_ratio_right_eye) / 2
        print(hor_gaze_ratio)


        # if gaze_ratio <= 0.6:
        #     cv2.putText(frame, "LEFT", (50, 100), font, 2, (0, 0, 255), 3)
        #     new_frame[:] = (0, 0, 255)  
        # elif 0.6 < gaze_ratio < 1.4:
        #     cv2.putText(frame, "CENTER", (50, 100), font, 2, (0, 0, 255), 3)
        # else:
        #     new_frame[:] = (255, 0, 0)
        #     cv2.putText(frame, "RIGHT", (50, 100), font, 2, (0, 0, 255), 3)

        # Gaze detection
        ver_gaze_ratio_left_eye = get_ver_gaze_ratio(left_eyes_points, landmarks, frame, gray)
        ver_gaze_ratio_right_eye = get_ver_gaze_ratio(right_eyes_points, landmarks, frame, gray)
        ver_gaze_ratio = (ver_gaze_ratio_left_eye + ver_gaze_ratio_right_eye) / 2
        print(ver_gaze_ratio)


        if  0.6 < hor_gaze_ratio < 1.3:
            cv2.putText(frame, "ON SCREEN", (50, 100), font, 2, (0, 0, 255), 3)
        else:
            cv2.putText(frame, "OUT SCREEN", (50, 100), font, 2, (0, 0, 255), 3)


        # if  0.4 < ver_gaze_ratio < 1.1:
        #     cv2.putText(frame, "ON SCREEN", (50, 100), font, 2, (0, 0, 255), 3)
        # else:
        #     cv2.putText(frame, "OUT SCREEN", (50, 100), font, 2, (0, 0, 255), 3)




    cv2.imshow("Frame", frame)


    key = cv2.waitKey(0)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()