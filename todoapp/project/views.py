 # Create your views here.


from django.http import HttpResponse
from django.shortcuts import render


def addProject(request):
    return HttpResponse("addproject called...")
 
def viewProject(request):
    return HttpResponse("viewproject called...")

def projectpage(request):
    return render(request,'project/projectpage.html')