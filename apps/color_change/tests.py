# from django.test import TestCase

# Create your tests here.

import cv2
import numpy as np

def color_change_test():
    # lower_blue=np.array([90,70,70])里面三个数值可以控制好处理出来的效果和噪点
    img = cv2.imread('test.jpg')
    #缩放
    rows, cols, channels = img.shape
    # cv2.imshow('img_resized', img)

    #转换hsv
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([90, 70, 70])
    upper_blue = np.array([110, 255, 255])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    # cv2.imshow('Mask', mask)

    #腐蚀膨胀
    erode = cv2.erode(mask, None, iterations=1)
    # cv2.imshow('erode', erode)
    dilate = cv2.dilate(erode, None, iterations=1)
    # cv2.imshow('dilate', dilate)

    #遍历替换
    for i in range(rows):
        for j in range(cols):
            if dilate[i, j] == 255:
                img[i, j] = (0, 0, 255) #此处替换颜色，为BGR通道

    # cv2.imshow('res', img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    dimg_bin = np.array(cv2.imencode('.jpg', img)[1]).tobytes()
    with open('t1.jpg', 'wb') as f:
        f.write(dimg_bin)
