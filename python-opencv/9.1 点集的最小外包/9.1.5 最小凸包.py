import numpy as np
import cv2

s = 400
I = np.zeros((s, s), np.uint8)
# 随机生成横、纵坐标均在100至300之间的坐标点
n = 80  # 随机生成n个坐标点，每一行存储一个坐标
points = np.random.randint(100, 300, (n, 2), np.int32)
# 在画板上用一个小圆标出这些点
for i in range(n):
    cv2.circle(I, (points[i, 0], points[i, 1]), 2, 255, 2)

# 求点集points的凸包
convexhull = cv2.convexHull(points)

# print(convexhull)
print(convexhull.shape)
# 依次连接凸包的各个点
# print(points)
rect = cv2.boundingRect(points)  # 返回的是左下角的坐标和w, h
print(rect)
cv2.rectangle(I, (rect[0], rect[1]), (rect[0]+rect[2], rect[1]+rect[3]), 255, 2)
k = convexhull.shape[0]
for i in range(k-1):
    cv2.line(I,
             (convexhull[i, 0, 0], convexhull[i, 0, 1]),
             (convexhull[i+1, 0, 0], convexhull[i+1, 0, 1]), 255, 2)

cv2.line(I, (convexhull[k-1, 0, 0], convexhull[k-1, 0, 1]),
         (convexhull[0, 0, 0], convexhull[0, 0, 1]), 255, 2)

cv2.imshow("I", I)
cv2.waitKey()
cv2.destroyAllWindows()