# 图片边缘识别

import cv2
import numpy as np

img=cv2.imread("C:\\Users\\joysu\\Pictures\\inputOpencv\\2015.jpg")
dst=cv2.Canny(img,50,100)

cv2.imshow('img',img)
cv2.imshow('dst',dst)
cv2.waitKey(0)

