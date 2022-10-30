# 像素值运算

import cv2
import numpy as np

fireImg = cv2.imread('C:\\Users\\joysu\\Pictures\\inputOpencv\\3.jpg')

img = np.ones((426, 640, 3), np.uint8) * 30

cv2.imshow('fireImg', fireImg)
result = cv2.add(fireImg, img)  # 像素值相加  减 乘 除的API分别是 subtract multiply divide
cv2.imshow('result', result)
cv2.waitKey(0)
