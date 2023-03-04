import cv2
import numpy as np

FPATH = "haarcascade_frontalface_default.xml"
EPATH = "haarcascade_eye.xml"
LBFPATH = "lbfmodel.yaml"
# define a video capture object
vid = cv2.VideoCapture(1)
# create an instance of the Face Detection Cascade Classifier
face_detector = cv2.CascadeClassifier(FPATH)
eye_detector = cv2.CascadeClassifier(EPATH)
# landmark_detector  = cv2.face.createFacemarkLBF()
# landmark_detector.loadModel("lbfmodel.yaml")

  
while(True):
  ret, frame = vid.read()
  # frame += np.random.randint(low=0, high=63, size=frame.shape).astype(np.uint8) % 255
  if ret:
    image_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(image_gray)
    for face in faces:
      (x,y,w,d) = face
      # cv2.rectangle(image_gray,(x,y),(x+w, y+d),(255, 255, 255), 2)
      roi_gray = image_gray[y:y+d, x:x+w]
      roi_color = frame[y:y+d, x:x+w]
      eyes = eye_detector.detectMultiScale(roi_gray, 1.2, 6)

      if len(eyes) > 2:
        eyes = eyes[:2]

      for (ex,ey,ew,ed) in eyes:
          cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+ed),(0,255,0),2)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break
  
vid.release()
cv2.destroyAllWindows()
