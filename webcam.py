import cv2
import numpy as np
import dlib
from collections import OrderedDict
from eye_aspect_ratio import eye_aspect_ratio

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

FACIAL_LANDMARKS_68_IDXS = OrderedDict([
	("mouth", (48, 68)),
	("right_eyebrow", (17, 22)),
	("left_eyebrow", (22, 27)),
	("right_eye", (36, 42)),
	("left_eye", (42, 48)),
	("nose", (27, 36)),
	("jaw", (0, 17))
])
  
def draw_points(image, points):
  for i, (x, y) in enumerate(points):
    cv2.circle(image, (x, y), 5, (0, 0, 255), -1)

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
      ls, le = FACIAL_LANDMARKS_68_IDXS['left_eye']
      rs, re = FACIAL_LANDMARKS_68_IDXS['right_eye']
      left_eye = shape[ls:le]
      right_eye = shape[rs:re]
      draw_points(frame, left_eye)
      draw_points(frame, right_eye)
      print("left eye: " + eye_aspect_ratio(left_eye))
      print("right eye: " + eye_aspect_ratio(right_eye))

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
      break
  
vid.release()
cv2.destroyAllWindows()
