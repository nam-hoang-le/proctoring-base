import cv2
import pytesseract
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

# -------------------- Write it into different files -----------------
with open("data/text.txt", 'a', encoding='utf-8') as f:
    f.writelines(text)