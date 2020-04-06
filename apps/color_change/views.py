from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_protect

import cv2
import numpy as np

from . import utils


def colorch(request):
    """底色转换页面"""
    return render(request, 'html/color_ch.html')


@csrf_protect
def upload(request):
    """底色转换"""
    if request.method == 'POST':
        param = request.POST

        # 验证码检查
        code = request.session.get('ver_code')
        if code and code.lower() == param['ver_code'].lower():

            # 文件检查
            if request.FILES.get('img') is not None:
                simg_bin = request.FILES['img'].read()
            else:
                return JsonResponse({'res': 'Need an image'})

            # 图片底色转换
            dimg_bin = utils.bg_color_cvt(simg_bin, param['bg_color'])
            if dimg_bin is None:
                return JsonResponse({'res': 'No such color'})

            return HttpResponse(dimg_bin, content_type='image')
        else:
            return JsonResponse({'res': 'ver_code wrong'})
    else:
        raise Http404
