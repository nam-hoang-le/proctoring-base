import cv2
import pytesseract
import time
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

# ---------------- Store all the words ----------------
fullText = []

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
            fullText.append(text)

# ------------------------ Set the file names ----------------------------
timeNow = time.time()
timeNow = str(timeNow).split('.')
timeNow = timeNow[0] + timeNow[1]

# -------------------- Write it into different files -----------------
with open(f"information/{timeNow}.txt", 'a', encoding='utf-8') as f:
    for text in fullText:
        f.writelines(text + ' ')
