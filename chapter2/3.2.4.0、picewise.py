import cv2
import numpy as np


def f(x, r1, s1, r2, s2):
    if r1 == r2:
        if x < r1:
            return 0
        else:
            return 255
    if x <= r1:
        return s1 / r1 * x
    elif x > r1 and x <= r2:
        return s1+(s2-s1)/(r2-r1)*(x-r1)
    else:
        return s2+(255.0-s2)/(255.0-r2)*(x-r2)


def picewise(x, r1, s1, r2, s2):
    image = x.copy()
    height, width = image.shape
    map = []
    for i in range(256):
        map.append(int(f(i, r1, s1, r2, s2)))
    for rows in range(height):
        for cols in range(width):
            image[rows, cols] = map[image[rows, cols]]
    print(map)
    return image




if __name__ == '__main__':
    original = cv2.imread('imgae\\Fig0310(b)(washed_out_pollen_image).tif',cv2.IMREAD_GRAYSCALE)
    cv2.imshow('b',original)
    rmin = np.min(original)
    rmax = np.max(original)
    print(rmin)
    print(rmax)
    transform = picewise(original,rmin,0,rmax,255)
    cv2.imshow('c',transform)
    rmean = np.mean(original)
    transform2 = picewise(original,rmean,0,rmean,255)
    cv2.imshow('d',transform2)

    cv2.waitKey()