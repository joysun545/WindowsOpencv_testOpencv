# 透视变换
import cv2
import numpy as np

img = cv2.imread("C:\\Users\\joysu\\Pictures\\inputOpencv\\10.jpg")
print(img.shape)
src = np.float32([[300, 100], [1170, 200], [150, 1600], [1170, 1600]])  # 点击坐标分别是 左上角、右上角、左下角、右下角
dst = np.float32([[0, 0], [1000, 0], [0, 1500], [1000, 1500]])
M = cv2.getPerspectiveTransform(src, dst)
new = cv2.warpPerspective(img, M, (950, 1500))
cv2.imshow('orgin', img)
cv2.imshow('new', new)
cv2.imwrite("C:\\Users\\joysu\\Pictures\\inputOpencv\\12.jpg", new)
cv2.waitKey()
