from django.contrib import admin
from django.urls import path
from cowsay import views

urlpatterns = [
    path('', views.index),
    path('history/', views.history)
]