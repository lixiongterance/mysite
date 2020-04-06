import cv2
import numpy as np


def bg_color_cvt(img_bin, color):
    colors = {
        'red': (0, 0, 255),
        'blue': (255, 0, 0),
        'white': (255, 255, 255)
    }
    if color not in colors.keys():
        return None
    img = cv2.imdecode(np.asarray(bytearray(img_bin), dtype='uint8'), cv2.IMREAD_COLOR)
    rows, cols, channels = img.shape

    #转换hsv
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([90, 70, 70])
    upper_blue = np.array([110, 255, 255])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    #腐蚀膨胀
    erode = cv2.erode(mask, None, iterations=1)
    dilate = cv2.dilate(erode, None, iterations=1)

    #遍历替换
    for i in range(rows):
        for j in range(cols):
            if dilate[i, j] == 255:
                # 此处替换颜色，为BGR通道
                img[i, j] = colors[color]

    return np.array(cv2.imencode('.jpg', img)[1]).tobytes()
