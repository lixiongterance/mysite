from django.urls import path

from . import views

urlpatterns = [
    path(r'^$', views.colorch, name='colorch'),
    path(r'upload/', views.upload, name='upload'),
    path(r'', views.colorch, name='colorch'),
]