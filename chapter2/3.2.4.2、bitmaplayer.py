import cv2
import numpy as np


def bitmap(n):
    map = []
    for i in range(256):
        if i & pow(2, n-1) == pow(2, n-1):
            map.append(255)
        else:
            map.append(0)
    print(map)
    return map


def bitimage(x, n):
    image = x.copy()
    height, width = image.shape
    map = bitmap(n)
    for rows in range(height):
        for cols in range(width):
            image[rows, cols] = map[image[rows, cols]]
    return image


if __name__ == '__main__':
    original = cv2.imread('imgae\Fig0314(a)(100-dollars).tif',
                          cv2.IMREAD_GRAYSCALE)

    cv2.imshow('a', original)
    """
    b = bitimage(original,1)
    cv2.imshow('bitmap1',b)
    c = bitimage(original,2)
    cv2.imshow('bitmap2',c)
    d = bitimage(original,3)
    cv2.imshow('bitmap3',d)
    e = bitimage(original,4)
    cv2.imshow('bitmap4',e)
    f = bitimage(original,5)
    cv2.imshow('bitmap5',f)
    g = bitimage(original,6)
    cv2.imshow('bitmap6',g)
    h = bitimage(original,7)
    cv2.imshow('bitmap7',h)
    i = bitimage(original,8)
    cv2.imshow('bitmap8',i)
    """
    bit5 = bitimage(original, 5)
    bit6 = bitimage(original, 6)
    bit7 = bitimage(original, 7)
    bit8 = bitimage(original, 8)

    bit5 = np.where(bit5 == 255, 16, 0)
    bit6 = np.where(bit6 == 255, 32, 0)
    bit7 = np.where(bit7 == 255, 64, 0)
    bit8 = np.where(bit8 == 255, 128, 0)
    re_7_8 = np.uint8(bit7 + bit8)
    re_6_7_8 = np.uint8(bit6 + bit7 + bit8)
    re_5_6_7_8 = np.uint8(bit5 + bit6 + bit7 + bit8)
    cv2.imshow('re_7_8', re_7_8)
    cv2.imshow('re_6_7_8', re_6_7_8)
    cv2.imshow('re_5_6_7_8', re_5_6_7_8)

    '''
    a = np.array([1,3,4,5,6,1,1,1])
    a = np.where(a==1,0,255)
    '''
    cv2.waitKey()