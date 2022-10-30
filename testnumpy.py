# 定义各种矩阵

import numpy as np
import cv2
from math import cos

# 通过array定义矩阵
# a = np.array([1, 2, 3])
# b = np.array([[1, 2, 3], [4, 5, 6]])
# print(a)
# print(b)

# 定义zeros矩阵
# c = np.zeros((480, 640, 3), np.uint8)
# print(c)

# 定义ones矩阵
# d=np.ones((480,640,3,np.uint8))
# print(d)

# 定义full矩阵
# e=np.full((8,8,3),155,np.uint8)
# print(e)

# 定义单位矩阵identity
# f=np.identity(4)   #4行4列对角线是1
# print(f)

# 定义一个长方形的单位矩阵eye
# g = np.eye(5, 7, k=3)  # 5x7的长方形矩阵，从第1行的第4个开始对角线为1
# print(g)


# print(c[100,100])   # 索检
# count=0
# while count<200:
#     c[count,100,2]=255   # 第count行，第100列，第3通道的像素值为255 那么这个点的rgb值就是[0,0,255]即是红色
#     count=count+1

img=cv2.imread("C:\\Users\\joysu\\Pictures\\inputOpencv\\opencv-logo.png")

# 定义一个子矩阵
roi = img[0:180, 0:180]
# roi[:, :] = [0, 0, 255]
# roi[50:150, 50:250] = [0, 255, 0]
# roi[70, 50:250] = [255, 0, 0]
# roi[50:150, 70] = [255, 0, 0]
# roi[80:120, 80:220] = [255, 0, 0]
# roi[90, 80:220] = [255, 255, 255]
# roi[80:120, 90] = [255, 255, 255]
# roi[30, :] = [0, 255, 0]
# roi[:, 30] = [0, 255, 0]

cv2.imshow('roi', roi)
cv2.imwrite("C:\\Users\\joysu\\Pictures\\inputOpencv\\opencv-logo-02.png",roi)
key = cv2.waitKey()
if key & 0xFF == ord('q'):
    cv2.destroyAllWindows()
