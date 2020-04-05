from django.shortcuts import render
from django.http import Http404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect

import cv2
import numpy as np
import uuid

def bg_color_cvt(simg, dimg, color):
    # 蓝底->红底
    img = cv2.imread('~/tmp/test.jpg')
    rows, cols, channels = img.shape
    cv2.imshow('img_resized', img)

    #转换hsv
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # lower_blue=np.array([90,70,70])里面三个数值可以控制好处理出来的效果和噪点
    lower_blue = np.array([90, 70, 70])
    upper_blue = np.array([110, 255, 255])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    cv2.imshow('Mask', mask)

    #腐蚀膨胀
    erode = cv2.erode(mask, None, iterations=1)
    # cv2.imshow('erode', erode)
    dilate = cv2.dilate(erode, None, iterations=1)
    cv2.imshow('dilate', dilate)

    #遍历替换
    for i in range(rows):
        for j in range(cols):
            if dilate[i, j] == 255:
                # 此处替换颜色，为BGR通道
                img[i, j] = (0, 0, 255)

    # img = cv2.dilate(img, None, iterations=10)

    cv2.imshow('res', img)
    cv2.waitKey(10)
    cv2.destroyAllWindows()

    # cv2.imwrite(dimg, img)


file_tmp = './tmp/'

@csrf_protect
def colorch(request):
    """底色转换"""
    if request.method != 'POST':
        if not request.session.get('sid'):
            uid = str(uuid.uuid4()).split('-')
            request.session['sid'] = ''.join(uid)
        return render(request, 'color_ch.html')
    else:
        simg = ''
        dimg = ''
        color = ''
        bg_color_cvt(simg, dimg, color)
        return ''

def upload(request):
    """底色转换"""
    if request.method == 'POST':
        img_name = file_tmp + str(request.session.session_key)
        with open(img_name, 'wb') as f:
            f.write(request.FILES['pic'])
        return JsonResponse({'res': 'success'})
    else:
        raise Http404

def download(request):
    """下载"""
    return ''
