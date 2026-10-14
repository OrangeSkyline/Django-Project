from django.contrib import admin
from .models import Portfolio, Project, Student

# Register your models here.
admin.site.register(Student)
admin.site.register(Portfolio)
admin.site.register(Project)
