from project_team import views
from django.urls import path

urlpatterns = [
    path('add/',views.project_team),
    path('contactUs/',views.contactUs),
    path('',views.index),
    path('aboutUs/',views.aboutUs),

]
