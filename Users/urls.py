from django.urls import path
from . import views
app_name = 'Users'
urlpatterns = [
    path('', views.auth_view, name='auth'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),
]