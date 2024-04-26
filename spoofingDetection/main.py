import math
import time
import cv2
import cvzone
from ultralytics import YOLO

# =================================
confidence = 0.6
classNames = ["fake", "real"]

# =================================

# --------------------- Choose the webcam and set the size ----------------------------
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

# --------------------- Choose model to run -----------------------
model = YOLO("../models/yolov8Train.pt")


while True:
    # --------------- Take the info and flip the cam ------------------
    success, img = cap.read()
    img = cv2.flip(img, 1)
    # ----------------- Take the result from model ----------------------
    results = model(img, stream=True, verbose=False)
    # ------------------ Loop through all the program -----------------
    for result in results:
        boxes = result.boxes
        # ---------------------- Loop through all the boxes ------------------
        for box in boxes:
            # -------------------- Take info of the bounding Box -------------------
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            w, h = x2 - x1, y2 - y1
            # ----------------- Confidence ------------------
            conf = math.ceil((box.conf[0] * 100)) / 100
            # ---------------------- Class Name -------------------------
            cls = int(box.cls[0])
            # --------------------- Find the threshold --------------------
            if conf > confidence:
                if classNames[cls] == 'real':
                    color = (0, 255, 0)
                else:
                    color = (0, 0, 255)
                # --------------------- Drawing --------------------
                cvzone.cornerRect(img, (x1, y1, w, h),colorC=color,colorR=color)
                cvzone.putTextRect(img, f'{classNames[cls].upper()} {int(conf*100)}%',
                                   (max(0, x1), max(35, y1)), scale=2, thickness=4,colorR=color,
                                   colorB=color)

    # --------------------- Show the image -------------
    cv2.imshow("Image", img)
    key = cv2.waitKey(1)

    # ----------------------- Break the loop ------------------
    if key == 27:
        break