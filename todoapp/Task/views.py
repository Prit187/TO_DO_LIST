
from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView


from .models import Task
# Create your views here.
class CreateTask(CreateView):
    model = Task
    fields = ['task_name','task_description']
    template_name = 'Task/create_task.html'
    Success_url = '/task/view/'
    

class TaskList(ListView):
    model = Task
    tasklist = model.objects.all().values_list()
    template_name = 'Task/task_list.html'
    context_object_name = 'tasklist'

class DeleteTask(DeleteView):
    model =Task
    success_url = '/task/view/'

# def index(request):
#     return render (request,'Task/index.html')

class UpdateTask(UpdateView):
    model = Task
    fields = ['task_name','task_description']
    template_name = 'Task/update_task.html'
    Success_url = '/task/view/'

class TaskDetail(DetailView):
    model = Task
    template_name = 'Task/task_detail.html'
    
   
    

