from django.contrib import admin

from students.models import Student, Course
from django.core.exceptions import ValidationError
from django.db import models
# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass