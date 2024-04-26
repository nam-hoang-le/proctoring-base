import cv2
import pytesseract
# =============================
font = cv2.FONT_HERSHEY_PLAIN
# =============================

# --------------- Call tesseract.exe --------------------
pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

# ---------------- Read the image -------------------
img = cv2.imread("test/1.1.JPG")

# --------------- Change the image to BGR format -------------
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# ---------------- Use pytesseract library to take information from the image ----------------
boxes = pytesseract.image_to_data(img)

# ------------------ Run through every line in the information -------------------------
for idx, line in enumerate(boxes.splitlines()):
    # ------------------------ Remove the first line ---------------------
    if idx != 0:
        # ------------------ Split information from every line --------------------------
        info = line.split()
        # -------------------- If line has words ------------------------
        if len(info) == 12:
            # ------------------- Take the information ------------------------
            x, y, w, h, text = int(info[6]), int(info[7]), int(info[8]), int(info[9]), info[11]

            # ----------------------- Draw a rectangle and text ----------------------
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.putText(img, text, (x, y), font, 1, (255, 0, 0), 2)

# ---------------------- Show the image ----------------------
cv2.imshow("Frame", img)
# ---------------------- Close the window ----------------
key = cv2.waitKey(0)
if key == 27:
    cv2.destroyAllWindows()
