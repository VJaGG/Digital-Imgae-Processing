import cv2
import numpy as np
import matplotlib.pyplot as plt


points = np.array([[[1, 1]], [[5, 10]], [[5, 1]], [[1, 10]], [[2, 5]]], np.float32)
print(points.dtype)
print(points.shape)
# 最小外包三角形
for i in range(points.shape[0]):
    plt.scatter(points[i, 0, 0], points[i, 0, 1])

area, triangle = cv2.minEnclosingTriangle(points)

print(area)
print(triangle)
print(triangle.shape)
plt.plot((triangle[0, 0, 0], triangle[1, 0, 0]),
         (triangle[0, 0, 1], triangle[1, 0, 1]))
plt.plot((triangle[1, 0, 0], triangle[2, 0, 0]),
         (triangle[1, 0, 1], triangle[2, 0, 1]))
plt.plot((triangle[2, 0, 0], triangle[0, 0, 0]),
         (triangle[2, 0, 1], triangle[0, 0, 1]))
plt.show()
