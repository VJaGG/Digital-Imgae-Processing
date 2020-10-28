import cv2

# 3x3的矩形结构
s = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
print(s)

# 5x5的椭圆结构
s = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
print(s)

# 5x3的十字结构
s = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 5))
print(s)

print("=======")
s = cv2.getStructuringElement(cv2.MORPH_DILATE, (5, 5))
print(s)

if __name__ == "__main__":
    path = '4.jpeg'
    image = cv2.imread(path)
    edge1 = cv2.Canny(image, 50, 200)
    s = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    # 腐蚀图像，迭代次数采用默认值1
    r = cv2.erode(image, s)
    # 边界提取
    e = image - r
    edge2 = cv2.Canny(r, 50, 200)
    cv2.imshow('image', image)
    cv2.imshow('erode', r)
    cv2.imshow('edge', e)
    cv2.imshow('edge1', edge1)
    cv2.imshow('edge2', edge2)
    s = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
    edge3 = cv2.erode(edge1, s)
    cv2.imshow('edge3', edge3)
    cv2.waitKey()