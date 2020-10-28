import cv2
import numpy as np
import matplotlib.pyplot as plt


image = cv2.imread("roi.jpeg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print(gray.shape)
rows, cols = gray.shape
# 将二维的图像矩阵转为一维的数组，便于直接计算灰度直方图
pixelSequence = gray.reshape([rows * cols, ])
print(pixelSequence.shape)
# 组数
numberBins = 256
historgram, bins, patch = plt.hist(pixelSequence, numberBins, histtype='bar')
print(bins)
print(patch)
plt.xlabel(u"gray level")
plt.ylabel(u"number of pixels")

# 设置坐标轴的范围
y_maxValue = np.max(historgram)
plt.axis([0, 255, 0, y_maxValue])
plt.show()
# cv2.imshow("gray", gray)
# cv2.waitKey()

