from django.urls import path

from . import views

urlpatterns = [
    path('upload/', views.upload, name='upload'),
    path('preview/', views.preview, name='preview'),
    path('download/', views.download, name='download'),
    path('', views.colorch, name='colorch'),
]