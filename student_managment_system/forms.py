from django import forms
from student_managment_system.models import Student

class AddStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_number', 'first_name', 'last_name', 'email', 'field_of_study','gpa']
