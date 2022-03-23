from django.contrib import admin
from django.urls import include, path

from .views import AddServiceProvider, ViewServiceProvider, DetailServiceProvider, UpdateServiceProvider, DeleteServiceProvider

urlpatterns = [
   path('add/',AddServiceProvider.as_view(),name='add_serviceprovider'),
   path('view/',ViewServiceProvider.as_view(),name='view_serviceprovider'),
   path('<int:pk>/detail/',DetailServiceProvider.as_view(),name='detail_serviceprovider'),
   path('<int:pk>/update/',UpdateServiceProvider.as_view(),name='update_serviceprovider'),
   path('<int:pk>/delete/',DeleteServiceProvider.as_view(),name='delete_serviceprovider'),
   




]