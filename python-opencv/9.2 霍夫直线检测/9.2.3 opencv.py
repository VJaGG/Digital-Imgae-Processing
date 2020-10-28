import cv2
import numpy as np


image = cv2.imread('9.jpg')
image = cv2.GaussianBlur(image, (3, 3), 0)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Canny边缘检测
edge = cv2.Canny(gray, 100, 200)
# 显示二值化的边缘

lines = cv2.HoughLinesP(edge, 1, np.pi / 180, 200)
result = image.copy()
for line in lines:
    rho = line[0][0]  # 第一个元素是距离rho
    theta = line[0][1]  # 第二个元素是角度theta
    print(rho)
    print(theta)
    if (theta < (np.pi/4.)) or (theta > (3.*np.pi/4.0)):  # 垂直直线
        pt1 = (int(rho/np.cos(theta)), 0)               # 该直线与第一行的交点
        # 该直线与最后一行的焦点
        pt2 = (int((rho-result.shape[0]*np.sin(theta))/np.cos(theta)),
               result.shape[0])
        cv2.line(result, pt1, pt2, (255))             # 绘制一条白线
    else:                                              # 水平直线
        pt1 = (0, int(rho/np.sin(theta)))               # 该直线与第一列的交点
        # 该直线与最后一列的交点
        pt2 = (result.shape[1],
               int((rho-result.shape[1]*np.cos(theta))/np.sin(theta)))
        cv2.line(result, pt1, pt2, (255), 1)           # 绘制一条直线

cv2.imshow('Canny', edge)
cv2.imshow('Result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()