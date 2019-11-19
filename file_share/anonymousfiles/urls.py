from django.contrib import admin
from django.urls import path, include
from .views import AfileView

app_name='anonymousfiles'


urlpatterns = [
    path("",AfileView.as_view(), name="home"),

]