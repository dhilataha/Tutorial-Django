from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('recent/', views.recent),
    path('legend/', views.legend, name= 'legend'),
    path('news/', views.news, name='news'),
    path('', views.index),
]
