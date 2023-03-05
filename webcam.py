import cv2
import numpy as np
import dlib
from collections import OrderedDict
from eye_aspect_ratio import eye_aspect_ratio
import threading
from sound import Sound_Alerts

FPATH = "pretrain/haarcascade_frontalface_default.xml"
EPATH = "pretrain/haarcascade_eye.xml"
LBFPATH = "pretrain/lbfmodel.yaml"
DLIBPATH = "pretrain/shape_predictor_68_face_landmarks.dat"

FACIAL_LANDMARKS_68_IDXS = OrderedDict([
	("mouth", (48, 68)),
	("right_eyebrow", (17, 22)),
	("left_eyebrow", (22, 27)),
	("right_eye", (36, 42)),
	("left_eye", (42, 48)),
	("nose", (27, 36)),
	("jaw", (0, 17))
])
  
ls, le = FACIAL_LANDMARKS_68_IDXS['left_eye']
rs, re = FACIAL_LANDMARKS_68_IDXS['right_eye']
ms, me = FACIAL_LANDMARKS_68_IDXS['mouth']

# sound = AudioSegment.from_file("dunDun.wav")

def draw_points(image, points):
  for i, (x, y) in enumerate(points):
    cv2.circle(image, (x, y), 2, (0, 0, 255), -1)


TEMPERATURE = 5

if __name__ == "__main__":
  vid = cv2.VideoCapture(1)
  # create an instance of the Face Detection Cascade Classifier
  face_detector = cv2.CascadeClassifier(FPATH)
  landmark_detector = dlib.get_frontal_face_detector()
  landmark_predictor = dlib.shape_predictor(DLIBPATH)
  ss = Sound_Alerts()
  x = threading.Thread(target=lambda: ss.input(1))

  while(True):
    ret, frame = vid.read()
    if ret:
      frame = cv2.resize(frame, (854, 480), fx=0,fy=0, interpolation = cv2.INTER_CUBIC)
      image_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
      faces = landmark_detector(image_gray, 1)
      for f in faces:
        shape = landmark_predictor(image_gray, f)
        shape_np = np.zeros((68, 2), dtype="int")
        for i in range(0, 68):
          shape_np[i] = (shape.part(i).x, shape.part(i).y)
        shape = shape_np
        left_eye = shape[ls:le]
        right_eye = shape[rs:re]
        draw_points(frame, left_eye)
        draw_points(frame, right_eye)
        ler, rer = eye_aspect_ratio(left_eye), eye_aspect_ratio(right_eye)

        if ler < 0.20 and rer < 0.20:
          TEMPERATURE -= 1
        else: 
          TEMPERATURE = 5 

        if TEMPERATURE < 0:
          if not x.is_alive():
            ### Execute block
            x = threading.Thread(target=lambda: ss.input(1))
            x.start()
            ### Execute block

      cv2.imshow('frame', frame)

      if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
  vid.release()
  cv2.destroyAllWindows()
