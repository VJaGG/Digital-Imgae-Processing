import cv2
import numpy as np


def log(x, c):
    return np.uint8(c * np.log10(x + 1.0) / np.log10(255.0+ 1) * 255.0)


def log_transform(x, c):
    map = []
    for i in range(256):
        t = c * np.log10(i + 1) / np.log10(255 + 1) * 255
        map.append(int(np.ceil(t)))
    print(map)
    width, height = x.shape
    print(width)
    print(height)
    image = np.zeros((width, height), np.uint8)
    for i in range(height):
        for j in range(width):
            image[i][j] = map[x[i][j]]
    return image


if __name__ == '__main__':
    original = cv2.imread('./image/Fig0305(a)(DFT_no_log).tif',
                          cv2.IMREAD_GRAYSCALE)

    cv2.imshow('original', original)
    transform = log(original, 1)
    print(transform)

    cv2.imshow('transform', transform)
    cv2.waitKey()
