from django.contrib import admin
from django.urls import include, path
from generic import views
from .import views

urlpatterns = [
   path('',views.index,name='index')
]
