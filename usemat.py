# 浅拷贝和深拷贝

import cv2
import numpy as np

img=cv2.imread("C:\\Users\\joysu\\Pictures\\inputOpencv\\3.jpg")

# 浅拷贝
img2=img

# 深拷贝
img3=img.copy()

img[10:80,10:80]=[0,0,255]

cv2.imshow('img',img)
cv2.imshow('img2',img2)
cv2.imshow('img3',img3)

cv2.waitKey(0)