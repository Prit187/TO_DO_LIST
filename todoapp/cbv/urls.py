from django.urls import path

from .views import HrList

urlpatterns = [
   path('list/',HrList.as_view()),
]