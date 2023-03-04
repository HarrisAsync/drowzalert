import cv2
import numpy as np
import dlib

FPATH = "pretrain/haarcascade_frontalface_default.xml"
EPATH = "pretrain/haarcascade_eye.xml"
LBFPATH = "pretrain/lbfmodel.yaml"
DLIBPATH = "pretrain/shape_predictor_68_face_landmarks.dat"
# define a video capture object
vid = cv2.VideoCapture(1)
# create an instance of the Face Detection Cascade Classifier
face_detector = cv2.CascadeClassifier(FPATH)
# eye_detector = cv2.CascadeClassifier(EPATH)
# landmark_detector = cv2.face.createFacemarkLBF()
# landmark_detector.loadModel("lbfmodel.yaml")
landmark_detector = dlib.get_frontal_face_detector()
landmark_predictor = dlib.shape_predictor(DLIBPATH)

  
while(True):
  ret, frame = vid.read()
  if ret:
    image_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = landmark_detector(image_gray, 1)
    for f in faces:
      shape = landmark_predictor(image_gray, f)
      shape_np = np.zeros((68, 2), dtype="int")
      print(shape_np)
      for i in range(0, 68):
        shape_np[i] = (shape.part(i).x, shape.part(i).y)
      shape = shape_np
      for i, (x, y) in enumerate(shape):
        cv2.circle(frame, (x, y), 5, (0, 0, 255), -1)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
      break
  
vid.release()
cv2.destroyAllWindows()
