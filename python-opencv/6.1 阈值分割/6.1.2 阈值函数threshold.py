import cv2
import numpy as np


if __name__ == "__main__":
    src = np.array([[123, 234, 68], [33, 51, 17], [48, 98, 234],
                    [129, 89, 27], [46, 167, 134]], np.uint8)
    print(src.dtype)
    # 手动设置阈值
    the = 150
    maxval = 255
    dst = cv2.threshold(src, the, maxval, cv2.THRESH_BINARY)
    print(dst)

    # Otsu 阈值处理
    otsuThe = 0
    otsuThe, dst_Otsu = cv2.threshold(src, otsuThe, maxval, cv2.THRESH_OTSU)
    print(otsuThe)  # 阈值
    print(dst_Otsu)  # 阈值分割后的结果

    # TRIANGLE 阈值处理
    triThe = 0
    triThe, dst_Tri = cv2.threshold(src, triThe, maxval,
                                    cv2.THRESH_TRIANGLE+cv2.THRESH_BINARY)
    print(triThe)
    print(dst_Tri)

