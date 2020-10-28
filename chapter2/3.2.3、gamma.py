import cv2
import numpy as np


def gamma(x, r):
    map = [i for i in range(256)]
    map = np.ceil(np.power(map, r, dtype=np.double)/np.power(255, r, dtype=np.double)*255.0)
    print(map)
    height, width = x.shape
    image = np.zeros((height, width), dtype=np.uint8)
    for i in range(height):
        for j in range(width):
            image[i][j] = map[x[i][j]]

    return image


if __name__ == '__main__':

    original = cv2.imread('./image/Fig0307(a)(intensity_ramp).tif',
                          cv2.IMREAD_GRAYSCALE)
    cv2.imshow('original', original)
    transform = gamma(original, 0.4)
    cv2.imshow('transform', transform)
    original1 = cv2.imread('./image/Fig0308(a)(fractured_spine).tif',
                           cv2.IMREAD_GRAYSCALE)
    cv2.imshow('original1', original1)
    transform6 = gamma(original1, 0.6)
    cv2.imshow('transform6', transform6)
    transform4 = gamma(original1, 0.4)
    cv2.imshow('transform4', transform4)
    transform3 = gamma(original1, 0.3)
    cv2.imshow('transform3', transform3)

    original2 = cv2.imread('./image/Fig0309(a)(washed_out_aerial_image).tif',
                           cv2.IMREAD_GRAYSCALE)
    cv2.imshow('original2', original2)
    transform_3 = gamma(original2, 3.0)
    transform_4 = gamma(original2, 4.0)
    transform_5 = gamma(original2, 5.0)

    cv2.imshow('transform_3', transform_3)
    cv2.imshow('transform_4', transform_4)
    cv2.imshow('transform_5', transform_5)

    cv2.waitKey()
