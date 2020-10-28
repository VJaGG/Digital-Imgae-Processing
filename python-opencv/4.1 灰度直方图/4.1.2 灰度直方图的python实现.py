import cv2
import numpy as np
import matplotlib.pyplot as plt


def calcGrayHist(image):
    # 灰度图像矩阵的宽度和高度
    rows, cols = image.shape
    # 存储灰度直方图
    grayHist = np.zeros([256])  # 可以这样建立数组
    # print(grayHist.shape)
    for r in range(rows):
        for c in range(cols):
            grayHist[image[r, c]] += 1
    return grayHist


if __name__ == "__main__":
    image = cv2.imread("roi.jpeg")
    # print(image.shape)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    grayHist = calcGrayHist(gray)
    # print(histGray)
    # print(gray.shape)
    x_range = range(256)
    # plt.plot(x_range, grayHist, 'r', linewidth=2, c='black')
    plt.bar(x_range, grayHist)
    # 设置坐标轴的范围
    y_max_value = np.max(grayHist)
    plt.axis([0, 255, 0, y_max_value])
    # 设置坐标轴标签
    plt.xlabel('gray level')
    plt.ylabel('number of pixels')
    plt.show()
    # cv2.imshow("image", image)
    # cv2.imshow("gray", gray)
    # cv2.waitKey()
