import cv2
import numpy as np
import matplotlib.pyplot as plt


# points = np.array([[0, 0], [1, 1], [5, 10], [5, 1], [1, 10], [2, 5], [-3, -4]])
# rect = cv2.boundingRect(points)
# print(rect)
# x = points[:, 0]
# y = points[:, 1]

# xmin, ymin, w, h = rect
# plt.scatter(x, y)
# plt.plot((xmin, xmin), (ymin, ymin+h))
# plt.plot((xmin, xmin+w), (ymin+h, ymin+h))
# plt.plot((xmin+w, xmin+w), (ymin+h, ymin))
# plt.plot((xmin+w, xmin), (ymin, ymin))
# plt.show()

plt.figure()
n = 80
points = np.random.randint(100, 300, (n, 2), np.int32)
# 在画板上用一个小圆标出这些点
print(points.shape)
for i in range(n):
    plt.scatter(points[i, 0], points[i, 1])
rect = cv2.boundingRect(points)
print(rect)
xmin, ymin, w, h = rect
plt.plot((xmin, xmin), (ymin, ymin+h))
plt.plot((xmin, xmin+w), (ymin+h, ymin+h))
plt.plot((xmin+w, xmin+w), (ymin+h, ymin))
plt.plot((xmin+w, xmin), (ymin, ymin))
plt.show()