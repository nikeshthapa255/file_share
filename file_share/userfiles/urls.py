from django.contrib import admin
from django.urls import path, include
from .views import UfileView, ShowFiles

app_name='userfiles'


urlpatterns = [
    path('show/',ShowFiles, name="show"),
    path("",UfileView.as_view(), name="home"),


]