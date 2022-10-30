# 图片像素大小缩放 重新生成图片的像素大小

import cv2

img = cv2.imread("./images/detectionCode.jpg")
print(img.shape)

# resize可导入四个参数 img表示操作的对象，（640，426）表示缩放到指定的像素大小，
# 如果这个值取None,在后面添加fx=0.3,fy=0.5,表示新生成长宽是原长宽的倍数，
# 在后面可设定缩放模式，共4种
new = cv2.resize(img, (480, 640))

cv2.imshow('img1', new)

cv2.imwrite("C:\\Users\\joysu\\Pictures\\inputOpencv\\2017.png", new)

cv2.waitKey(0)
