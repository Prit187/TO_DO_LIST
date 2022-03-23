from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def project_team(request):
    return HttpResponse("project_team called..")

def index(request):
    context = {
        'name':'TodoList',
    }
    return render(request,'project_team/index.html',context)

def contactUs(request):
    context = {
        'contact_name':["Prit","Arkan","Kaif"]
    }
    return render(request,'project_team/contactUs.html',context)

def aboutUs(request):
    context = {
        'isActive':True,
        'age':20,
    }
    return render(request,'project_team/aboutUs.html',context)