# 图像的伽马变换实际上是对图像矩阵中的每一个值进行幂运算
# 伽马的幂运算时候,先使得像素的值归一化到[0, 1]之间这样便于计算


import cv2
import numpy as np
import matplotlib.pyplot as plt


path = "1.jpeg"
image = cv2.imread(path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print(image.dtype)

# 图像归一化
normalize = image / 255.0
gamma = 0.5
change = np.power(normalize, gamma)  # 生成的图像结果在[0, 1]之间
cv2.imshow("change", change)  # imshow在[0, 1]之间可以直接展示
change = change * 255
change = np.round(change)
change = change.astype(np.uint8)  # 转换为uint8之间显示
H, W = change.shape
pixelSequence = change.reshape(H*W)
plt.figure()
plt.hist(pixelSequence, 256)
plt.figure()
pixelSequence = image.reshape(H*W)
plt.hist(pixelSequence, 256)
cv2.imshow("normalize", change)
cv2.imshow("image", image)
plt.show()
cv2.waitKey()