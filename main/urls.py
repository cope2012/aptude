from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainView.as_view(), name='main_view'),
    path('store', views.StoreFile.as_view(), name='store_view'),
]
