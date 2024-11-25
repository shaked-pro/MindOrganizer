from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name='home'),
    path('login/', views.authLogin , name='login'),
    path('register/', views.register , name='register'),
    path('dashboard/', views.dashboard , name='dashboard'),
    #path('dashboard/<str:pk>', views.dashboard , name='dashboard'),
    path('logout/', views.logoutUser , name='logout'),
]
