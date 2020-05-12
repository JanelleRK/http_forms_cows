from django.contrib import admin
from django.urls import path
from Cowsay.views import views

urlpatterns = [
    path('', views.index),
]