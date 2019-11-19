from django.contrib import admin
from django.urls import path, include
from .views import AfileView, ShowFile

app_name='anonymousfiles'


urlpatterns = [
    path("file/<int:pk>",ShowFile, name="show"),
    path("",AfileView.as_view(), name="home"),

]