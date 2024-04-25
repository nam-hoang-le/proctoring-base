from cvzone.FaceDetectionModule import FaceDetector
import cv2

cap = cv2.VideoCapture(0)

# Initialize the FaceDetector object
detector = FaceDetector()

# Run the loop to continually get frames from the webcam
while True:
    # Read the current frame from the webcam
    # success: Boolean, whether the frame was successfully grabbed
    # img: the captured frame
    success, img = cap.read()

    # Detect faces in the image
    # img: Updated image
    # bboxs: List of bounding boxes around detected faces
    img, bboxs = detector.findFaces(img, draw=False)

    # Check if any face is detected
    if bboxs:
        # ---- Get Data  ---- #
        center = bboxs[0]["center"]

        # ---- Draw Data  ---- #
        cv2.circle(img, center, 5, (255, 0, 255), cv2.FILLED)

    # Display the image in a window named 'Image'
    cv2.imshow("Image", img)
    # Wait for 1 millisecond, and keep the window open
    key = cv2.waitKey(1) # Esc key
    if key == 27:
        break

