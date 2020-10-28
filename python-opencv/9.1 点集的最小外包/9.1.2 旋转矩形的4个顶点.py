# -*- coding: utf-8 -*-
import cv2
import numpy as np


if __name__ == "__main__":
    # 旋转矩形
    vertices = cv2.boxPoints(((200, 200), (90, 150), (-60.0)))
    # 4个顶点
    print(vertices.dtype)
    print(vertices)

    img = np.zeros((400, 400), np.uint8)
    for i in range(4):
        # 相邻的点
        p1 = vertices[i, :]
        j = (i + 1) % 4
        p2 = vertices[j, :]
        cv2.line(img, (p1[0], p1[1]), (p2[0], p2[1]), 255, 2)
    cv2.imshow("img", img)
    cv2.waitKey()
