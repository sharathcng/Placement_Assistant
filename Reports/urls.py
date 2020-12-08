from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    #path('report', views.report, name="report"),
    path('report/', views.bookir_chart, name='report'),
]
