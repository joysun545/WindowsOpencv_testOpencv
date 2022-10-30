#meanshift图像分割

import cv2
import numpy as np

img=cv2.imread("C:\\Users\\joysu\\Pictures\\inputOpencv\\2017.png")
mean_img=cv2.pyrMeanShiftFiltering(img,20,30)

canny_img=cv2.Canny(mean_img,150,300)

cv2.imshow('img',img)
cv2.imshow('mean_img',mean_img)
cv2.imshow('canny_img',canny_img)
cv2.waitKey()