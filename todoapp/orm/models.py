from sre_constants import CATEGORY
from telnetlib import STATUS
from time import time
from django.db import models

# Create your models here.
class Role(models.Model):
    role_name = models.CharField(max_length=50)
    role_description = models.TextField()
    class Meta:
        db_table = 'role'

class Employee(Role):
    employee_name = models.CharField(max_length=50)
    employee_email = models.CharField(max_length=50)
    employee_password = models.CharField(max_length=50)
    employee_phone = models.CharField(max_length=10)
    employee_address = models.TextField()
    employee_dob = models.DateField()
    class Meta:
        db_table ='employee'

class Student(models.Model):
    # role_id = models.ForeignKey(Role, on_delete=models.CASCADE)
    role_id = models.OneToOneField(Role,on_delete=models.CASCADE)
    student_name = models.CharField(max_length=50)
    student_email = models.CharField(max_length=50)
    student_paswword= models.CharField(max_length=50)
    student_phone = models.CharField(max_length=50)
    student_dob = models.DateField()
    class Meta:
      db_table = 'student'

class ProjectManager(models.Model):
    pmanager_name = models.CharField(max_length=50)
    class meta:
        db_table = 'projectmanager'
    
class Developer(models.Model):
    CATEGORY = (('website','website'),('application','application'))
    name = models.CharField(max_length=200)
    time = models.TimeField()
    date_created = models.DateTimeField()
    class Meta:
        db_table = 'developer'

class Project(models.Model):
    STATUS = (('PENDING','PENDING'),('RUNNING','RUNNING'),('COMPLETED','COMPLETED'))
    projectmanager = models.ForeignKey(ProjectManager,null=True,on_delete=models.SET_NULL)
    developer1 = models.ForeignKey(Developer,null=True,on_delete=models.SET_NULL) 
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=200,choices=STATUS)
    class Meta:
        db_table = 'project1'

    
