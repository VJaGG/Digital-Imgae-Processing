import cv2
def graylevel(x):
    image = x.copy()
    height,width = image.shape
    map= []
    for i in range(256):
        if i>145 and i<240:
            map.append(255)
        else:
            map.append(0)
    print(map)
    for rows in range(height):
        for cols in range(width):
            image[rows,cols] = map[image[rows,cols]]
    return image
def graylevel1(x,r1,r2,s):
    image = x.copy()
    height,width = image.shape
    map = []
    for i in range(256):
        if i > r1 and i < r2:
            map.append(s)
        else:
            map.append(i)
    print(map)
    for rows in range(height):
        for cols in range(width):
            image[rows,cols] = map[image[rows,cols]]
    return image
if __name__ == '__main__':
    original = cv2.imread('imgae\Fig0312(a)(kidney).tif',cv2.IMREAD_GRAYSCALE)
    cv2.imshow('original',original)

    transform = graylevel(original)
    transform1 = graylevel1(original,80,146,0)
    cv2.imshow('b',transform)
    cv2.imshow('c',transform1)
    cv2.waitKey()