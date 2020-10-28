import cv2


image = cv2.imread("4.jpeg")
image = cv2.resize(image, (420*2, 297*2), interpolation=cv2.INTER_CUBIC)
blur = cv2.GaussianBlur(image, (3, 3), 0.5)
edge = cv2.Canny(blur, 50, 200)
contours, hc = cv2.findContours(edge, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 对于每一个轮廓进行拟合
n = len(contours)
for i in range(n):
    rect = cv2.boundingRect(contours[i])
    xmin, ymin, w, h = rect
    if w * h > 10000:
        cv2.rectangle(image, (xmin, ymin), (xmin+w, ymin+h), 255, 2)
        convexhull = cv2.convexHull(contours[i])
        k = convexhull.shape[0]
        for i in range(k-1):
            cv2.line(image,
                    (convexhull[i, 0, 0], convexhull[i, 0, 1]),
                    (convexhull[i+1, 0, 0], convexhull[i+1, 0, 1]), 255, 2)

        cv2.line(image, (convexhull[k-1, 0, 0], convexhull[k-1, 0, 1]),
                (convexhull[0, 0, 0], convexhull[0, 0, 1]), 255, 2)
cv2.imshow("edge", edge)
cv2.imshow("image", image)
cv2.waitKey()