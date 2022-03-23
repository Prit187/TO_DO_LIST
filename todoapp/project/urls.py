from django import views
from django.urls import path
from project import views
urlpatterns = [
    path('addproject/',views.addProject),
    path('viewproject/',views.viewProject),
    path('projectpage/',views.projectpage),

]
