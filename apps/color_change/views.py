from django.shortcuts import render
from django.http import Http404
from django.http import StreamingHttpResponse, HttpResponse
from django.views.decorators.csrf import csrf_protect

import cv2
import numpy as np

def bg_color_cvt(img, color):
    colors = {
        'red': (0, 0, 255),
        'blue': (255, 0, 0),
        'white': (255, 255, 255)
    }
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


bg_colors = ['red', 'blue', 'white']

def colorch(request):
    """底色转换页面"""
    return render(request, 'color_ch.html')

@csrf_protect
def upload(request):
    """底色转换"""
    if request.method == 'POST':
        param = request.POST
        if param['bg_color'] not in bg_colors:
            raise Http404

        simg_bin = request.FILES['img'].read()
        simg = cv2.imdecode(np.asarray(bytearray(simg_bin), dtype='uint8'), cv2.IMREAD_COLOR)

        bg_color_cvt(simg, param['bg_color'])

        dimg_bin = np.array(cv2.imencode('.jpg', simg)[1]).tobytes()
        return HttpResponse(dimg_bin, content_type='image')
    else:
        raise Http404
