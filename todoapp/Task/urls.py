from django.urls import path
from .views import CreateTask, TaskDetail, TaskList, UpdateTask
from .views import DeleteTask
from Task import views
urlpatterns = [
    path('add/',CreateTask.as_view()),
    path('view/',TaskList.as_view()),
    # path('view/',views.index),
    path('<pk>/delete/',DeleteTask.as_view()),
    path('<pk>/update/',UpdateTask.as_view()),
    path('<pk>/view/',TaskDetail.as_view()),



    
    
]