import cv2
import numpy as np


path = '9.jpg'
image = cv2.imread(path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# 边缘检测或者阈值处理成一张二值图像
# blur = cv2.GaussianBlur(gray, (3, 3), 0.5)  # 高斯平滑处理
edge = cv2.Canny(image, 50, 200)

# 边缘的轮廓返回的contours是一个list的列表
contours, hc = cv2.findContours(edge, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# 打印轮廓的数据
print(type(contours))
# contours的每一个元素都是一个ndarry，打印它的shape属性
print(contours[0].shape)

# 轮廓的数量
n = len(contours)
print(n)
contoursImg = []

for i in range(n):
    # 创建一个黑色的画布
    temp = np.zeros(edge.shape, np.uint8)
    contoursImg.append(temp)
    cv2.drawContours(contoursImg[i], contours, i, 255, 2)
    cv2.imshow("contour-"+str(i), contoursImg[i])

cv2.imshow("contours", temp)
cv2.imshow("edge", edge)
cv2.imshow("gray", gray)
cv2.waitKey()