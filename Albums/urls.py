from django.urls import path, include
from . import views

app_name = 'albums'

urlpatterns = [
    path('', views.album_list, name='album_list'),
    path('create/', views.album_create, name='album_create'),
    path('<int:pk>/', views.album_detail, name='album_detail'),
    path('<int:album_id>/upload/', views.photo_upload, name='photo_upload'),
]