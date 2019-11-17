from django.contrib import admin
from django.urls import path
from .views import *
app_name='iapp1'
urlpatterns=[
    path('',index,name='index'),
    path('register/',register,name='register'),
    path('login/',userlogin,name='login'),
    path('logout/',userlogout,name='logout')
]