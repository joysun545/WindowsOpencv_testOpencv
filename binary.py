#全局阈值二值化

import cv2
import numpy as np

img = cv2.imread("C:\\Users\\joysu\\Pictures\\inputOpencv\\10.jpg")
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, dst = cv2.threshold(img1, 180, 255, cv2.THRESH_BINARY)
ret2, dst2 = cv2.threshold(img1, 180, 255, cv2.THRESH_BINARY_INV)

cv2.imshow('img', img)
cv2.imshow('img1', img1)
cv2.imshow('dst', dst)
cv2.imshow('dst2', dst2)

cv2.waitKey(0)
