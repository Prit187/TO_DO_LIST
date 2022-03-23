from django.http import HttpResponse
from django.shortcuts import render
from .models import Employee
# Create your views here.
def addEmployee(request):
    # INSERT....INSERT.....INSERT....
    emp = Employee(ename='Arkan',eage=25,eemail='Arkan@gmail.com',econtact=123546897)
    emp.save()
    # return render(request,'employee/addEmployee.html')
    return HttpResponse("Employee Add....")

def viewEmployee(request):
    employees = Employee.objects.all().values_list()
    print(employees)
    return render(request,'employee/view.html',{'employees':employees})

# DELETE......DELETE....DELETE.......
def deleteEmployee(request):
    emp = Employee.objects.get(id=7) 
    emp.delete()
    return HttpResponse("Employee deleted...")

# UPDATE......UPDATE......UPDATE.....
def updateEmployee(request):
    emp = Employee.objects.get(id=8)
    # emp.id=1
    emp.eage = 30
    emp.econtact = 987654321
    emp.save()
    return HttpResponse('Employee updated')