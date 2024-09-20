
from import_export import resources
from .models import Course, Student

# Register your models with admin
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

@admin.register(Student)
class StudentAdmin(ImportExportModelAdmin):
    list_display = ('name', 'age')
    list_filter = ("date_of_birth", 'age', 'courses')
    search_fields = ('name', 'age')


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_per_page = 5
    search_fields = ('name',)
