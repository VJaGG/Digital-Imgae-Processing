import cv2
import numpy as np


I = np.array([[0, 200], [23, 4]], np.uint8)
print(I)
O = 2 * I
print(O)  # 这边200 * 2 = 400 但是输出为144
print(O.dtype)  # 这边的数据类型为np.uint8,所以结果发生了截断 400 % 256
# 当改为2.0的时候,数据类型发生了变化
O = 2.0 * I
print(O)
print(O.dtype)  # float64

path = '4.jpeg'
image = cv2.imread(path)
change2 = image.copy()
change3 = image.copy()
# print(dir(image))
print(image.dtype)
print(image.shape)
cv2.imshow("image", image)

change = image * 2  # 直接对图像乘以2,存在溢出
cv2.imshow("change", change)

change1 = image * 2.0  # 直接对原图乘以2.0
image = image * 2  # 对图像乘以2,存在溢出
image[change1 > 255] = 255  # 通过索引到大于255的位置,置为255
# print(image)

cv2.imshow("change1", image)

change2 = change2 * 2.0
change2 = np.round(change2)
change2[change2 > 255] = 255
change2 = change2.astype(np.uint8)
cv2.imshow("change2", change2)

change3 = change3 * 0.5
change3 = np.round(change3)
change3 = change3.astype(np.uint8)
cv2.imshow("change3", change3)
cv2.waitKey()
