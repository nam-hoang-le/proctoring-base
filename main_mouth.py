# import the necessary packages
from src.features.mouth_opening import mouth_aspect_ratio
from imutils import face_utils
import numpy as np
import dlib
import cv2


# define one constants, for mouth aspect ratio to indicate open mouth
MOUTH_AR_THRESH = 0.74

# initialize dlib's face detector (HOG-based) and then create
# the facial landmark predictor

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("face_landmarks.dat")

# grab the indexes of the facial landmarks for the mouth
(mStart, mEnd) = (49, 68)

cap = cv2.VideoCapture(0)  # choose the webcam


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
        # determine the facial landmarks for the face region, then 
        # convert the facial landmark (x, y)-coordinates to a NumPy 
        # array 
        
        shape = predictor(gray, face)
        shape = face_utils.shape_to_np(shape)
        
        # extract the mouth coordinates, then use the 
        # coordinates to compute the mouth aspect ratio 
        mouth_points = shape[mStart:mEnd]
        
        mouth_ratio = mouth_aspect_ratio(mouth_points)
        mar = mouth_ratio
        
        # compute the convex hull for the mouth, then 
        # visualize the mouth 
        mouthHull = cv2.convexHull(mouth_points)
        # cv2.drawContours(frame, [mouthHull], -1, (0, 255, 0), 1)
        # cv2.putText(frame, "MAR: {:.2f}".format(mar), (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        
        # Draw text if mouth is open
        if mar > MOUTH_AR_THRESH: 
            cv2.putText(frame, "OPEN!", (50, 150), font, 10, (0, 0, 255))

    
    # show the frame 
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == 27: # Esc key 
        break 

        
    
# do a bit of cleanup
cv2.destroyAllWindows()	
cap.release()

