from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('report', views.report, name="report"),
    # path('bookir_chart1/', views.bookir_chart1, name='bookir_chart1'),
]
