# 像素索检和赋值

import cv2
import numpy as np

img1 = cv2.imread("C:\\Users\\joysu\\Pictures\\inputOpencv\\opencv-logo-02.png")
img2 = np.zeros((280, 220, 3), np.uint8)

# b, g, r = cv2.split(img)  # 分割通道
# b[10:100, 10:100] = 255  # 按索引赋值
# g[10:100, 10:100] = 255  # 按索引赋值

# img2 = cv2.merge((b, g, r))  # 合并通道
img2[20:200, 20:200] = img1
cv2.imshow('img1', img1)
# cv2.imshow('b', b)
# cv2.imshow('g', g)
# cv2.imshow('r', r)
cv2.imshow('img2', img2)
cv2.imwrite("C:\\Users\\joysu\\Pictures\\inputOpencv\\opencv-test-02.png", img2)
cv2.waitKey(0)
