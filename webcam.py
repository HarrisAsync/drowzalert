import cv2

# define a video capture object
vid = cv2.VideoCapture(1)
# create an instance of the Face Detection Cascade Classifier
detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
# Detect faces using the haarcascade classifier on the "grayscale image"
# create an instance of the cv2.sdFacial landmark Detector with the model
landmark_detector  = cv2.face.createFacemarkLBF()
landmark_detector.loadModel("lbfmodel.yaml")

  
while(True):
  ret, frame = vid.read()
  if ret:
    image_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(image_gray)
    # _, landmarks = landmark_detector.fit(image_gray, faces)
    for face in faces:
  #     save the coordinates in x, y, w, d variables
      (x,y,w,d) = face
      # Draw a white coloured rectangle around each face using the face's coordinates
      # on the "image_template" with the thickness of 2 
      cv2.rectangle(image_gray,(x,y),(x+w, y+d),(255, 255, 255), 2)
    cv2.imshow('frame', image_gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break
  
vid.release()
cv2.destroyAllWindows()
