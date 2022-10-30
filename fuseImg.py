# 图片融合

import cv2
import numpy as np

back = cv2.imread('C:\\Users\\joysu\\Pictures\\joysun\\2009.jpg')
before = cv2.imread('C:\\Users\\joysu\\Pictures\\joysun\\20052.jpg')

print(back.shape)
print(before.shape)
result = cv2.addWeighted(back, 0.7, before, 0.3, 0)  # 0.7和0.3分别代表两张照片在融合时的权重
cv2.imshow('fuse', result)
cv2.waitKey(0)
