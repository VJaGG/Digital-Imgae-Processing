import numpy as np

hist = np.array([10, 3, 13, 2, 1, 5])
maxLoc = np.where(hist == np.max(hist))
print(maxLoc)  # 这里返回所有的位置的索引
maxLoc = np.argmax(hist)
print(maxLoc)  # 这里只是返回最大位置的第一个索引


hist = np.array([10, 23, 3, 23, 33, 30, 33, 12, 33])
maxLoc = np.where(hist == np.max(hist))
print(maxLoc)
maxLoc = np.argmax(hist)
print(maxLoc)


def threshTwoPeeks(image):
    # 