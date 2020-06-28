# -*- coding: utf-8 -*-
"""OpenCV-Face Detection.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Dd5K8ztsjezEuGx4Bj7tO8_673YXPm_K
"""

import cv2
from google.colab import files
file=files.upload()

import cv2
from google.colab import files
file=files.upload()

import numpy as np
import cv2
import matplotlib.pyplot as plt

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img = cv2.imread('Angelina-Jolie.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
print(faces)

for (x,y,w,h) in faces:
  cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
  roigray = gray[y:y+h, x:x+w]
  roicolor = img[y:y+h, x:x+w]
plt.grid(None)
plt.xticks([])
plt.yticks([])
imgplot = plt.imshow(img)