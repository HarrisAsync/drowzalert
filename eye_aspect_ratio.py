from scipy.spatial import distance
from typing import List, Tuple

"""
Function to get eye aspect ratio
eye[0] Left middle point of eye
eye[1] Top left point of eye
eye[2] Top right point of eye
eye[3] Right middle point of eye
eye[4] Bottom right point of eye
eye[5] Bottom left point of eye
"""
def eye_aspect_ratio(eye: List[Tuple[float, float]]) -> float:
  # Distance between vertical coordinates
  D_1 = distance.euclidean(eye[1], eye[5])
  D_2 = distance.euclidean(eye[2], eye[4])
  # Distance between horizontal coordinates
  D_3 = distance.euclidean(eye[0], eye[3])
  return (D_1+D_2)/(2.0*D_3)

#print(eye_aspect_ratio([(20.2, 20.2),(32.0,20.2),(32.0,20.2),(32.0,20.2),(32.0,20.2),(32.0,20.2)]))
