from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('index/', views.index),
    path('login/', views.login),
    path('register/', views.register),
    path('logout/', views.logout),
    path('findpassword/', views.findpassword),
    path('captcha', include('captcha.urls')),
]