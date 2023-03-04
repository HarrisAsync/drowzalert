import cv2
import numpy as np
import dlib
from collections import OrderedDict
from eye_aspect_ratio import eye_aspect_ratio, mouth_aspect_ratio

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

# Point storage 
left_eye_aspect_ratios = []
right_eye_aspect_ratios = []

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

def draw_points(image, points):
  for i, (x, y) in enumerate(points):
    cv2.circle(image, (x, y), 2, (0, 0, 255), -1)

# left_save = []
# right_save = []

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
      mouth = shape[ms:me]
      draw_points(frame, left_eye)
      draw_points(frame, right_eye)
      # draw_points(frame, mouth)
      ler, rer = eye_aspect_ratio(left_eye), eye_aspect_ratio(right_eye)
      if ler < 0.2 and rer < 0.2:
        print("Sleepy")
      else: print("Good")
      # left_save.append(ler)
      # right_save.append(rer)

      # print(f"left eye: {}")
      # print(f"right eye: {}")
      # print(f"mouth: {mouth_aspect_ratio(mouth)}")

      # Check if we are empty
      if len(left_eye_aspect_ratios) >= 3 and len(right_eye_aspect_ratios) >= 3:
        left_eye_aspect_ratios.pop(0)
        right_eye_aspect_ratios.pop(0)
      # Push aspect ratio
      left_eye_aspect_ratios.append(eye_aspect_ratio(left_eye))
      right_eye_aspect_ratios.append(eye_aspect_ratio(right_eye))
      # Check if the list has at least 3 points
      mv_avg_left_eye = 0
      mv_avg_right_eye = 0
      if len(left_eye_aspect_ratios) >= 3 and len(right_eye_aspect_ratios) >= 3:
        mv_avg_left_eye = (left_eye_aspect_ratios[-1] + left_eye_aspect_ratios[-2] + left_eye_aspect_ratios[-3])/3
        mv_avg_right_eye = (right_eye_aspect_ratios[-1] + right_eye_aspect_ratios[-2] + right_eye_aspect_ratios[-3])/3


    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
      break
  
vid.release()
cv2.destroyAllWindows()
# with open('eye_dataset/jack_left.npy', 'wb') as f:
#   np.save(f, np.array(left_save))
# with open('eye_dataset/jack_right.npy', 'wb') as f:
#   np.save(f, np.array(right_save))
#
# import matplotlib.pyplot as plt
# plt.plot(left_save)
# plt.plot(right_save)
# plt.show()
