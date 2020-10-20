from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('D_Head', views.D_Head, name="D_Head"),
]