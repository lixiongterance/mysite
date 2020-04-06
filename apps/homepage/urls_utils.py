from django.urls import re_path

from . import views

urlpatterns = [
    re_path('ver_code', views.get_ver_code, name='ver_code'),
]
