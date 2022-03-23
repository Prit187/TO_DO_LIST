from django.contrib import admin
from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path("user-registration/",BaseRegisterView.as_view(),name="user-registration"),
    path('login/', UserLoginView.as_view() ,name='userlogin'),
    path('index/',views.index)

]
 