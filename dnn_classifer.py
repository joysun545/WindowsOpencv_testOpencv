# dnn图片识别

import cv2
import numpy as np

# 导入模型，创建神经网络
config = "./models/bvlc_googlenet.prototxt"
model = "./models/bvlc_googlenet.caffemodel"
net = cv2.dnn.readNetFromCaffe(config, model)

# 读图片 转成 张量
img = cv2.imread("C:\\Users\\joysu\\Pictures\\inputOpencv\\cat.jpg")
blob = cv2.dnn.blobFromImage(img, 1.0, (224, 224), (104, 117, 123))

# 将张量输入到网络中 并进行预测
net.setInput(blob)
r = net.forward()

# 读取类目
classes = []
path = './models/synset_words.txt'
with open(path, 'rt') as f:
    classes = [x[x.find(" ") + 1:] for x in f]

z = list(range(3))
order = sorted(r[0], reverse=True)

for i in range(0, 3):
    z[i] = np.where(r[0] == order[i])[0][0]
    print('第', i + 1, '项,匹配：', classes[z[i]], end='')
    print('类所在行:', z[i] + 1, ' ', '可能性:', order[i])
