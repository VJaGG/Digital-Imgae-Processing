import cv2
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def HTLine(image, stepTheta=1, stepRho=1):
    # 宽、高
    rows, cols = image.shape
    print(rows, cols)

    # 图像中可能出现的最大垂线的长度
    L = round(np.sqrt((rows - 1)**2 + (cols - 1)**2)) + 1

    # 初始化投票器
    numtheta = int(180.0 / stepTheta)
    numRho = int(2 * L / stepRho + 1)  # 为负数的rho，也在正数范围之内
    accumulator = np.zeros((numRho, numtheta), np.int32)

    # 建立字典
    accuDict = {}
    for k1 in range(numRho):
        for k2 in range(numtheta):
            accuDict[(k1, k2)] = []

    # 投票计数
    for y in range(rows):
        for x in range(cols):
            if image[y][x] == 255:  # 只对边缘点做霍夫变换
                for m in range(numtheta):
                    # 对于每一个角度计算出对应的rho值
                    theta = stepTheta * m / 180.0 * np.pi
                    rho = x * np.cos(theta) + y * np.sin(theta)

                    # 计算投票到哪一个区域
                    n = int(round(rho + L) / stepRho)

                    # 投票加1
                    accumulator[n, m] += 1

                    # 记录该点
                    accuDict[(n, m)].append((y, x))
    return accumulator, accuDict


if __name__ == "__main__":
    # gray = cv2.imread('1.jpeg', cv2.IMREAD_GRAYSCALE)

    # 读入灰度图像
    image = cv2.imread('9.jpg')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Canny边缘检测
    edge = cv2.Canny(gray, 50, 200)
    # 显示二值化的边缘
    cv2.imshow('edge', edge)

    # 霍夫直线检测
    accumulator, accuDict = HTLine(edge, 1, 1)

    # 计算器的二维直方图显示
    rows, cols = accumulator.shape
    print(rows, cols)
    fig = plt.figure()
    ax = Axes3D(fig)
    X, Y = np.mgrid[0: rows: 1, 0: cols: 1]
    surf = ax.plot_wireframe(X, Y, accumulator, cstride=1, rstride=1, color='gray')
    ax.set_xlabel(u"$\\rho")
    ax.set_ylabel(u"$\\theta")
    ax.set_zlabel("accumulator")
    ax.set_zlim3d(0, np.max(accumulator))

    # 计数器的灰度级显示
    grayAcc = accumulator / float(np.max(accumulator))
    grayAcc = 255 * grayAcc
    grayAcc = grayAcc.astype(np.uint8)

    # 只画出投票数大于60的
    voteThresh = 100
    for r in range(rows):
        for c in range(cols):
            if accumulator[r][c] > voteThresh:
                points = accuDict[(r, c)]
                cv2.line(edge, points[0], points[len(points)-1], (255), 1)
    cv2.imshow('accumulator', grayAcc)

    cv2.imshow("image", edge)
    plt.show()
    cv2.waitKey()
    # cv2.waitKey()