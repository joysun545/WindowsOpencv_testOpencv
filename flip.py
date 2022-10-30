#图片翻转

import cv2
import numpy as np

img = cv2.imread("C:\\Users\\joysu\\Pictures\\inputOpencv\\1.jpg")

new = cv2.flip(img, 0)  # 上下翻转
new2 = cv2.flip(img, 1)  # 左右翻转
new3 = cv2.flip(img, -1)  # 上下加左右翻转，相当于旋转180°

cv2.imshow('new', new)
cv2.imshow('new2', new2)
cv2.imshow('new3', new3)

cv2.waitKey(0)
cv2.destroyAllWindows()
