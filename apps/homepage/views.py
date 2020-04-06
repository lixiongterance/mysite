from django.shortcuts import redirect
from django.http import HttpResponse

from . import utils


def index(request):
    """首页"""
    return redirect('color_change:colorch', permanent=True)


def get_ver_code(request):
    """验证码"""
    img_bin, code = utils.create_verification_code()
    request.session['ver_code'] = code
    return HttpResponse(img_bin, content_type='image')
