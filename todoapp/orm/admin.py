from django.contrib import admin
from .models import Developer, Project, ProjectManager, Role,Employee
from .models import Student


# Register your models here.
admin.site.register(Role)
admin.site.register(Employee)
admin.site.register(Student)
admin.site.register(ProjectManager)
admin.site.register(Developer)
admin.site.register(Project)
