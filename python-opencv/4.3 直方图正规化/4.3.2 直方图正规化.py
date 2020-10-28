import cv2
import numpy as np
import matplotlib.pyplot as plt


path = "4.jpeg"
image = cv2.imread(path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
rows, cols = image.shape
pixelSequence = image.reshape([rows*cols, -1])
plt.hist(pixelSequence, bins=256)
print(type(image))  # image的类型为<class 'numpy.ndarray'>
print(image.dtype)  # image都为uint8的
I_max = np.max(image)
I_min = np.min(image)
O_max = 100
O_min = 0
print(I_max)
print(I_min)
image1 = (O_max - O_min) / (I_max - I_min) * (image - I_min) + O_min
image1 = image1.astype(np.uint8)
pixelSequence = image1.reshape([rows*cols, -1])
plt.figure()
plt.hist(pixelSequence, bins=256)
cv2.imshow("image1", image1)
cv2.imshow("image", image)
plt.show()
cv2.waitKey()