import cv2


def reverse(x):
    x = 255-x
    return x


if __name__ == '__main__':
    image = cv2.imread('./image/Fig0304(a)(breast_digital_Xray).tif',
                       cv2.IMREAD_GRAYSCALE)
    print(image.shape)
    cv2.imshow('original', image)
    image = reverse(image)
    cv2.imshow('reversal', image)
    cv2.waitKey()
