import cv2
import numpy as np
import dlib
from src.features.eye_blinking import get_blinking_ratio
from src.features.eye_gazing import get_gaze_ratio

cap = cv2.VideoCapture(0)  # choose the webcam

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("face_landmarks.dat")


font = cv2.FONT_HERSHEY_PLAIN

while True:
    # take the frame from the capture
    _, frame = cap.read()

    # flip the camera
    frame = cv2.flip(frame, 1)
    
    # define the new frame for side looking
    new_frame = np.zeros((500, 500, 3), np.uint8)

    # use the gray frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # detect the face
    faces = detector(gray)

    for face in faces:
        x, y = face.left(), face.top()
        # x1, y1 = face.right(), face.bottom()

        ## draw the rectangle out
        # cv2.rectangle(frame, (x, y), (x1, y1), (0, 255, 0), 2)
        landmarks = predictor(gray, face)

        # both eye landmarks points
        left_eye_points = [36, 37, 38, 39, 40, 41]
        right_eye_points = [42, 43, 44, 45, 46, 47]

        # taking the ratio
        left_eye_ratio = get_blinking_ratio(left_eye_points, landmarks)
        right_eye_ratio = get_blinking_ratio(right_eye_points, landmarks)
        blinking_ratio = (left_eye_ratio + right_eye_ratio) / 2

        if blinking_ratio > 5.7:
            cv2.putText(frame, "BLINK", (50, 150), font, 10, (0, 0, 255))

        # Gaze detection
        gaze_ratio_left_eye = get_gaze_ratio(left_eye_points, landmarks, frame, gray)
        gaze_ratio_right_eye = get_gaze_ratio(right_eye_points, landmarks, frame, gray)
        gaze_ratio = (gaze_ratio_left_eye + gaze_ratio_right_eye) / 2
        

        if 0.7 < gaze_ratio <= 1.5:
            # cv2.putText(frame, "RIGHT", (50, 100), font, 2, (0, 0, 255), 3)
            new_frame[:] = (0, 0, 255)
        # elif 0.5 < gaze_ratio < 1.5:
            # cv2.putText(frame, "CENTER", (50, 100), font, 2, (0, 0, 255), 3)
            # new_frame = new_frame
        else:
            new_frame = new_frame
            # new_frame[:] = (255, 0, 0)
            # cv2.putText(frame, "LEFT", (50, 100), font, 2, (0, 0, 255), 3)
            
        # Showing direction 
        
    # show the camera
    cv2.imshow("Frame", frame)
    cv2.imshow("NewFrame", new_frame)

    key = cv2.waitKey(1)
    if key == 27:  # Esc key
        break

cap.release()
cv2.destroyAllWindows()
