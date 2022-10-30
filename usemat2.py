# 获取图片属性

import cv2
import numpy as np

img = cv2.imread("C:\\Users\\joysu\\Pictures\\inputOpencv\\3.jpg")

print(img.shape)  # 打印shape得到三个参数：图片的长宽和通道数

print(img.size)  # 打印size得到图片数据大小（长*宽*通道数）

print(img.dtype)  # 打印type得到图片中每个元素的位深
