#!/bin/sh

curl http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2 -- output shape_predictor_68_face_landmarks.dat.bz2 && bzip2 -dk shape_predictor_68_face_landmarks.dat.bz2

