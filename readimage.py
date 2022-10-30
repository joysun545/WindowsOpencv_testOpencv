# 加载图片
import cv2

cv2.namedWindow('img', cv2.WINDOW_NORMAL)
img = cv2.imread("C:\\Users\\joysu\\Pictures\\inputOpencv\\2.jpg")
cv2.imshow("img", img)
while True:
    key = cv2.waitKey(0)
    if key & 0xFF == ord('q'):
        exit()
    elif key & 0xFF == ord('s'):
        cv2.imwrite("C:\\Users\\joysu\\Pictures\\outOpencv\\test01.png", img)

cv2.destroyAllWindows()
