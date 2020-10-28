import cv2


path = 'roi.jpeg'
image = cv2.imread(path)
# 显示原来的图像
cv2.imshow("image", image)

# 结构元半径，迭代次数
r, i = 1, 1
MAX_R, MAX_I = 20, 20
# 显示形态学处理的窗口
cv2.namedWindow("morphology", 1)


def nothing(*args):
    pass


# 调节结构元半径
cv2.createTrackbar("r", 'morphology', r, MAX_R, nothing)

# 调节迭代的次数
cv2.createTrackbar("i", 'morphology', i, MAX_I, nothing)

while True:
    # 得到进度条上当前的r值
    r = cv2.getTrackbarPos('r', 'morphology')
    # 得到进度条上当前的i值
    i = cv2.getTrackbarPos('i', 'morphology')
    # 创建结构元
    s = cv2.getStructuringElement(cv2.MORPH_RECT, (2*r+1, 2*r+1))
    # 形态学处理
    d = cv2.morphologyEx(image, cv2.MORPH_TOPHAT, s, iterations=i)

    # 显示效果
    cv2.imshow("morphology", d)
    ch = cv2.waitKey(5)
    if ch == 27:
        break
cv2.destroyAllWindows() 
