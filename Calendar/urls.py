from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('cal', views.CalendarView.as_view(), name='cal'),
]
