#自适应阈值二值化

import cv2
import numpy as np

img = cv2.imread("C:\\Users\\joysu\\Pictures\\inputOpencv\\12.jpg")
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

dst = cv2.adaptiveThreshold(img1, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,3,0)
dst2 = cv2.adaptiveThreshold(img1, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,3,0)


cv2.imshow('img', img)
cv2.imshow('img1', img1)
cv2.imshow('dst', dst)
cv2.imshow('dst2', dst2)
cv2.imwrite("C:\\Users\\joysu\\Pictures\\inputOpencv\\101.jpg",dst)
cv2.imwrite("C:\\Users\\joysu\\Pictures\\inputOpencv\\102.jpg",dst2)

cv2.waitKey(0)