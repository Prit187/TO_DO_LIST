from pickle import FALSE
from django.db import models
from django.forms import BooleanField

# Create your models here.
#WE HAVE EXTENDED MODELS CLASS HERE TO USE MODEL'S CLASS VARIABLE
class Project(models.Model):
    project_name = models.CharField(max_length=30)
    project_description = models.TextField()
    project_technology = models.TextField()
    project_status =models.BooleanField(default=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=False)
    class Meta:
        db_table ='project'

class ProjectCategory(models.Model):
    category_name = models.CharField(max_length=50)
    category_descripation = models.TextField()
    class Meta:
        db_table ='category'