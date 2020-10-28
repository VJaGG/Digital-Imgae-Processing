import cv2
import numpy as np
import matplotlib.pyplot as plt


points = np.array([[1, 1], [2, 1], [3, 1], [3, 0], [2, 2], [3, 3], [1, 1]], np.int32)
x = points[:, 0]
y = points[:, 1]
plt.figure(figsize=(10, 10))
plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.scatter(x, y)
circle = cv2.minEnclosingCircle(points)
print(circle)
circle = plt.Circle(circle[0], radius=circle[1], )
plt.gcf().gca().add_artist(circle)
plt.show()
