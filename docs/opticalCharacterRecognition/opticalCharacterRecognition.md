# Optical Character Recognition 

## Problem 

We need to recognize the ID card of the candidates at the first of every tests. My suggested idea is we need to first recognize the ID card, checking whether it is at the correct format, then extract the information using OCR (Optical Character Recognition). 

For recognizing the ID card, it's hard for me to have my own dataset with multiple challenges like private information, difference in ID format between countries, etc. So, I just made the OCR parts to extract the information from the images. 

I have two versions, one is lighter using pytesseract library, one is heavier using additional packages. The first version supports only English, the second version supports to 100 languages. So depending on your problem and your implementation, we can choose the right version. 

Note that I also stored the zip file of the tesseract library in the **opticalCharacterRecognition** folder.

## Solution 

Extract words from image, then store it in the folder. 

## How-to-do

**Step 1:** 
I call the library, take information from them 

**Step 2:** 

I stored the information in the *information* folder with file name is the current time exchange. 



