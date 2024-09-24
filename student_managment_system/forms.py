from django import forms
from student_managment_system.models import Student
from django.core.validators import MinValueValidator, MaxValueValidator
#
# def validate_gpa(value):
#     if value < 0 or value > 4:
#         raise forms.ValidationError("GPA is invalid", params= {"value": value}
# )


class AddStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

    def clean_gpa(self):
        gpa = self.cleaned_data.get('gpa')
        if gpa < 0 or gpa > 4:
            raise forms.ValidationError("GPA must be between 0 and 4.")
        return gpa
