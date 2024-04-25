import cv2 

# Opencv DNN 
net = cv2.dnn.readNet("models/yolov4-tiny.weights", "models/yolov4-tiny.cfg")

# Create the detection model 
model = cv2.dnn_DetectionModel(net)

# Create Input Parameters
model.setInputParams(size=(320, 320), scale=1/255)

# Load class lists 
classes = []
with open("models/classes.txt", "r") as file_object: 
    for class_name in file_object.readlines(): 
        class_name = class_name.strip()
        classes.append(class_name)

# Initialize the camera
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
# FULL HD 1920 x 1080


while True: 
    # Get frames
    ret, frame = cap.read()
    
    # flip the camera
    frame = cv2.flip(frame, 1)

    # Object Detection 
    (class_ids, scores, bboxes)  = model.detect(frame)
    for class_id, score, bbox in zip(class_ids, scores, bboxes): 
        (x, y, w, h) = bbox
        class_name = classes[class_id]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3)
        cv2.putText(frame, str(class_name), (x, y - 5), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
        
    

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == 27: 
        break

# do a bit of cleanup
cv2.destroyAllWindows()	
cap.release()