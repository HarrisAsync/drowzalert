from scipy.spatial import distance
from typing import List, Tuple
"""
Function to get eye aspect ratio
eye[0] Left middle point of eye
eye[1] Right middle point of eye
eye[2] Top left point of eye
eye[3] Top right point of eye
eye[4] Bottom left point of eye
eye[5] Bottom right point of eye
"""
def eye_aspect_ratio(eye: List[Tuple[float, float]]) -> float:
  # Euclidean distance between the two sets of vertical coordinates
  EAR1 = distance.euclidean(eye[1], eye[5])
  EAR2 = distance.euclidean(eye[2], eye[4])

  # Euclidean distance between the sets of horizontal coordinates
  EAR3 = distance.euclidean(eye[0], eye[3])

  EAR = (EAR1 + EAR2) / (2.0 * EAR3)

  return EAR


"""
mouth is a list of 20 (x,y) points
"""
def mouth_aspect_ratio(mouth: List[Tuple[tuple, tuple]]) -> float:
  # Euclidean distance between the three sets of vertical coordinates
  MAR1 = distance.euclidean(mouth[13], mouth[19])
  MAR2 = distance.euclidean(mouth[14], mouth[18])
  MAR3 = distance.euclidean(mouth[15], mouth[17])

  # Euclidean distance between the sets of horizontal coordinates
  MAR4 = distance.euclidean(mouth[12], mouth[16])

  MAR = (MAR1 + MAR2 + MAR3) / (3.0 * MAR4)
  return MAR


#print(eye_aspect_ratio([(20.2, 20.2),(32.0,20.2),(32.0,20.2),(32.0,20.2),(32.0,20.2),(32.0,20.2)]))
