"""Djtest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from test0 import views
from django.conf.urls import url, include
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()

from test0.views import UserViews,HealthdataViews,DeviceViews,DivrecViews,PermissionViews

router.register(r'User', UserViews, basename='User') 
router.register(r'Healthdata', HealthdataViews, basename='Healthadata') 
router.register(r'Device', HealthdataViews, basename='Device') 
router.register(r'Divrec', HealthdataViews, basename='Divrec') 
router.register(r'Permission', HealthdataViews, basename='Permission') 
urlpatterns = [
   # path('admin/', admin.site.urls),
   path('index/',views.index),
   path('user/list/',views.user_list),
   path('sth/',views.sth),
   path('login/',views.login),
   path('admin/', admin.site.urls),
   path('user/', views.UsersView.as_view()),
   path('user/<int:pk>/', views.UsersView.as_view()),
   path('data/', views.HealthdataView.as_view()),
   path('data/<int:pk>/', views.HealthdataView.as_view()),
   url('/', include(router.urls)),
   path('api-auth/', include('rest_framework.urls', namespace='rest_framework')) 
]