import cv2
import numpy as np
import matplotlib.pyplot as plt


path = '4.jpeg'
image = cv2.imread(path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
H, W = image.shape
pixelSequence = image.reshape(H*W)
plt.figure()
plt.hist(pixelSequence, bins=256)
print(pixelSequence.shape)
cv2.imshow("image", image)
arr = image.copy()  # 第二个参数是正规化的结果,与返回结果相同

normalize = cv2.normalize(image, arr, 100, 0, cv2.NORM_MINMAX, cv2.CV_8U)
cv2.imshow("normalize", normalize)
pixelSequence = normalize.reshape(H*W)
plt.figure()
plt.hist(pixelSequence, bins=256)
plt.show()
cv2.waitKey()
