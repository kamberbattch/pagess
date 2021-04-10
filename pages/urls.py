#The `urlpatterns` list routes URLs to views.

from django.contrib import admin
from django.urls import path, include # новое

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include('app_page.urls')), # новое
]