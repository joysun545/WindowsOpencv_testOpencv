# 图片的 与 或 异或 操作

import cv2
import numpy as np

img = np.zeros((200, 200), np.uint8)
img2 = np.zeros((200, 200), np.uint8)

img[20:120, 20:120] = 255
img2[80:180, 80:180] = 255

# img=cv2.imread('C:\\Users\\joysu\\Pictures\\inputOpencv\\2.jpg')
# img2=cv2.imread('C:\\Users\\joysu\\Pictures\\inputOpencv\\3.jpg')

new_img = cv2.bitwise_and(img, img2)  # 与操作
new_img2 = cv2.bitwise_or(img, img2)  # 或操作
new_img3 = cv2.bitwise_xor(img, img2)  # 异或操作

cv2.imshow('img', img)
cv2.imshow('img2', img2)
cv2.imshow('new_img', new_img)
cv2.imshow('new_img2', new_img2)
cv2.imshow('new_img3', new_img3)
cv2.waitKey(0)
