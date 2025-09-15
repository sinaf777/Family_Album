from django.urls import path
from . import views

app_name = 'Sharing'

urlpatterns = [
    path('', views.sharing_list, name='sharing_list'),
    path('upload/', views.sharing_upload, name='sharing_upload'),
    path('<int:pk>/', views.sharing_detail, name='sharing_detail'),
]