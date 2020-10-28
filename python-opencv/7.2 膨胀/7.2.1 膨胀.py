import cv2


path = '4.jpeg'
image = cv2.imread(path)
cv2.imshow('image', image)
# image = cv2.Canny(image, 50, 200)
cv2.waitKey()
# 结构元半径
r = 1
MAX_R = 20

# 显示膨胀效果的窗口
cv2.namedWindow('dilate', 1)


def nothing(*args):
    pass


# 调节结构元半径
cv2.createTrackbar("r", "dilate", r, MAX_R, nothing)
while True:
    # 得到当前的r
    r = cv2.getTrackbarPos('r', 'dilate')
    # 创建结构元
    s = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,
                                  (2 * r + 1, 2 * r + 1))
    # 膨胀图像
    d = cv2.dilate(image, s)
    # 显示膨胀效果
    cv2.imshow("dilate", d)
    ch = cv2.waitKey(5)
    if ch == 27:
        break
cv2.destroyAllWindows()