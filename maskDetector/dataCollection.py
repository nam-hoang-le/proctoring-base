from time import time

import cv2
import cvzone
from cvzone.FaceDetectionModule import FaceDetector

####################################
outputFolderPath = 'dataset/mask'
save = True
camWidth, camHeight = 640, 480
####################################

# --------- Take the camera -----------
cap = cv2.VideoCapture(0)

# --------------- Set the image ---------------
cap.set(0, camWidth)
cap.set(0, camHeight)

detector = FaceDetector()
while True:
    success, img = cap.read()
    # ------------------- Flip it ------------------------------
    img = cv2.flip(img, 1)
    imgOut = img.copy()

    # ---------  To Save -----------
    if save:
        # ------  Save Image  --------
        timeNow = time()
        timeNow = str(timeNow).split('.')
        timeNow = timeNow[0] + timeNow[1]
        cv2.imwrite(f"{outputFolderPath}/{timeNow}.jpg", img)

    cv2.imshow("Image", imgOut)
    key = cv2.waitKey(27)
    if key == 27:
        break