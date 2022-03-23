from multiprocessing.sharedctypes import Value
from django.template import context
from django.shortcuts import render
from .models import Student
# Create your views here.
def studentData(request):
    
    students = Student.objects.all().values()
    students1 = Student.objects.filter(student_name__startswith='p').values()
    students2 = Student.objects.filter(student_name__contains='D').values()
    students3 = Student.objects.filter(role_id__gt=1).values()
    print('gt----',students3)
    print('filter==',students2)
    print('s1====',students1)
    print(students[0].get('id'))
    print(students[0])

    studentlist = []
    # for student in students:
    #     print(student.get('id'))
    for i in students[0].values():
        studentlist.append(i)
    print("student list=",studentlist)
    context = {
        'students':studentlist
    }
    return render (request,'orm/student.html',context)