from time import time
import cv2
import cvzone
from cvzone.FaceDetectionModule import FaceDetector
####################################
classID = 0  # 0 is fake and 1 is real
outputFolderPath = 'dataset/all'
confidence = 0.8
save = True
blurThreshold = 35  # Larger is more focus
debug = False
offsetPercentageW = 10
offsetPercentageH = 20
camWidth, camHeight = 640, 480
floatingPoint = 6
####################################

# ------------- Take the cap from the camera, set the frame size ------------
cap = cv2.VideoCapture(0)
cap.set(0, camWidth)
cap.set(0, camHeight)

# -------------- Detect the face from the cvzone --------------------------
detector = FaceDetector()

while True:
    success, img = cap.read()
    # ------------------- Flip it ------------------------------
    img = cv2.flip(img, 1)

    # ------------------- Copy other image --------------------------
    imgOut = img.copy()

    # ------------------- Find info of the face --------------------------
    img, bboxs = detector.findFaces(img, draw=False)

    listBlur = []  # True False values indicating if the faces are blur or not
    listInfo = []  # The normalized values and the class name for the label txt file

    # ----------------------- If there is face ----------------------------
    if bboxs:
        # ----------------------- Loop through all the boxes ----------------
        for bbox in bboxs:
            # --------------------- Take the information out ------------------------
            x, y, w, h = bbox["bbox"]
            score = bbox["score"][0]

            # ------  Check the score --------
            if score > confidence:

                # ------  Adding an offset to the face Detected --------
                offsetW = (offsetPercentageW / 100) * w
                x = int(x - offsetW)
                w = int(w + offsetW * 2)
                offsetH = (offsetPercentageH / 100) * h
                y = int(y - offsetH * 3)
                h = int(h + offsetH * 3.5)

                # ------  To avoid values below 0 --------
                x = max(x, 0)
                y = max(y, 0)
                w = max(w, 0)
                h = max(h, 0)

                # ------  Find Blurriness --------
                imgFace = img[y:y + h, x:x + w]
                cv2.imshow("Face", imgFace)
                blurValue = int(cv2.Laplacian(imgFace, cv2.CV_64F).var())
                if blurValue > blurThreshold:
                    listBlur.append(True)
                else:
                    listBlur.append(False)

                # ------  Normalize Values  --------
                ih, iw, _ = img.shape
                xc, yc = x + w / 2, y + h / 2

                xcn, ycn = round(xc / iw, floatingPoint), round(yc / ih, floatingPoint)
                wn, hn = round(w / iw, floatingPoint), round(h / ih, floatingPoint)

                # ------  To avoid values above 1 --------
                xcn = min(1, xcn)
                ycn = min(1, ycn)
                wn = min(1, wn)
                hn = min(1, hn)

                listInfo.append(f"{classID} {xcn} {ycn} {wn} {hn}\n")

                # ------  Drawing --------
                cv2.rectangle(imgOut, (x, y, w, h), (255, 0, 0), 3)
                cvzone.putTextRect(imgOut, f'Score: {int(score * 100)}% Blur: {blurValue}', (x, y - 0),
                                   scale=2, thickness=3)
                # ------------- For debugging -----------------------
                if debug:
                    cv2.rectangle(img, (x, y, w, h), (255, 0, 0), 3)
                    cvzone.putTextRect(img, f'Score: {int(score * 100)}% Blur: {blurValue}', (x, y - 0),
                                       scale=2, thickness=3)

        # ------  To Save --------
        if save:
            if all(listBlur) and listBlur != []:
                # ------  Save Image  --------
                timeNow = time()
                timeNow = str(timeNow).split('.')
                timeNow = timeNow[0] + timeNow[1]
                cv2.imwrite(f"{outputFolderPath}/{timeNow}.jpg", img)
                # ------  Save Label Text File  --------
                for info in listInfo:
                    f = open(f"{outputFolderPath}/{timeNow}.txt", 'a')
                    f.write(info)
                    f.close()

    # ---------------- Show the image -------------------------
    cv2.imshow("Image", imgOut)

    # ----------------- Break out ---------------------
    key = cv2.waitKey(27)
    if key == 27: 
        break