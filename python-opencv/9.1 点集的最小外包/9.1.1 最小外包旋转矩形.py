import cv2
import numpy as np
import matplotlib.pyplot as plt

# 点集
points = np.array([[1, 1], [5, 1], [1, 10], [5, 10], [2, 5], [6, 9], [-1, -4]], np.int32)
print(points.shape)
x = points[:, 0]
y = points[:, 1]
plt.scatter(x, y)
# plt.show()

# 计算点集最小外包旋转矩形
rotatedRect = cv2.minAreaRect(points)
print(rotatedRect)
vertices = cv2.boxPoints(rotatedRect)
print(vertices.dtype)
print(vertices)
for i in range(4):
    p1 = vertices[i, :]
    j = (i + 1) % 4
    p2 = vertices[j, :]
    print('----')
    print(p1)
    print(p2)
    plt.plot((p1[0], p2[0]), (p1[1], p2[1]))  
    # 不是点p1和p2而是两者的横坐标和纵坐标
plt.show()
