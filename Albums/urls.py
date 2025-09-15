from django.urls import path, include
from . import views

app_name = 'Albums'

urlpatterns = [
    path('', views.album_list, name='album_list'),
    path('upload/', views.album_upload, name='album_upload'),
    path('<int:pk>/', views.album_detail, name='album_detail'),
]