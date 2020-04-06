from django.shortcuts import redirect


def index(request):
    """首页"""
    return redirect('color_change:colorch', permanent=True)
