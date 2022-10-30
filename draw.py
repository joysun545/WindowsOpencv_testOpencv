# 各种绘制

import cv2
import numpy as np

img = np.ones((460, 680, 3), np.uint8)
img[:] = [255,255,255]
# img=cv2.imread("C:\\Users\\joysu\\Pictures\\inputOpencv\\opencv-test-02.png")
# # 画线的参数 img指定划线的画面 （10，10）画线的起始坐标 （300，300）画线的终点坐标  （0，0，255）线的颜色  5线的粗细 4线的类型（-1，4，8，16）
cv2.line(img, (100, 100), (300, 100), (0, 0, 0), 3, 4)
cv2.line(img, (100, 100), (290, 20), (0, 0, 0), 3, 4)
cv2.line(img, (400, 200), (600, 200), (0, 0, 0), 3, 4)
cv2.line(img, (400, 200), (400, 20), (0, 0, 0), 3, 4)
cv2.line(img, (350, 250), (180, 350), (0, 0, 0), 3, 4)
cv2.line(img, (350, 250), (500, 380), (0, 0, 0), 3, 4)
#
# # 画矩形
# cv2.rectangle(img, (10, 10), (300, 300), (0, 0, 255))
# cv2.rectangle(img, (100, 100), (200, 200), (0, 255, 0), -1)
#
# # 画圆
# cv2.circle(img, (300, 300), 100, (255, 0, 0))
# cv2.circle(img, (300, 300), 30, (255, 255, 0), -1)
#
# # 画椭圆  角度按x轴正方向为0°，再顺时针叠加 0表示椭圆x轴与0°线的夹角，45表示画圆的起始点与0°线的夹角，270表示画圆终止点与0°线的夹角
# cv2.ellipse(img, (300, 300), (250, 150), 0, 45, 270, (0, 255, 255), -1)
# cv2.ellipse(img, (300, 300), (150, 80), 60, 0, 270, (0, 255, 0), -1)

# 画多边形 [pts]是一个点集数组，True表示闭合（Fasle则反之），（0，0，255）表示颜色 点集的数据类型必须是int32的
# pts = np.array([(300, 80), (150, 100), (250, 100),(200,150),(350,150),(300,200),(500,300),(350,180),(420,120),(280,120),(330,80)], np.int32)
# cv2.polylines(img, [pts], True, (0, 0, 255))
# cv2.fillPoly(img, [pts], (255, 255, 255))

# 绘制文本
# cv2.putText(img, "TEST", (60, 200), 2, 1, (0,0,0))
# cv2.putText(img, "Test learning", (60, 280), 1, 1, (0,0,0))
# cv2.putText(img, "1 2 3 4 5 6 7 8 9 10 11 12 13", (60, 360), 1, 1, (0,0,0))
# cv2.putText(img, "joysun learns code!", (60, 440), 1, 1, (0,0,0))

cv2.imshow('draw', img)
cv2.imwrite("C:\\Users\\joysu\\PycharmProjects\\pythonProject02\\images\\angle.png",img)
cv2.waitKey(0)
