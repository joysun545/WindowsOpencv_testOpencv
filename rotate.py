#图片旋转

import cv2
import numpy as np

img = cv2.imread('C:\\Users\\joysu\\Pictures\\inputOpencv\\1.jpg')
new = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)  # 顺时针90°旋转
new2 = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)  # 逆时针90°旋转
new3 = cv2.rotate(img, cv2.ROTATE_180)  # 180°旋转

cv2.imshow('img', img)
cv2.imshow('new', new)
cv2.imshow('new2', new2)
cv2.imshow('new3', new3)
cv2.waitKey(0)
