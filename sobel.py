# 高通滤波 索贝尔 沙尔 拉普拉斯算子

import cv2
import numpy as np

img = cv2.imread("C:\\Users\\joysu\\Pictures\\inputOpencv\\2015.jpg")

# 索贝尔算子y方向边缘
dy = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
# 索贝尔算子x方向边缘
dx = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)

# 沙尔算子y方向边缘
dy2 = cv2.Scharr(img, cv2.CV_64F, 1, 0)
# 沙尔算子x方向边缘
dx2 = cv2.Scharr(img, cv2.CV_64F, 0, 1)

dst = cv2.add(dy, dx)
dst2 = cv2.add(dy2, dx2)

# 拉普拉斯算子
dst3 = cv2.Laplacian(img, cv2.CV_64F, ksize=5)

cv2.imshow('img', img)
# cv2.imshow('dy',dy)
# cv2.imshow('dx',dx)
cv2.imshow('dst', dst)
cv2.imshow('dst2', dst2)
cv2.imshow('dst3', dst3)
cv2.imwrite("C:\\Users\\joysu\\Pictures\\inputOpencv\\201501.jpg", dst)
cv2.imwrite("C:\\Users\\joysu\\Pictures\\inputOpencv\\201502.jpg", dst2)
cv2.imwrite("C:\\Users\\joysu\\Pictures\\inputOpencv\\201503.jpg", dst3)

cv2.waitKey(0)
