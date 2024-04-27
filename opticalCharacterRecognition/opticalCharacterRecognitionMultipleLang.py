import cv2
import pytesseract
import time
# =============================
font = cv2.FONT_HERSHEY_PLAIN
# =============================

# --------------- Call tesseract.exe --------------------
pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

# ---------------- Read the image -------------------
img = cv2.imread("test/1.3.JPG")

# --------------- Change the image to BGR format -------------
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# ----------------- Read Vietnamese lang text ----------------
text = pytesseract.image_to_string(img, lang='vie')

# ------------------------ Set the file names ----------------------------
timeNow = time.time()
timeNow = str(timeNow).split('.')
timeNow = timeNow[0] + timeNow[1]

# -------------------- Write it into different files -----------------
with open(f"information/{timeNow}.txt", 'a', encoding='utf-8') as f:
    f.writelines(text)